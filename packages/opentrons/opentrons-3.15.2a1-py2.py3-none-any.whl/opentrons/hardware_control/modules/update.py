import asyncio
import logging
import os
import sys
from glob import glob
from typing import Any, Dict, Optional, Tuple

from .mod_abc import UploadFunction

log = logging.getLogger(__name__)

PORT_SEARCH_TIMEOUT = 5.5

# avrdude_options
PART_NO = 'atmega32u4'
PROGRAMMER_ID = 'avr109'
BAUDRATE = '57600'


async def enter_bootloader(driver, model):
    """
    Using the driver method, enter bootloader mode of the atmega32u4.
    The bootloader mode opens a new port on the uC to upload the hex file.
    After receiving a 'dfu' command, the firmware provides a 3-second window to
    close the current port so as to do a clean switch to the bootloader port.
    The new port shows up as 'ttyn_bootloader' on the pi; upload fw through it.
    NOTE: Modules with old bootloader will have the bootloader port show up as
    a regular module port- 'ttyn_tempdeck'/ 'ttyn_magdeck' with the port number
    being either different or same as the one that the module was originally on
    So we check for changes in ports and use the appropriate one
    """
    # Required for old bootloader
    ports_before_dfu_mode = await _discover_ports()

    if model == 'thermocycler':
        await driver.enter_programming_mode()
    else:
        driver.enter_programming_mode()

    driver.disconnect()
    new_port = ''
    try:
        new_port = await asyncio.wait_for(
            _port_poll(_has_old_bootloader(model), ports_before_dfu_mode),
            PORT_SEARCH_TIMEOUT)
    except asyncio.TimeoutError:
        pass
    return new_port


async def upload_firmware(port: str,
                          firmware_file_path: str,
                          upload_function: UploadFunction,
                          loop: Optional[asyncio.AbstractEventLoop])\
        -> Tuple[str, Tuple[bool, str]]:
    """
    Run firmware upload command. Switch back to normal module port

    Note: For modules with old bootloader, the kernel could assign the module
    a new port after the update (since the board is automatically reset).
    Scan for such a port change and use the appropriate port.

    Returns a tuple of the new port to communicate on (or empty string
    if it was not found) and a tuple of success and message from bootloader.
    """

    ports_before_update = await _discover_ports()

    kwargs: Dict[str, Any] = {
        'stdout': asyncio.subprocess.PIPE,
        'stderr': asyncio.subprocess.PIPE
    }
    if loop:
        kwargs['loop'] = loop

    res = await upload_function(port, firmware_file_path, kwargs)

    await asyncio.sleep(2)  # wait for com port to reappear
    new_port = await _port_on_mode_switch(ports_before_update)
    return new_port, res


async def upload_via_avrdude(port: str,
                             firmware_file_path: str,
                             kwargs: Dict[str, Any]) -> Tuple[bool, str]:
    config_file_path = os.path.join(
        os.path.dirname(sys.modules['opentrons'].__file__),
        'config', 'modules', 'avrdude.conf')
    proc = await asyncio.create_subprocess_exec(
        'avrdude', '-C{}'.format(config_file_path), '-v',
        '-p{}'.format(PART_NO),
        '-c{}'.format(PROGRAMMER_ID),
        '-P{}'.format(port),
        '-b{}'.format(BAUDRATE), '-D',
        '-Uflash:w:{}:i'.format(firmware_file_path),
        **kwargs)
    await proc.wait()

    _result = await proc.communicate()
    result = _result[1].decode()
    avrdude_res = _format_avrdude_response(result)
    if avrdude_res[0]:
        log.debug(result)
    else:
        log.error("Failed to update module firmware for {}: {}"
                  .format(port, avrdude_res[1]))
    return avrdude_res


def _format_avrdude_response(raw_response: str) -> Tuple[bool, str]:
    avrdude_log = ''
    for line in raw_response.splitlines():
        if 'avrdude:' in line and line != raw_response.splitlines()[1]:
            avrdude_log += line.lstrip('avrdude:') + '..'
            if 'flash verified' in line:
                return True, line.lstrip('avrdude: ')
    return False, avrdude_log


async def upload_via_bossa(port: str,
                           firmware_file_path: str,
                           kwargs: Dict[str, Any]) -> Tuple[bool, str]:
    # bossac -p/dev/ttyACM1 -e -w -v -R --offset=0x2000
    #   modules/thermo-cycler/production/firmware/thermo-cycler-arduino.ino.bin
    # NOTE: bossac cannot traverse symlinks to port,
    # so we resolve to real path
    resolved_symlink = os.path.realpath(port)
    log.info(
        f"device at symlinked port: {port}"
        f"resolved to path: {resolved_symlink}")
    bossa_args = ['bossac', f'-p{resolved_symlink}',
                  '-e', '-w', '-v', '-R',
                  '--offset=0x2000', f'{firmware_file_path}']

    proc = await asyncio.create_subprocess_exec(*bossa_args, **kwargs)
    stdout, stderr = await proc.communicate()
    res = stdout.decode()
    if "Verify successful" in res:
        log.debug(res)
        return True, res
    elif stderr:
        log.error(f"Failed to update module firmware for {port}: {res}")
        log.error(f"Error given: {stderr.decode()}")
        return False, res
    return False, ''


async def _port_on_mode_switch(ports_before_switch):
    ports_after_switch = await _discover_ports()
    new_port = ''
    if ports_after_switch and \
            len(ports_after_switch) >= len(ports_before_switch) and \
            not set(ports_before_switch) == set(ports_after_switch):
        new_ports = list(filter(
            lambda x: x not in ports_before_switch,
            ports_after_switch))
        if len(new_ports) > 1:
            raise OSError('Multiple new ports found on mode switch')
        new_port = new_ports[0]
    return new_port


async def _port_poll(is_old_bootloader, ports_before_switch=None):
    """
    Checks for the bootloader port
    """
    new_port = ''
    while not new_port:
        if is_old_bootloader:
            new_port = await _port_on_mode_switch(ports_before_switch)
        else:
            ports = await _discover_ports()
            if ports:
                discovered_ports = list(filter(
                    lambda x: 'bootloader' in x, ports))
                if len(discovered_ports) == 1:
                    new_port = discovered_ports[0]
                elif len(discovered_ports) > 1:
                    raise OSError('Multiple new bootloader ports'
                                  'found on mode switch')

        await asyncio.sleep(0.05)
    return new_port


def _has_old_bootloader(model: str) -> bool:
    return model in ('temp_deck_v1', 'temp_deck_v2')


async def _discover_ports():
    for attempt in range(2):
        # Measure for race condition where port is being switched in
        # between calls to isdir() and listdir()
        module_ports = glob('/dev/ot_module*')
        if module_ports:
            return module_ports
        await asyncio.sleep(2)
    raise Exception("No ot_modules found in /dev. Try again")
