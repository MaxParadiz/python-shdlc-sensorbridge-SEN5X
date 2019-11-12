# -*- coding: utf-8 -*-
# (c) Copyright 2019 Sensirion AG, Switzerland

##############################################################################
##############################################################################
#                 _____         _    _ _______ _____ ____  _   _
#                / ____|   /\  | |  | |__   __|_   _/ __ \| \ | |
#               | |       /  \ | |  | |  | |    | || |  | |  \| |
#               | |      / /\ \| |  | |  | |    | || |  | | . ` |
#               | |____ / ____ \ |__| |  | |   _| || |__| | |\  |
#                \_____/_/    \_\____/   |_|  |_____\____/|_| \_|
#
#     THIS FILE IS AUTOMATICALLY GENERATED AND MUST NOT BE EDITED MANUALLY!
#
# Generator:    sensirion-shdlc-interface-generator 0.4.0
# Product:      Sensor Bridge
# Version:      0.1.0
#
##############################################################################
##############################################################################

# flake8: noqa

from __future__ import absolute_import, division, print_function
from sensirion_shdlc_driver.command import ShdlcCommand
from struct import pack, unpack

import logging
log = logging.getLogger(__name__)


class SensorBridgeCmdFirmwareUpdateBase(ShdlcCommand):
    """
    SHDLC command 0xF3: "Firmware Update".
    """

    def __init__(self, *args, **kwargs):
        super(SensorBridgeCmdFirmwareUpdateBase, self).__init__(
            0xF3, *args, **kwargs)


class SensorBridgeCmdEnterBootloader(SensorBridgeCmdFirmwareUpdateBase):

    def __init__(self):
        """
        Enter Bootloader Command

        Command to enter into the bootloader mode. The device will reboot into
        bootloader mode and wait until the new Firmware is received (start
        update command expected). Even after a power reset, the device returns
        into bootloader mode. The response frame is sent before the reset.

        .. note:: After the response frame is received, the device will not
                  accept new commands until fully booted (wait at least 1 s).
        """
        super(SensorBridgeCmdEnterBootloader, self).__init__(
            data=[],
            max_response_time=0.5,
            post_processing_time=1.0,
            min_response_length=0,
            max_response_length=0
        )


class SensorBridgeCmdStartUpdate(SensorBridgeCmdFirmwareUpdateBase):

    def __init__(self):
        """
        Start Update Command

        Command to start the firmware update. The devices flash will be erased
        (except bootloader) and the internal pointers resetted. The device is
        then ready to receive the new firmware with the update data command.

        .. note:: Only supported when in bootloader mode.
        """
        super(SensorBridgeCmdStartUpdate, self).__init__(
            data=[0x01],
            max_response_time=0.5,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=0
        )


class SensorBridgeCmdUpdateData(SensorBridgeCmdFirmwareUpdateBase):

    def __init__(self, data):
        """
        Update Data Command

        Command to send the new firmware data as hex code in binary format.

        .. note:: Only supported when in bootloader mode after receiving the
                  start update command. Send even number of bytes except for
                  the last frame.

        :param bytearray data:
            Firmware hex data in binary format.
        """
        super(SensorBridgeCmdUpdateData, self).__init__(
            data=b"".join([bytes(bytearray([0x02])),
                           bytes(bytearray(data))]),
            max_response_time=0.5,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=0
        )


class SensorBridgeCmdStopUpdate(SensorBridgeCmdFirmwareUpdateBase):

    def __init__(self, checksum):
        """
        Stop Update Command

        After all update data frames are sent, the stop update marks the end of
        the update sequence. The checksum is sent to the device and
        verification is done. The device state represents the success of the
        update sequence. If successfully, the device writes the signature and
        reboots into the application.

        .. note:: The checksum is calculated the same way as the SHDLC
                  checksum. First sum all firmware update data bytes and then
                  take the LSB of the result and invert it. This will be the
                  checksum.

        :param int checksum:
            Checksum of the firmware data.
        """
        super(SensorBridgeCmdStopUpdate, self).__init__(
            data=b"".join([bytes(bytearray([0x03])),
                           pack(">1B", checksum)]),
            max_response_time=1.0,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=0
        )
