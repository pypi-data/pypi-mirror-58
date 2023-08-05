#  Copyright (c) 2019 ETH Zurich, SIS ID and HVL D-ITET
#
"""
Communication protocol for LabJack using the LJM Library.
Originally developed and tested for LabJack T7-PRO.

Makes use of the LabJack LJM Library Python wrapper.
This wrapper needs an installation of the LJM Library for Windows, Mac OS X or Linux.
Go to:
https://labjack.com/support/software/installers/ljm
and
https://labjack.com/support/software/examples/ljm/python
"""

import logging
from typing import Union, Sequence, Tuple

from labjack import ljm

from .base import CommunicationProtocol
from .._dev import labjack
from ..configuration import configdataclass
from ..utils.enum import AutoNumberNameEnum


class LJMCommunicationError(Exception):
    """
    Errors coming from LJMCommunication.
    """

    pass


@configdataclass
class LJMCommunicationConfig:
    """
    Configuration dataclass for :class:`LJMCommunication`.
    """

    DeviceType = labjack.DeviceType

    #: Can be either string 'ANY', 'T7_PRO', 'T7', 'T4', or of enum :class:`DeviceType`.
    device_type: Union[str, labjack.DeviceType] = "ANY"

    class ConnectionType(AutoNumberNameEnum):
        """
        LabJack connection type.
        """

        ANY = ()
        USB = ()
        TCP = ()
        ETHERNET = ()
        WIFI = ()

    #: Can be either string or of enum :class:`ConnectionType`.
    connection_type: Union[str, ConnectionType] = "ANY"

    identifier: str = "ANY"
    """
    The identifier specifies information for the connection to be used. This can
    be an IP address, serial number, or device name. See the LabJack docs (
    https://labjack.com/support/software/api/ljm/function-reference/ljmopens/\
identifier-parameter) for more information.
    """

    def clean_values(self) -> None:
        """
        Performs value checks on device_type and connection_type.
        """
        if not isinstance(self.device_type, self.DeviceType):
            self.force_value(  # type: ignore
                "device_type", self.DeviceType(self.device_type)
            )

        if not isinstance(self.connection_type, self.ConnectionType):
            self.force_value(  # type: ignore
                "connection_type", self.ConnectionType(self.connection_type)
            )


class LJMCommunication(CommunicationProtocol):
    """
    Communication protocol implementing the LabJack LJM Library Python wrapper.
    """

    def __init__(self, configuration) -> None:
        """
        Constructor for LJMCommunication.
        """
        super().__init__(configuration)

        # reference to the ctypes handle
        self._handle = None

        self.logger = logging.getLogger(__name__)

    @staticmethod
    def config_cls():
        return LJMCommunicationConfig

    def open(self) -> None:
        """
        Open the communication port.
        """

        self.logger.info("Open connection")

        # open connection and store handle
        # may throw 1227 LJME_DEVICE_NOT_FOUND if device is not found
        try:
            with self.access_lock:
                self._handle = ljm.openS(
                    self.config.device_type.type_str,
                    str(self.config.connection_type),
                    str(self.config.identifier),
                )
        except ljm.LJMError as e:
            self.logger.error(e)
            # only catch "1229 LJME_DEVICE_ALREADY_OPEN", never observed
            if e.errorCode != 1229:
                raise LJMCommunicationError from e

    def close(self) -> None:
        """
        Close the communication port.
        """

        self.logger.info("Closing connection")

        try:
            with self.access_lock:
                ljm.close(self._handle)
        except ljm.LJMError as e:
            self.logger.error(e)
            # only catch "1224 LJME_DEVICE_NOT_OPEN", thrown on invalid handle
            if e.errorCode != 1224:
                raise LJMCommunicationError from e
        self._handle = None

    @property
    def is_open(self) -> bool:
        """
        Flag indicating if the communication port is open.

        :return: `True` if the port is open, otherwise `False`
        """
        # getHandleInfo does not work with LJM DEMO_MODE - consider it always opened
        # if only set
        if str(self._handle) == labjack.constants.DEMO_MODE:
            return True

        try:
            ljm.getHandleInfo(self._handle)
        except ljm.LJMError as e:
            if e.errorCode == 1224:  # "1224 LJME_DEVICE_NOT_OPEN"
                return False
            raise LJMCommunicationError from e
        return True

    def __del__(self) -> None:
        """
        Finalizer, closes port
        """

        self.close()

    def read_name(self, *names: str) -> Union[str, Tuple[str, ...]]:
        """
        Read one or more inputs by name.

        :param names: one or more names to read out from the LabJack
        :return: answer of the LabJack, either single answer or multiple answers in a
            tuple
        """

        # Errors that can be returned here:
        # 1224 LJME_DEVICE_NOT_OPEN if the device is not open
        # 1239 LJME_DEVICE_RECONNECT_FAILED if the device was opened, but connection
        #   lost

        with self.access_lock:
            try:
                if len(names) == 1:
                    ret = str(ljm.eReadName(self._handle, names[0]))
                else:
                    ret = tuple(  # type: ignore
                        str(read_name)
                        for read_name in ljm.eReadNames(self._handle, len(names), names)
                    )
            except ljm.LJMError as e:
                self.logger.error(e)
                raise LJMCommunicationError from e

        return ret

    def write_name(
        self, name: Union[Sequence[str], str], value: Union[Sequence[object], object]
    ) -> None:
        """
        Write one value to a named output.

        :param name: String or with name of LabJack IO
        :param value: is the value to write to the named IO port
        """

        with self.access_lock:
            try:
                ljm.eWriteName(self._handle, name, value)
            except ljm.LJMError as e:
                self.logger.error(e)
                raise LJMCommunicationError from e

    def write_names(self, names: Sequence[str], values: Sequence[object]) -> None:
        """
        Write more than one value at once to named outputs.

        :param names: is a sequence of strings with names of LabJack IO
        :param values: is a sequence of values corresponding to the list of names
        """

        with self.access_lock:
            try:
                ljm.eWriteNames(self._handle, len(names), names, values)
            except ljm.LJMError as e:
                self.logger.error(e)
                raise LJMCommunicationError from e

    def write_address(
        self, address: Union[Sequence[int], int], value: Union[Sequence[object], object]
    ) -> None:
        """
        **NOT IMPLEMENTED.**
        Write one or more values to Modbus addresses.

        :param address: One or more Modbus address on the LabJack.
        :param value: One or more values to be written to the addresses.
        """

        raise NotImplementedError
        # TODO: Implement function to write on addresses. Problem so far: I also need
        #  to bring in the data types (INT32, FLOAT32...)
