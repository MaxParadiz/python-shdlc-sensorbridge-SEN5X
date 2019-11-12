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


class SensorBridgeCmdBlinkBase(ShdlcCommand):
    """
    SHDLC command 0x70: "Blink".
    """

    def __init__(self, *args, **kwargs):
        super(SensorBridgeCmdBlinkBase, self).__init__(
            0x70, *args, **kwargs)


class SensorBridgeCmdBlink(SensorBridgeCmdBlinkBase):

    def __init__(self, port):
        """
        Blink Command

        Let the LEDs on the device blink. Useful for example to identify the
        device on a bus.

        :param int port:
            The port(s) which should blink:
            
            -  0x00: Port 1
            -  0x01: Port 2
            -  0xFF: All ports
        """
        super(SensorBridgeCmdBlink, self).__init__(
            data=b"".join([pack(">1B", port)]),
            max_response_time=1.0,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=0
        )
