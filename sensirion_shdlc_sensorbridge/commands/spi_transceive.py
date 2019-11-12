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


class SensorBridgeCmdSpiTransceiveBase(ShdlcCommand):
    """
    SHDLC command 0x61: "Spi Transceive".
    """

    def __init__(self, *args, **kwargs):
        super(SensorBridgeCmdSpiTransceiveBase, self).__init__(
            0x61, *args, **kwargs)


class SensorBridgeCmdSpiTransceive(SensorBridgeCmdSpiTransceiveBase):

    def __init__(self, port, length, tx_data):
        """
        Spi Transceive Command

        Transceives an SPI frame on a certain port.

        :param int port:
            The port where the transceive should be executed:
            
            -  0x00: Port 1
            -  0x01: Port 2
        :param int length:
            Count of bytes to send. This amount of bytes has to be attached to
            the command.
        :param bytearray tx_data:
            Bytes to send.
        """
        super(SensorBridgeCmdSpiTransceive, self).__init__(
            data=b"".join([pack(">1B", port),
                           pack(">1I", length),
                           bytes(bytearray(tx_data))]),
            max_response_time=5.0,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=255
        )

    @staticmethod
    def interpret_response(data):
        """
        :return: Received bytes.
        :rtype: bytearray
        """
        rx_data = bytes(data[0:])  # bytes
        return rx_data
