import asyncio
import base64
from decimal import Decimal
import json
import logging
import os
from pathlib import Path
import pkg_resources
import platform
from pprint import pformat
import secrets
import shutil
import signal
import struct
import sys
from typing import (
    Any, Optional, Union,
    Dict, Mapping, MutableMapping,
    Set,
    List, Tuple,
    Type,
)
from typing_extensions import Literal

import aiohttp
import attr
from async_timeout import timeout
import zmq
import trafaret as t

from aiodocker.docker import Docker
from aiodocker.exceptions import DockerError
import aiotools

from ai.backend.common.docker import (
    ImageRef,
    MIN_KERNELSPEC,
    MAX_KERNELSPEC,
)
from ai.backend.common.exception import ImageNotAvailable
from ai.backend.common.logging import BraceStyleAdapter
from ai.backend.common.types import (
    AutoPullBehavior,
    ImageRegistry,
    KernelCreationConfig,
    KernelCreationResult,
    KernelId,
    DeviceName,
    SlotName,
    MetricKey, MetricValue,
    MountPermission,
    MountTypes,
    ResourceSlot,
    ServicePort,
    SessionTypes,
    ServicePortProtocols,
    current_resource_slots,
)
from .kernel import DockerKernel
from .resources import detect_resources
from ..exception import UnsupportedResource, InsufficientResource
from ..fs import create_scratch_filesystem, destroy_scratch_filesystem
from ..kernel import match_krunner_volume, KernelFeatures
from ..resources import (
    Mount,
    KernelResourceSpec,
)
from ..agent import (
    AbstractAgent,
    ipc_base_path,
)
from ..proxy import proxy_connection, DomainSocketProxy
from ..resources import (
    AbstractComputePlugin,
    known_slot_types,
)
from ..server import (
    get_extra_volumes,
)
from ..stats import (
    spawn_stat_synchronizer, StatSyncState
)
from ..utils import (
    update_nested_dict,
    get_kernel_id_from_container,
    host_pid_to_container_pid,
    container_pid_to_host_pid,
    parse_service_ports,
)

log = BraceStyleAdapter(logging.getLogger(__name__))


