import asyncio
import logging
from glob import glob
import re
from typing import List, Optional
from collections import namedtuple

from opentrons.config import IS_ROBOT, IS_LINUX
from .mod_abc import AbstractModule
# Must import tempdeck and magdeck (and other modules going forward) so they
# actually create the subclasses
from . import update, tempdeck, magdeck, thermocycler  # noqa(W0611)

log = logging.getLogger(__name__)

ModuleAtPort = namedtuple('ModuleAtPort', ('port', 'name'))


class UnsupportedModuleError(Exception):
    pass


class AbsentModuleError(Exception):
    pass


# mypy isn’t quite expressive enough to handle what we’re doing here, which
# is get all the class objects that are subclasses of an abstract module
# (strike 1) and call a classmethod on them (strike 2) and actually store
# the class objects (strike 3). So, type: ignore
MODULE_TYPES = {cls.name(): cls
                for cls in AbstractModule.__subclasses__()}  # type: ignore

MODULE_PORT_REGEX = re.compile('|'.join(MODULE_TYPES.keys()), re.I)


async def build(
        port: str,
        which: str,
        simulating: bool,
        interrupt_callback) -> AbstractModule:
    return await MODULE_TYPES[which].build(
        port, interrupt_callback=interrupt_callback, simulating=simulating)


def get_module_at_port(port: str) -> Optional[ModuleAtPort]:
    """ Given a port, returns either a ModuleAtPort
        if it is a recognized module, or None if not recognized.
    """
    match = MODULE_PORT_REGEX.search(port)
    if match:
        name = match.group().lower()
        return ModuleAtPort(port=f'/dev/{port}', name=name)
    return None


def discover() -> List[ModuleAtPort]:
    """ Scan for connected modules and return list of
        tuples of serial ports and device names
    """
    if IS_ROBOT and IS_LINUX:
        devices = glob('/dev/ot_module*')
    else:
        devices = []

    discovered_modules = []

    for port in devices:
        match = MODULE_PORT_REGEX.search(port)
        if match:
            name = match.group().lower()
            if name not in MODULE_TYPES:
                log.warning("Unexpected module connected: {} on {}"
                            .format(name, port))
                continue
            discovered_modules.append(ModuleAtPort(port=port, name=name))
    log.debug('Discovered modules: {}'.format(discovered_modules))

    return discovered_modules


class UpdateError(RuntimeError):
    def __init__(self, msg):
        self.msg = msg


async def update_firmware(
        module: AbstractModule,
        firmware_file: str,
        loop: Optional[asyncio.AbstractEventLoop]) -> AbstractModule:
    """ Update a module.

    If the update succeeds, a Module instance will be returned.

    Otherwise, raises an UpdateError with the reason for the failure.
    """
    simulating = module.is_simulated
    cls = type(module)
    old_port = module.port
    flash_port = await module.prep_for_update()
    callback = module.interrupt_callback
    del module
    after_port, results = await update.upload_firmware(
        port=flash_port,
        firmware_file_path=firmware_file,
        upload_function=cls.bootloader(),
        loop=loop)
    await asyncio.sleep(1.0)
    new_port = after_port or old_port
    if not results[0]:
        log.debug(f'Bootloader reponse: {results[1]}')
        raise UpdateError(results[1])
    return await cls.build(
        port=new_port,
        interrupt_callback=callback,
        simulating=simulating)
