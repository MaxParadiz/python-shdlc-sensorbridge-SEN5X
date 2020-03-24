# -*- coding: utf-8 -*-
# (c) Copyright 2020 Sensirion AG, Switzerland

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
# Generator:    sensirion-shdlc-interface-generator 0.5.1
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


class SensorBridgeCmdPortVoltageOnOffBase(ShdlcCommand):
    """
    SHDLC command 0x01: "Port Voltage On Off".
    """

    def __init__(self, *args, **kwargs):
        super(SensorBridgeCmdPortVoltageOnOffBase, self).__init__(
            0x01, *args, **kwargs)


class SensorBridgeCmdPortVoltageOnOff(SensorBridgeCmdPortVoltageOnOffBase):

    def __init__(self, port, state):
        """
        Port Voltage On Off Command

        Switches a port supply on or off. If switched on, the previously set
        voltage will be applied.

        :param int port:
            The port(s) to switch on or off:

            -  0x00: Port 1
            -  0x01: Port 2
            -  0xFF: All ports
        :param int state:
            The new state to set:

            -  0x00: off
            -  0x01: on
        """
        super(SensorBridgeCmdPortVoltageOnOff, self).__init__(
            data=b"".join([pack(">B", port),
                           pack(">B", state)]),
            max_response_time=0.05,
            post_processing_time=0.0,
            min_response_length=0,
            max_response_length=0
        )