class DockerAgent(AbstractAgent):

    docker: Docker
    monitor_fetch_task: asyncio.Task
    monitor_handle_task: asyncio.Task
    agent_sockpath: Path
    agent_sock_task: asyncio.Task
    scan_images_timer: asyncio.Task

    def __init__(self, config, *, skip_initial_scan: bool = False) -> None:
        super().__init__(config, skip_initial_scan=skip_initial_scan)

    async def __ainit__(self) -> None:
        self.docker = Docker()
        if not self._skip_initial_scan:
            docker_version = await self.docker.version()
            log.info('running with Docker {0} with API {1}',
                     docker_version['Version'], docker_version['ApiVersion'])
        await super().__ainit__()
        self.agent_sockpath = ipc_base_path / f'agent.{self.agent_id}.sock'
        self.agent_sock_task = self.loop.create_task(self.handle_agent_socket())
        self.monitor_fetch_task  = self.loop.create_task(self.fetch_docker_events())
        self.monitor_handle_task = self.loop.create_task(self.handle_docker_events())

    async def shutdown(self, stop_signal: signal.Signals):
        try:
            await super().shutdown(stop_signal)
        finally:
            # Stop docker event monitoring.
            if self.monitor_fetch_task is not None:
                self.monitor_fetch_task.cancel()
                self.monitor_handle_task.cancel()
                await self.monitor_fetch_task
                await self.monitor_handle_task
            try:
                await self.docker.events.stop()
            except Exception:
                pass
            await self.docker.close()

        # Stop handlign agent sock.
        # (But we don't remove the socket file)
        if self.agent_sock_task is not None:
            self.agent_sock_task.cancel()
            await self.agent_sock_task

    @staticmethod
    async def detect_resources(resource_configs: Mapping[str, Any],
                               plugin_configs: Mapping[str, Any]) \
                               -> Tuple[
                                   Mapping[DeviceName, Type[AbstractComputePlugin]],
                                   Mapping[SlotName, Decimal]
                               ]:
        return await detect_resources(resource_configs, plugin_configs)

    async def scan_running_kernels(self) -> None:
        for container in (await self.docker.containers.list()):
            kernel_id = await get_kernel_id_from_container(container)
            if kernel_id is None:
                continue
            # NOTE: get_kernel_id_from_containers already performs .show() on
            #       the returned container objects.
            status = container['State']['Status']
            if status in {'running', 'restarting', 'paused'}:
                log.info('detected running kernel: {0}', kernel_id)
                await container.show()
                image = container['Config']['Image']
                labels = container['Config']['Labels']
                kernelspec = int(labels.get('ai.backend.kernelspec', '1'))
                if not (MIN_KERNELSPEC <= kernelspec <= MAX_KERNELSPEC):
                    continue
                ports = container['NetworkSettings']['Ports']
                port_map = {}
                for private_port, host_ports in ports.items():
                    private_port = int(private_port.split('/')[0])
                    if host_ports is None:
                        public_port = 0
                    else:
                        public_port = int(host_ports[0]['HostPort'])
                        self.port_pool.discard(public_port)
                    port_map[private_port] = public_port
                for computer_set in self.computers.values():
                    await computer_set.klass.restore_from_container(
                        container, computer_set.alloc_map)
                kernel_host = self.config['container']['kernel-host']
                config_dir = (self.config['container']['scratch-root'] /
                              str(kernel_id) / 'config').resolve()
                with open(config_dir / 'resource.txt', 'r') as f:
                    resource_spec = KernelResourceSpec.read_from_file(f)
                    # legacy handling
                    if resource_spec.container_id is None:
                        resource_spec.container_id = container._id
                    else:
                        assert container._id == resource_spec.container_id, \
                                'Container ID from the container must match!'
                # TODO: restore internal_data
                #       -> could we get this from the manager again?
                service_ports: List[ServicePort] = []
                service_ports.append({
                    'name': 'sshd',
                    'protocol': ServicePortProtocols('tcp'),
                    'container_ports': (2200,),
                    'host_ports': (port_map.get(2200, None),),
                })
                service_ports.append({
                    'name': 'ttyd',
                    'protocol': ServicePortProtocols('http'),
                    'container_ports': (7681,),
                    'host_ports': (port_map.get(7681, None),),
                })
                for service_port in parse_service_ports(labels.get('ai.backend.service-ports', '')):
                    service_port['host_ports'] = tuple(
                        port_map.get(cport, None) for cport in service_port['container_ports']
                    )
                    service_ports.append(service_port)
                block_service_ports = labels.get('ai.backend.internal.block-service-ports', '0')
                self.kernel_registry[kernel_id] = await DockerKernel.new(
                    kernel_id,
                    ImageRef(image),
                    kernelspec,
                    agent_config=self.config,
                    resource_spec=resource_spec,
                    service_ports=service_ports,
                    data={
                        'container_id': container._id,
                        'kernel_host': kernel_host,
                        'repl_in_port': port_map[2000],
                        'repl_out_port': port_map[2001],
                        'stdin_port': port_map.get(2002, 0),
                        'stdout_port': port_map.get(2003, 0),
                        'host_ports': [*port_map.values()],
                        'block_service_ports': t.ToBool().check(block_service_ports),
                    })
            elif status in {'exited', 'dead', 'removing'}:
                log.info('detected terminated kernel: {0}', kernel_id)
                await self.produce_event('kernel_terminated', str(kernel_id),
                                         'self-terminated', None)

        log.info('starting with resource allocations')
        for computer_name, computer_ctx in self.computers.items():
            log.info('{}: {!r}', computer_name,
                        dict(computer_ctx.alloc_map.allocations))

    async def scan_images(self, interval: float = None) -> None:
        all_images = await self.docker.images.list()
        updated_images = {}
        for image in all_images:
            if image['RepoTags'] is None:
                continue
            for repo_tag in image['RepoTags']:
                if repo_tag.endswith('<none>'):
                    continue
                img_detail = await self.docker.images.inspect(repo_tag)
                labels = img_detail['Config']['Labels']
                if labels is None or 'ai.backend.kernelspec' not in labels:
                    continue
                kernelspec = int(labels['ai.backend.kernelspec'])
                if MIN_KERNELSPEC <= kernelspec <= MAX_KERNELSPEC:
                    updated_images[repo_tag] = img_detail['Id']
        for added_image in (updated_images.keys() - self.images.keys()):
            log.debug('found kernel image: {0}', added_image)
        for removed_image in (self.images.keys() - updated_images.keys()):
            log.debug('removed kernel image: {0}', removed_image)
        self.images = updated_images

    async def handle_agent_socket(self):
        '''
        A simple request-reply socket handler for in-container processes.
        For ease of implementation in low-level languages such as C,
        it uses a simple C-friendly ZeroMQ-based multipart messaging protocol.

        Request message:
            The first part is the requested action as string,
            The second part and later are arguments.

        Reply message:
            The first part is a 32-bit integer (int in C)
                (0: success)
                (-1: generic unhandled error)
                (-2: invalid action)
            The second part and later are arguments.

        All strings are UTF-8 encoded.
        '''
        my_uid = os.geteuid()
        my_gid = os.getegid()
        kernel_uid = self.config['container']['kernel-uid']
        kernel_gid = self.config['container']['kernel-gid']
        try:
            agent_sock = self.zmq_ctx.socket(zmq.REP)
            agent_sock.bind(f'ipc://{self.agent_sockpath}')
            if my_uid == 0:
                os.chown(self.agent_sockpath, kernel_uid, kernel_gid)
            else:
                if my_uid != kernel_uid:
                    log.error('The UID of agent ({}) must be same to the container UID ({}).',
                              my_uid, kernel_uid)
                if my_gid != kernel_gid:
                    log.error('The GID of agent ({}) must be same to the container GID ({}).',
                              my_gid, kernel_gid)
            while True:
                msg = await agent_sock.recv_multipart()
                if not msg:
                    break
                try:
                    if msg[0] == b'host-pid-to-container-pid':
                        container_id = msg[1].decode()
                        host_pid = struct.unpack('i', msg[2])[0]
                        container_pid = await host_pid_to_container_pid(
                            container_id, host_pid)
                        reply = [
                            struct.pack('i', 0),
                            struct.pack('i', container_pid),
                        ]
                    elif msg[0] == b'container-pid-to-host-pid':
                        container_id = msg[1].decode()
                        container_pid = struct.unpack('i', msg[2])[0]
                        host_pid = await container_pid_to_host_pid(
                            container_id, container_pid)
                        reply = [
                            struct.pack('i', 0),
                            struct.pack('i', host_pid),
                        ]
                    else:
                        reply = [struct.pack('i', -2), b'Invalid action']
                except asyncio.CancelledError:
                    raise
                except Exception as e:
                    reply = [struct.pack('i', -1), f'Error: {e}'.encode('utf-8')]
                await agent_sock.send_multipart(reply)
        except asyncio.CancelledError:
            pass
        except zmq.ZMQError:
            log.exception('zmq socket error with {}', self.agent_sockpath)
        finally:
            agent_sock.close()

    async def pull_image(self, image_ref: ImageRef, registry_conf: ImageRegistry) -> None:
        auth_config = None
        reg_user = registry_conf.get('username')
        reg_passwd = registry_conf.get('password')
        if reg_user and reg_passwd:
            encoded_creds = base64.b64encode(
                f'{reg_user}:{reg_passwd}'.encode('utf-8')) \
                .decode('ascii')
            auth_config = {
                'auth': encoded_creds,
            }
        log.info('pulling image {} from registry', image_ref.canonical)
        await self.docker.images.pull(
            image_ref.canonical,
            auth=auth_config)

    async def check_image(self, image_ref: ImageRef, image_id: str, auto_pull: AutoPullBehavior) -> bool:
        try:
            image_info = await self.docker.images.inspect(image_ref.canonical)
            if auto_pull == AutoPullBehavior.DIGEST:
                if image_info['Id'] != image_id:
                    return True
            log.info('found the local up-to-date image for {}', image_ref.canonical)
        except DockerError as e:
            if e.status == 404:
                if auto_pull == AutoPullBehavior.DIGEST:
                    return True
                elif auto_pull == AutoPullBehavior.TAG:
                    return True
                elif auto_pull == AutoPullBehavior.NONE:
                    raise ImageNotAvailable(image_ref)
            else:
                raise
        return False

    async def get_service_ports_from_label(self, image_ref: ImageRef) -> str:
        image_info = await self.docker.images.inspect(image_ref.canonical)
        return image_info['Config']['Labels']['ai.backend.service-ports']

    async def create_kernel(self, kernel_id: KernelId, kernel_config: KernelCreationConfig, *,
                            restarting: bool = False) -> KernelCreationResult:

        await self.produce_event('kernel_preparing', str(kernel_id))

        log.debug('Kernel Creation Config: {0}', json.dumps(kernel_config))
        # Read image-specific labels and settings
        image_ref = ImageRef(
            kernel_config['image']['canonical'],
            [kernel_config['image']['registry']['name']])
        environ: MutableMapping[str, str] = {**kernel_config['environ']}
        extra_mount_list = await get_extra_volumes(self.docker, image_ref.short)
        internal_data: Mapping[str, Any] = kernel_config.get('internal_data') or {}

        do_pull = await self.check_image(
            image_ref,
            kernel_config['image']['digest'],
            AutoPullBehavior(kernel_config.get('auto_pull', 'digest')),
        )
        if do_pull:
            await self.produce_event('kernel_pulling',
                                     str(kernel_id), image_ref.canonical)
            await self.pull_image(image_ref, kernel_config['image']['registry'])

        await self.produce_event('kernel_creating', str(kernel_id))
        image_labels = kernel_config['image']['labels']
        version = int(image_labels.get('ai.backend.kernelspec', '1'))
        label_envs_corecount = image_labels.get('ai.backend.envs.corecount', '')
        envs_corecount = label_envs_corecount.split(',') if label_envs_corecount else []
        kernel_features = set(image_labels.get('ai.backend.features', '').split())

        scratch_dir = (self.config['container']['scratch-root'] / str(kernel_id)).resolve()
        tmp_dir = (self.config['container']['scratch-root'] / f'{kernel_id}_tmp').resolve()
        config_dir = scratch_dir / 'config'
        work_dir = scratch_dir / 'work'

        # PHASE 1: Read existing resource spec or devise a new resource spec.

        if restarting:
            with open(config_dir / 'resource.txt', 'r') as f:
                resource_spec = KernelResourceSpec.read_from_file(f)
            resource_opts = None
        else:
            slots = ResourceSlot.from_json(kernel_config['resource_slots'])
            # accept unknown slot type with zero values
            # but reject if they have non-zero values.
            for st, sv in slots.items():
                if st not in known_slot_types and sv != Decimal(0):
                    raise UnsupportedResource(st)
            # sanitize the slots
            current_resource_slots.set(known_slot_types)
            slots = slots.normalize_slots(ignore_unknown=True)
            vfolders = kernel_config['mounts']
            vfolder_mount_map: Mapping[str, str] = {}
            if 'mount_map' in kernel_config.keys():
                vfolder_mount_map = kernel_config['mount_map']
            resource_spec = KernelResourceSpec(
                container_id='',
                allocations={},
                slots={**slots},  # copy
                mounts=[],
                scratch_disk_size=0,  # TODO: implement (#70)
                idle_timeout=kernel_config['idle_timeout'],
            )
            resource_opts = kernel_config.get('resource_opts', {})

        # PHASE 2: Apply the resource spec.

        # Inject Backend.AI-intrinsic env-variables for gosu
        if KernelFeatures.UID_MATCH in kernel_features:
            uid = self.config['container']['kernel-uid']
            gid = self.config['container']['kernel-gid']
            environ['LOCAL_USER_ID'] = str(uid)
            environ['LOCAL_GROUP_ID'] = str(gid)

        # Inject Backend.AI-intrinsic mount points and extra mounts
        mounts: List[Mount] = [
            Mount(MountTypes.BIND, config_dir, '/home/config',
                  MountPermission.READ_ONLY),
            Mount(MountTypes.BIND, work_dir, '/home/work',
                  MountPermission.READ_WRITE),
        ]
        if (sys.platform.startswith('linux') and
            self.config['container']['scratch-type'] == 'memory'):
            mounts.append(Mount(MountTypes.BIND, tmp_dir, '/tmp',
                                MountPermission.READ_WRITE))
        mounts.extend(Mount(MountTypes.VOLUME, v.name, v.container_path, v.mode)
                      for v in extra_mount_list)

        if restarting:
            # Reuse previous CPU share.
            pass

            # Reuse previous memory share.
            pass

            # Reuse previous accelerator share.
            pass

            # Reuse previous mounts.
            for mount in resource_spec.mounts:
                mounts.append(mount)
        else:
            # Ensure that we have intrinsic slots.
            assert SlotName('cpu') in slots
            assert SlotName('mem') in slots

            # Realize ComputeDevice (including accelerators) allocations.
            dev_names: Set[SlotName] = set()
            for slot_name in slots.keys():
                dev_name = slot_name.split('.', maxsplit=1)[0]
                dev_names.add(dev_name)

            try:
                for dev_name in dev_names:
                    computer_set = self.computers[dev_name]
                    device_specific_slots = {
                        slot_name: alloc
                        for slot_name, alloc in slots.items()
                        if slot_name.startswith(dev_name)
                    }
                    resource_spec.allocations[dev_name] = \
                        computer_set.alloc_map.allocate(
                            device_specific_slots,
                            context_tag=dev_name)
            except InsufficientResource:
                log.info('insufficient resource: {} of {}\n'
                         '(alloc map: {})',
                         device_specific_slots, dev_name,
                         computer_set.alloc_map.allocations)
                raise

            # Realize vfolder mounts.
            for vfolder in vfolders:
                if len(vfolder) == 5:
                    folder_name, folder_host, folder_id, folder_perm, host_path_raw = vfolder
                    if host_path_raw:
                        host_path = Path(host_path_raw)
                    else:
                        host_path = (self.config['vfolder']['mount'] / folder_host /
                                     self.config['vfolder']['fsprefix'] / folder_id)
                elif len(vfolder) == 4:  # for backward compatibility
                    folder_name, folder_host, folder_id, folder_perm = vfolder
                    host_path = (self.config['vfolder']['mount'] / folder_host /
                                 self.config['vfolder']['fsprefix'] / folder_id)
                elif len(vfolder) == 3:  # legacy managers
                    folder_name, folder_host, folder_id = vfolder
                    folder_perm = 'rw'
                    host_path = (self.config['vfolder']['mount'] / folder_host /
                                 self.config['vfolder']['fsprefix'] / folder_id)
                else:
                    raise RuntimeError(
                        'Unexpected number of vfolder mount detail tuple size')
                if internal_data.get('prevent_vfolder_mounts', False):
                    # Only allow mount of ".logs" directory to prevent expose
                    # internal-only information, such as Docker credentials to user's ".docker" vfolder
                    # in image importer kernels.
                    if folder_name != '.logs':
                        continue
                # TODO: Remove `type: ignore` when mypy supports type inference for walrus operator
                # Check https://github.com/python/mypy/issues/7316
                # TODO: remove `NOQA` when flake8 supports Python 3.8 and walrus operator
                # Check https://gitlab.com/pycqa/flake8/issues/599
                if kernel_path_raw := vfolder_mount_map.get(folder_name):
                    if not kernel_path_raw.startswith('/home/work/'):  # type: ignore
                        raise ValueError(
                            f'Error while mounting {folder_name} to {kernel_path_raw}: '
                            'all vfolder mounts should be under /home/work')
                    kernel_path = Path(kernel_path_raw)  # type: ignore
                else:
                    kernel_path = Path(f'/home/work/{folder_name}')
                folder_perm = MountPermission(folder_perm)
                if folder_perm == MountPermission.RW_DELETE:
                    # TODO: enforce readable/writable but not deletable
                    # (Currently docker's READ_WRITE includes DELETE)
                    folder_perm = MountPermission.READ_WRITE
                mount = Mount(MountTypes.BIND, host_path, kernel_path, folder_perm)
                resource_spec.mounts.append(mount)
                mounts.append(mount)

            # should no longer be used!
            del vfolders

        # Inject Backend.AI-intrinsic env-variables for libbaihook and gosu
        cpu_core_count = len(resource_spec.allocations[DeviceName('cpu')][SlotName('cpu')])
        environ.update({k: str(cpu_core_count) for k in envs_corecount})

        def _mount(type: MountTypes,
                   src: Union[str, Path], target: Union[str, Path],
                   perm: Literal['ro', 'rw'] = 'ro',
                   opts: Mapping[str, Any] = None) -> None:
            nonlocal mounts
            mounts.append(Mount(type, src, target, MountPermission(perm), opts=opts))

        # Inject Backend.AI kernel runner dependencies.
        distro = image_labels.get('ai.backend.base-distro', 'ubuntu16.04')
        matched_distro, krunner_volume = match_krunner_volume(
            self.config['container']['krunner-volumes'], distro)
        matched_libc_style = 'glibc'
        if matched_distro.startswith('alpine'):
            matched_libc_style = 'musl'
        log.debug('selected krunner: {}', matched_distro)
        log.debug('selected libc style: {}', matched_libc_style)
        log.debug('krunner volume: {}', krunner_volume)
        arch = platform.machine()
        entrypoint_sh_path = Path(pkg_resources.resource_filename(
            'ai.backend.agent', '../runner/entrypoint.sh'))
        if matched_distro == 'centos6.10':
            # special case for image importer kernel (manylinux2010 is based on CentOS 6)
            suexec_path = Path(pkg_resources.resource_filename(
                'ai.backend.agent', f'../runner/su-exec.centos7.6.{arch}.bin'))
            hook_path = Path(pkg_resources.resource_filename(
                'ai.backend.agent', f'../runner/libbaihook.centos7.6.{arch}.so'))
            sftp_server_path = Path(pkg_resources.resource_filename(
                'ai.backend.agent',
                f'../runner/sftp-server.centos7.6.{arch}.bin'))
            scp_path = Path(pkg_resources.resource_filename(
                'ai.backend.agent',
                f'../runner/scp.centos7.6.{arch}.bin'))
        else:
            suexec_path = Path(pkg_resources.resource_filename(
                'ai.backend.agent', f'../runner/su-exec.{matched_distro}.{arch}.bin'))
            hook_path = Path(pkg_resources.resource_filename(
                'ai.backend.agent', f'../runner/libbaihook.{matched_distro}.{arch}.so'))
            sftp_server_path = Path(pkg_resources.resource_filename(
                'ai.backend.agent',
                f'../runner/sftp-server.{matched_distro}.{arch}.bin'))
            scp_path = Path(pkg_resources.resource_filename(
                'ai.backend.agent',
                f'../runner/scp.{matched_distro}.{arch}.bin'))
        if self.config['container']['sandbox-type'] == 'jail':
            jail_path = Path(pkg_resources.resource_filename(
                'ai.backend.agent', f'../runner/jail.{matched_distro}.bin'))
        kernel_pkg_path = Path(pkg_resources.resource_filename(
            'ai.backend.agent', '../kernel'))
        helpers_pkg_path = Path(pkg_resources.resource_filename(
            'ai.backend.agent', '../helpers'))
        jupyter_custom_css_path = Path(pkg_resources.resource_filename(
            'ai.backend.agent', '../runner/jupyter-custom.css'))
        logo_path = Path(pkg_resources.resource_filename(
            'ai.backend.agent', '../runner/logo.svg'))
        font_path = Path(pkg_resources.resource_filename(
            'ai.backend.agent', '../runner/roboto.ttf'))
        font_italic_path = Path(pkg_resources.resource_filename(
            'ai.backend.agent', '../runner/roboto-italic.ttf'))

        dropbear_path = Path(pkg_resources.resource_filename(
            'ai.backend.agent',
            f'../runner/dropbear.{matched_libc_style}.{arch}.bin'))
        dropbearconv_path = Path(pkg_resources.resource_filename(
            'ai.backend.agent',
            f'../runner/dropbearconvert.{matched_libc_style}.{arch}.bin'))
        dropbearkey_path = Path(pkg_resources.resource_filename(
            'ai.backend.agent',
            f'../runner/dropbearkey.{matched_libc_style}.{arch}.bin'))

        bashrc_path = Path(pkg_resources.resource_filename(
            'ai.backend.agent', '../runner/.bashrc'))
        vimrc_path = Path(pkg_resources.resource_filename(
            'ai.backend.agent', '../runner/.vimrc'))

        _mount(MountTypes.BIND, self.agent_sockpath, '/opt/kernel/agent.sock', perm='rw')
        _mount(MountTypes.BIND, entrypoint_sh_path.resolve(), '/opt/kernel/entrypoint.sh')
        _mount(MountTypes.BIND, suexec_path.resolve(), '/opt/kernel/su-exec')
        if self.config['container']['sandbox-type'] == 'jail':
            _mount(MountTypes.BIND, jail_path.resolve(), '/opt/kernel/jail')
        _mount(MountTypes.BIND, hook_path.resolve(), '/opt/kernel/libbaihook.so')

        _mount(MountTypes.BIND, dropbear_path.resolve(), '/opt/kernel/dropbear')
        _mount(MountTypes.BIND, dropbearconv_path.resolve(), '/opt/kernel/dropbearconvert')
        _mount(MountTypes.BIND, dropbearkey_path.resolve(), '/opt/kernel/dropbearkey')
        _mount(MountTypes.BIND, sftp_server_path.resolve(), '/usr/libexec/sftp-server')
        _mount(MountTypes.BIND, scp_path.resolve(), '/usr/bin/scp')

        _mount(MountTypes.VOLUME, krunner_volume, '/opt/backend.ai')
        _mount(MountTypes.BIND, kernel_pkg_path.resolve(),
                                '/opt/backend.ai/lib/python3.6/site-packages/ai/backend/kernel')
        _mount(MountTypes.BIND, helpers_pkg_path.resolve(),
                                '/opt/backend.ai/lib/python3.6/site-packages/ai/backend/helpers')

        # Since these files are bind-mounted inside a bind-mounted directory,
        # we need to touch them first to avoid their "ghost" files are created
        # as root in the host-side filesystem, which prevents deletion of scratch
        # directories when the agent is running as non-root.
        (work_dir / '.jupyter' / 'custom').mkdir(parents=True, exist_ok=True)
        (work_dir / '.jupyter' / 'custom' / 'custom.css').write_bytes(b'')
        (work_dir / '.jupyter' / 'custom' / 'logo.svg').write_bytes(b'')
        (work_dir / '.jupyter' / 'custom' / 'roboto.ttf').write_bytes(b'')
        (work_dir / '.jupyter' / 'custom' / 'roboto-italic.ttf').write_bytes(b'')
        _mount(MountTypes.BIND, jupyter_custom_css_path.resolve(),
                                '/home/work/.jupyter/custom/custom.css')
        _mount(MountTypes.BIND, logo_path.resolve(), '/home/work/.jupyter/custom/logo.svg')
        _mount(MountTypes.BIND, font_path.resolve(), '/home/work/.jupyter/custom/roboto.ttf')
        _mount(MountTypes.BIND, font_italic_path.resolve(),
                                '/home/work/.jupyter/custom/roboto-italic.ttf')
        _mount(MountTypes.BIND, bashrc_path.resolve(), '/home/work/.bashrc')
        _mount(MountTypes.BIND, vimrc_path.resolve(), '/home/work/.vimrc')
        environ['LD_PRELOAD'] = '/opt/kernel/libbaihook.so'
        if self.config['debug']['coredump']['enabled']:
            _mount(MountTypes.BIND, self.config['debug']['coredump']['path'],
                                    self.config['debug']['coredump']['core_path'],
                                    perm='rw')

        domain_socket_proxies = []
        for host_sock_path in internal_data.get('domain_socket_proxies', []):
            (ipc_base_path / 'proxy').mkdir(parents=True, exist_ok=True)
            host_proxy_path = ipc_base_path / 'proxy' / f'{secrets.token_hex(12)}.sock'
            proxy_server = await asyncio.start_unix_server(
                aiotools.apartial(proxy_connection, host_sock_path),
                str(host_proxy_path))
            host_proxy_path.chmod(0o666)
            domain_socket_proxies.append(DomainSocketProxy(
                Path(host_sock_path),
                host_proxy_path,
                proxy_server,
            ))
            _mount(MountTypes.BIND, host_proxy_path, host_sock_path, perm='rw')

        # Inject ComputeDevice-specific env-varibles and hooks
        computer_docker_args: Dict[str, Any] = {}
        for dev_type, device_alloc in resource_spec.allocations.items():
            computer_set = self.computers[dev_type]
            update_nested_dict(computer_docker_args,
                               await computer_set.klass.generate_docker_args(
                                   self.docker, device_alloc))
            alloc_sum = Decimal(0)
            for dev_id, per_dev_alloc in device_alloc.items():
                alloc_sum += sum(per_dev_alloc.values())
            if alloc_sum > 0:
                hook_paths = await computer_set.klass.get_hooks(matched_distro, arch)
                if hook_paths:
                    log.debug('accelerator {} provides hooks: {}',
                              computer_set.klass.__name__,
                              ', '.join(map(str, hook_paths)))
                for hook_path in hook_paths:
                    container_hook_path = '/opt/kernel/lib{}{}.so'.format(
                        computer_set.klass.key, secrets.token_hex(6),
                    )
                    _mount(MountTypes.BIND, hook_path, container_hook_path)
                    environ['LD_PRELOAD'] += ':' + container_hook_path

        # PHASE 3: Store the resource spec.

        if restarting:
            pass
        else:
            os.makedirs(scratch_dir, exist_ok=True)
            if (sys.platform.startswith('linux') and
                self.config['container']['scratch-type'] == 'memory'):
                os.makedirs(tmp_dir, exist_ok=True)
                await create_scratch_filesystem(scratch_dir, 64)
                await create_scratch_filesystem(tmp_dir, 64)
            os.makedirs(work_dir, exist_ok=True)
            os.makedirs(work_dir / '.jupyter', exist_ok=True)
            if KernelFeatures.UID_MATCH in kernel_features:
                uid = self.config['container']['kernel-uid']
                gid = self.config['container']['kernel-gid']
                if os.geteuid() == 0:  # only possible when I am root.
                    os.chown(work_dir, uid, gid)
                    os.chown(work_dir / '.jupyter', uid, gid)
                    os.chown(work_dir / '.jupyter' / 'custom', uid, gid)
                    os.chown(bashrc_path, uid, gid)
                    os.chown(vimrc_path, uid, gid)
            # Create bootstrap.sh into workdir if needed
            # TODO: Remove `type: ignore` when mypy supports type inference for walrus operator
            # Check https://github.com/python/mypy/issues/7316
            # TODO: remove `NOQA` when flake8 supports Python 3.8 and walrus operator
            # Check https://gitlab.com/pycqa/flake8/issues/599
            if bootstrap := kernel_config.get('bootstrap_script'):
                with open(work_dir / 'bootstrap.sh', 'wb') as fw:
                    fw.write(base64.b64decode(bootstrap))  # type: ignore
            os.makedirs(config_dir, exist_ok=True)
            # Store custom environment variables for kernel runner.
            with open(config_dir / 'environ.txt', 'w') as f:
                for k, v in environ.items():
                    f.write(f'{k}={v}\n')
                accel_envs = computer_docker_args.get('Env', [])
                for env in accel_envs:
                    f.write(f'{env}\n')
            with open(config_dir / 'resource.txt', 'w') as f:
                resource_spec.write_to_file(f)
                for dev_type, device_alloc in resource_spec.allocations.items():
                    computer_ctx = self.computers[dev_type]
                    kvpairs = \
                        await computer_ctx.klass.generate_resource_data(device_alloc)
                    for k, v in kvpairs.items():
                        f.write(f'{k}={v}\n')
            with open(config_dir / 'kernel_id.txt', 'w') as f:
                f.write(kernel_id.hex)
            docker_creds = internal_data.get('docker_credentials')
            if docker_creds:
                (config_dir / 'docker-creds.json').write_text(json.dumps(docker_creds))

        # Create SSH keypair only if ssh_keypair internal_data exists and
        # /home/work/.ssh folder is not mounted.
        if internal_data.get('ssh_keypair'):
            for m in mounts:
                container_path = str(m).split(':')[1]
                if container_path == '/home/work/.ssh':
                    break
            else:
                pubkey = internal_data['ssh_keypair']['public_key'].encode('ascii')
                privkey = internal_data['ssh_keypair']['private_key'].encode('ascii')
                ssh_dir = work_dir / '.ssh'
                ssh_dir.mkdir(parents=True, exist_ok=True)
                ssh_dir.chmod(0o700)
                (ssh_dir / 'authorized_keys').write_bytes(pubkey)
                (ssh_dir / 'authorized_keys').chmod(0o600)
                (work_dir / 'id_container').write_bytes(privkey)
                (work_dir / 'id_container').chmod(0o600)
                if KernelFeatures.UID_MATCH in kernel_features:
                    uid = self.config['container']['kernel-uid']
                    gid = self.config['container']['kernel-gid']
                    if os.geteuid() == 0:  # only possible when I am root.
                        os.chown(ssh_dir, uid, gid)
                        os.chown(ssh_dir / 'authorized_keys', uid, gid)
                        os.chown(work_dir / 'id_container', uid, gid)

        # PHASE 4: Run!
        log.info('kernel {0} starting with resource spec: \n',
                 pformat(attr.asdict(resource_spec)))

        # TODO: Refactor out as separate "Docker execution driver plugin" (#68)
        #   - Refactor volumes/mounts lists to a plugin "mount" API
        #   - Refactor "/home/work" and "/opt/backend.ai" prefixes to be specified
        #     by the plugin implementation.

        exposed_ports = [2000, 2001]
        service_ports = []
        port_map = {}

        for sport in parse_service_ports(await self.get_service_ports_from_label(image_ref)):
            port_map[sport['name']] = sport
        for sport in parse_service_ports(image_labels.get('ai.backend.service-ports', '')):
            port_map[sport['name']] = sport
        port_map['sshd'] = {
            'name': 'sshd',
            'protocol': ServicePortProtocols('tcp'),
            'container_ports': (2200,),
            'host_ports': (None,),
        }

        port_map['ttyd'] = {
            'name': 'ttyd',
            'protocol': ServicePortProtocols('http'),
            'container_ports': (7681,),
            'host_ports': (None,),
        }
        for sport in port_map.values():
            service_ports.append(sport)
            for cport in sport['container_ports']:
                exposed_ports.append(cport)

        log.debug('exposed ports: {!r}', exposed_ports)

        kernel_host = self.config['container']['kernel-host']
        if len(exposed_ports) > len(self.port_pool):
            raise RuntimeError('Container ports are not sufficiently available.')
        host_ports = []
        for eport in exposed_ports:
            hport = self.port_pool.pop()
            host_ports.append(hport)

        runtime_type = image_labels.get('ai.backend.runtime-type', 'python')
        runtime_path = image_labels.get('ai.backend.runtime-path', None)
        cmdargs: List[str] = []
        if self.config['container']['sandbox-type'] == 'jail':
            cmdargs += [
                "/opt/kernel/jail",
                "-policy", "/etc/backend.ai/jail/policy.yml",
            ]
            if self.config['container']['jail-args']:
                cmdargs += map(lambda s: s.strip(), self.config['container']['jail-args'])
        cmdargs += [
            "/opt/backend.ai/bin/python",
            "-m", "ai.backend.kernel", runtime_type,
        ]
        if runtime_path is not None:
            cmdargs.append(runtime_path)
        container_config: MutableMapping[str, Any] = {
            'Image': image_ref.canonical,
            'Tty': True,
            'OpenStdin': True,
            'Privileged': False,
            'StopSignal': 'SIGINT',
            'ExposedPorts': {
                f'{port}/tcp': {} for port in exposed_ports
            },
            'EntryPoint': ["/opt/kernel/entrypoint.sh"],
            'Cmd': cmdargs,
            'Env': [f'{k}={v}' for k, v in environ.items()],
            'WorkingDir': '/home/work',
            'Labels': {
                'ai.backend.kernel-id': str(kernel_id),
                'ai.backend.internal.block-service-ports':
                    '1' if internal_data.get('block_service_ports', False) else '0'
            },
            'HostConfig': {
                'Init': True,
                'Mounts': [
                    {
                        'Target': str(mount.target),
                        'Source': str(mount.source),
                        'Type': mount.type.value,
                        'ReadOnly': mount.permission == MountPermission.READ_ONLY,
                        f'{mount.type.value.capitalize()}Options':
                            mount.opts if mount.opts else {},
                    }
                    for mount in mounts
                ],
                'PortBindings': {
                    f'{eport}/tcp': [{'HostPort': str(hport),
                                      'HostIp': str(kernel_host)}]
                    for eport, hport in zip(exposed_ports, host_ports)
                },
                'PublishAllPorts': False,  # we manage port mapping manually!
            },
        }
        if resource_opts and resource_opts.get('shmem'):
            shmem = resource_opts.get('shmem')
            computer_docker_args['HostConfig']['ShmSize'] = shmem
            computer_docker_args['HostConfig']['MemorySwap'] -= shmem
            computer_docker_args['HostConfig']['Memory'] -= shmem
        if self.config['container']['sandbox-type'] == 'jail':
            container_config['HostConfig']['SecurityOpt'] = [
                'seccomp=unconfined',
                'apparmor=unconfined',
            ]
        update_nested_dict(container_config, computer_docker_args)
        kernel_name = f"kernel.{image_ref.name.split('/')[-1]}.{kernel_id}"
        log.debug('container config: {!r}', container_config)

        # We are all set! Create and start the container.
        try:
            container = await self.docker.containers.create(
                config=container_config, name=kernel_name)
            cid = container._id

            resource_spec.container_id = cid
            # Write resource.txt again to update the contaienr id.
            with open(config_dir / 'resource.txt', 'w') as f:
                resource_spec.write_to_file(f)
                for dev_name, device_alloc in resource_spec.allocations.items():
                    computer_ctx = self.computers[dev_name]
                    kvpairs = \
                        await computer_ctx.klass.generate_resource_data(device_alloc)
                    for k, v in kvpairs.items():
                        f.write(f'{k}={v}\n')

            stat_sync_state = StatSyncState(kernel_id)
            self.stat_sync_states[cid] = stat_sync_state
            async with spawn_stat_synchronizer(self.config['_src'],
                                               self.stat_sync_sockpath,
                                               self.stat_ctx.mode, cid,
                                               self.stat_ctx.log_endpoint) as proc:
                stat_sync_state.sync_proc = proc
                await container.start()

            # Get attached devices information (including model_name).
            attached_devices = {}
            for dev_name, device_alloc in resource_spec.allocations.items():
                computer_set = self.computers[dev_name]
                devices = await computer_set.klass.get_attached_devices(device_alloc)
                attached_devices[dev_name] = devices
        except asyncio.CancelledError:
            raise
        except Exception:
            # Oops, we have to restore the allocated resources!
            if (sys.platform.startswith('linux') and
                self.config['container']['scratch-type'] == 'memory'):
                await destroy_scratch_filesystem(scratch_dir)
                await destroy_scratch_filesystem(tmp_dir)
                shutil.rmtree(tmp_dir)
            shutil.rmtree(scratch_dir)
            self.port_pool.update(host_ports)
            for dev_name, device_alloc in resource_spec.allocations.items():
                self.computers[dev_name].alloc_map.free(device_alloc)
            raise

        ctnr_host_port_map: MutableMapping[int, int] = {}
        stdin_port = 0
        stdout_port = 0
        for idx, port in enumerate(exposed_ports):
            host_port = int((await container.port(port))[0]['HostPort'])
            assert host_port == host_ports[idx]
            if port == 2000:     # intrinsic
                repl_in_port = host_port
            elif port == 2001:   # intrinsic
                repl_out_port = host_port
            elif port == 2002:   # legacy
                stdin_port = host_port
            elif port == 2003:   # legacy
                stdout_port = host_port
            else:
                ctnr_host_port_map[port] = host_port
        for sport in service_ports:
            sport['host_ports'] = tuple(
                ctnr_host_port_map[cport] for cport in sport['container_ports']
            )

        kernel_obj = await DockerKernel.new(
            kernel_id,
            image_ref,
            version,
            agent_config=self.config,
            service_ports=service_ports,
            resource_spec=resource_spec,
            data={
                'container_id': container._id,
                'kernel_host': kernel_host,
                'repl_in_port': repl_in_port,
                'repl_out_port': repl_out_port,
                'stdin_port': stdin_port,    # legacy
                'stdout_port': stdout_port,  # legacy
                'host_ports': host_ports,
                'domain_socket_proxies': domain_socket_proxies,
                'block_service_ports': internal_data.get('block_service_ports', False)
            })
        self.kernel_registry[kernel_id] = kernel_obj
        log.debug('kernel repl-in address: {0}:{1}', kernel_host, repl_in_port)
        log.debug('kernel repl-out address: {0}:{1}', kernel_host, repl_out_port)
        for service_port in service_ports:
            log.debug('service port: {!r}', service_port)

        live_services = await kernel_obj.get_service_apps()
        if live_services['status'] != 'failed':
            for live_service in live_services['data']:
                for service_port in service_ports:
                    if live_service['name'] == service_port['name']:
                        service_port.update(live_service)
                        break

        # Finally we are done.
        await self.produce_event('kernel_started', str(kernel_id))

        # Execute the startup command if the session type is batch.
        if SessionTypes(kernel_config['session_type']) == SessionTypes.BATCH:
            log.debug('startup command: {!r}',
                      (kernel_config['startup_command'] or '')[:60])

            # TODO: make this working after agent restarts
            async def execute_batch():
                opts = {
                    'exec': kernel_config['startup_command'],
                }
                while True:
                    try:
                        result = await self.execute(
                            kernel_id,
                            'batch-job', 'batch', '',
                            opts=opts,
                            flush_timeout=1.0,
                            api_version=3)
                    except KeyError:
                        await self.produce_event(
                            'kernel_terminated',
                            str(kernel_id), 'self-terminated',
                            None)
                        break

                    if result['status'] == 'finished':
                        if result['exitCode'] == 0:
                            await self.produce_event(
                                'kernel_success',
                                str(kernel_id), 0)
                        else:
                            await self.produce_event(
                                'kernel_failure',
                                str(kernel_id), result['exitCode'])
                        break
                    if result['status'] == 'exec-timeout':
                        await self.produce_event(
                            'kernel_failure', str(kernel_id), -2)
                        break
                # TODO: store last_stat?
                await self.destroy_kernel(kernel_id, 'task-finished')

            self.loop.create_task(execute_batch())

        return {
            'id': str(kernel_id),  # type: ignore  # to make it msgpack-serializable
            'kernel_host': str(kernel_host),
            'repl_in_port': repl_in_port,
            'repl_out_port': repl_out_port,
            'stdin_port': stdin_port,    # legacy
            'stdout_port': stdout_port,  # legacy
            'service_ports': service_ports,
            'container_id': container._id,
            'resource_spec': resource_spec.to_json_serializable_dict(),
            'attached_devices': attached_devices,
        }

    async def destroy_kernel(self, kernel_id: KernelId, reason: str) \
            -> Optional[Mapping[MetricKey, MetricValue]]:
        try:
            kernel_obj = self.kernel_registry[kernel_id]
            cid = kernel_obj['container_id']
            kernel_obj.termination_reason = reason
        except KeyError:
            log.warning('destroy_kernel(k:{0}) kernel missing (already dead?)',
                        kernel_id)

            async def force_cleanup():
                await self.clean_kernel(kernel_id)
                await self.produce_event('kernel_terminated',
                                         str(kernel_id), reason,
                                         None)

            self.orphan_tasks.discard(asyncio.Task.current_task())
            await asyncio.shield(force_cleanup())
            return None

        container = self.docker.containers.container(cid)
        if kernel_obj.runner is not None:
            await kernel_obj.runner.close()
        try:
            await container.kill()
            # Collect the last-moment statistics.
            if cid in self.stat_sync_states:
                s = self.stat_sync_states[cid]
                try:
                    with timeout(5):
                        await s.terminated.wait()
                        if s.sync_proc is not None:
                            await s.sync_proc.wait()
                            s.sync_proc = None
                except ProcessLookupError:
                    pass
                except asyncio.TimeoutError:
                    log.warning('stat-collector shutdown sync timeout.')
                last_stat: MutableMapping[MetricKey, MetricValue] = {
                    key: metric.to_serializable_dict()
                    for key, metric in s.last_stat.items()
                }
                last_stat['version'] = 2  # type: ignore
                return last_stat
        except DockerError as e:
            if e.status == 409 and 'is not running' in e.message:
                # already dead
                log.warning('destroy_kernel(k:{0}) already dead', kernel_id)
                kernel_obj.release_slots(self.computers)
                await kernel_obj.close()
                self.kernel_registry.pop(kernel_id, None)
            elif e.status == 404:
                # missing
                log.warning('destroy_kernel(k:{0}) kernel missing, '
                            'forgetting this kernel', kernel_id)
                kernel_obj.release_slots(self.computers)
                await kernel_obj.close()
                self.kernel_registry.pop(kernel_id, None)
            else:
                log.exception('destroy_kernel(k:{0}) kill error', kernel_id)
                self.error_monitor.capture_exception()
        except asyncio.CancelledError:
            log.exception('destroy_kernel(k:{0}) operation cancelled', kernel_id)
            raise
        except Exception:
            log.exception('destroy_kernel(k:{0}) unexpected error', kernel_id)
            self.error_monitor.capture_exception()
        finally:
            self.orphan_tasks.discard(asyncio.Task.current_task())
        # The container will be deleted in the docker monitoring coroutine.
        return None

    async def clean_kernel(self, kernel_id: KernelId, exit_code: int = 255):
        try:
            kernel_obj = self.kernel_registry[kernel_id]
            found = True
        except KeyError:
            found = False
        try:
            if found:
                await self.produce_event(
                    'kernel_terminated', str(kernel_id),
                    kernel_obj.termination_reason or 'self-terminated',
                    exit_code)
                container_id = kernel_obj['container_id']
                container = self.docker.containers.container(container_id)
                if kernel_obj.runner is not None:
                    await kernel_obj.runner.close()
                stat_sync_state = self.stat_sync_states.pop(container_id, None)
                if stat_sync_state:
                    sync_proc = stat_sync_state.sync_proc
                    try:
                        if sync_proc is not None:
                            sync_proc.terminate()
                            try:
                                with timeout(2.0):
                                    await sync_proc.wait()
                            except asyncio.TimeoutError:
                                sync_proc.kill()
                                await sync_proc.wait()
                    except ProcessLookupError:
                        pass

                for domain_socket_proxy in kernel_obj.get('domain_socket_proxies', []):
                    domain_socket_proxy.proxy_server.close()
                    await domain_socket_proxy.proxy_server.wait_closed()
                    try:
                        domain_socket_proxy.host_proxy_path.unlink()
                    except IOError:
                        pass

                # When the agent restarts with a different port range, existing
                # containers' host ports may not belong to the new port range.
                if not self.config['debug']['skip-container-deletion']:
                    try:
                        with timeout(20):
                            await container.delete()
                    except DockerError as e:
                        if e.status == 409 and 'already in progress' in e.message:
                            pass
                        elif e.status == 404:
                            pass
                        else:
                            log.exception(
                                'unexpected docker error while deleting container (k:{}, c:{})',
                                kernel_id, container_id)
                    except asyncio.TimeoutError:
                        log.warning('container deletion timeout (k:{}, c:{})',
                                    kernel_id, container_id)
                    finally:
                        port_range = self.config['container']['port-range']
                        restored_ports = [*filter(
                            lambda p: port_range[0] <= p <= port_range[1],
                            kernel_obj['host_ports'])]
                        self.port_pool.update(restored_ports)

            if kernel_id in self.restarting_kernels:
                self.restarting_kernels[kernel_id].destroy_event.set()

            if found:
                scratch_root = self.config['container']['scratch-root']
                scratch_dir = scratch_root / str(kernel_id)
                tmp_dir = scratch_root / f'{kernel_id}_tmp'
                try:
                    if (sys.platform.startswith('linux') and
                        self.config['container']['scratch-type'] == 'memory'):
                        await destroy_scratch_filesystem(scratch_dir)
                        await destroy_scratch_filesystem(tmp_dir)
                        shutil.rmtree(tmp_dir)
                    shutil.rmtree(scratch_dir)
                except FileNotFoundError:
                    pass
                kernel_obj.release_slots(self.computers)
                await kernel_obj.close()
                self.kernel_registry.pop(kernel_id, None)
        except Exception:
            log.exception('unexpected error while cleaning up kernel (k:{})', kernel_id)
        finally:
            self.orphan_tasks.discard(asyncio.Task.current_task())
            if kernel_id in self.blocking_cleans:
                self.blocking_cleans[kernel_id].set()

    async def fetch_docker_events(self):
        while True:
            try:
                await self.docker.events.run()
            except asyncio.TimeoutError:
                # The API HTTP connection may terminate after some timeout
                # (e.g., 5 minutes)
                log.info('restarting docker.events.run()')
                continue
            except aiohttp.ClientError as e:
                log.warning('restarting docker.events.run() due to {0!r}', e)
                continue
            except asyncio.CancelledError:
                break
            except Exception:
                log.exception('unexpected error')
                self.error_monitor.capture_exception()
                break

    async def handle_docker_events(self):
        subscriber = self.docker.events.subscribe()
        last_footprint = None
        while True:
            try:
                evdata = await subscriber.get()
            except asyncio.CancelledError:
                break
            if evdata is None:
                # fetch_docker_events() will automatically reconnect.
                continue

            # FIXME: Sometimes(?) duplicate event data is received.
            # Just ignore the duplicate ones.
            new_footprint = (
                evdata['Type'],
                evdata['Action'],
                evdata['Actor']['ID'],
            )
            if new_footprint == last_footprint:
                continue
            last_footprint = new_footprint

            if self.config['debug']['log-docker-events']:
                log.debug('docker-event: raw: {}', evdata)

            if evdata['Action'] == 'die':
                # When containers die, we immediately clean up them.
                container_name = evdata['Actor']['Attributes']['name']
                kernel_id = await get_kernel_id_from_container(container_name)
                if kernel_id is None:
                    continue
                try:
                    exit_code = evdata['Actor']['Attributes']['exitCode']
                except KeyError:
                    exit_code = 255
                self.orphan_tasks.add(
                    self.loop.create_task(self.clean_kernel(kernel_id, exit_code))
                )

        await asyncio.sleep(0.5)
