"""The entities for Honeywell's RAMSES II / Residential Network Protocol."""
import queue
import time
from typing import Any, List, Optional

from .command import Command
from .const import (
    COMMAND_EXPOSES_ZONE,
    COMMAND_LOOKUP,
    COMMAND_MAP,
    ALL_DEV_ID,
    CTL_DEV_ID,
    DEVICE_LOOKUP,
    DEVICE_MAP,
)
from .logger import _LOGGER


def dev_hex_to_id(device_hex: str, friendly_id=False) -> str:
    """Convert (say) '06368E' to '01:145038' (or 'CTL:145038')."""
    if not device_hex:
        return f"{'':9}" if friendly_id else "--:------"
    _tmp = int(device_hex, 16)
    dev_type = f"{(_tmp & 0xFC0000) >> 18:02d}"
    if friendly_id:
        dev_type = DEVICE_MAP.get(dev_type, f"{dev_type:<3}")
    return f"{dev_type}:{_tmp & 0x03FFFF:06d}"


def dev_id_to_hex(device_id: str) -> str:
    """Convert (say) '01:145038' (or 'CTL:145038') to '06368E'."""
    if len(device_id) == 9:  # e.g. '01:123456'
        dev_type = device_id[:2]
        dev_number = device_id[3:]
    else:  # len(device_id) == 10, e.g. 'CTL:123456', or ' 63:123456'
        dev_type = DEVICE_LOOKUP.get(device_id[:3], device_id[1:3])
        dev_number = device_id[4:]
    return f"{(int(dev_type) << 18) + int(dev_number):0>6X}"  # without preceeding 0x


class Entity:
    """The base class."""

    def __init__(self, entity_id, gateway) -> None:
        self._id = entity_id
        self._gateway = gateway
        self._queue = gateway.command_queue

        self._data = {}

    def update(self, payload, msg):
        value = {"_dtm": msg._pkt_dt, "_msg": msg}
        value.update(payload.get(self._id, {}) if payload else {})
        self._data.update({msg.command_code: value})

    def _get_value(self, code, key) -> Optional[Any]:
        if self._data.get(code):
            return self._data[code][key]


class Domain(Entity):
    """Base for the named Zones and the other domains (e.g. DHW).

    Domains include F8(rare), F9, FA, FC & FF."""

    def __init__(self, domain_id, gateway) -> None:
        # _LOGGER.debug("Creating a new Device %s", device_id)
        super().__init__(domain_id, gateway)

        gateway.domain_by_id.update({domain_id: self})
        gateway.domains.append(self)

        self._type = None
        self._discover()

    def _discover(self):
        pass

    @property
    def domain_id(self):
        return self._id

    @property
    def heat_demand(self):  # 3150
        return self._get_value("3150", "heat_demand")

    @property
    def relay_demand(self):  # 3150
        return self._get_value("0008", "relay_demand")

    @property
    def device_id(self) -> Optional[str]:  # TODO: delete me
        return self._id

    @property
    def parent_zone(self) -> Optional[str]:  # TODO: delete me
        return None


class System(Domain):
    """Base for the central heating (FC) domain."""

    def __init__(self, domain_id, gateway):
        # _LOGGER.debug("Creating a new System %s", CTL_DEV_ID)
        super().__init__(domain_id, gateway)

    def _discover(self):
        pass

    @property
    def setpoint_status(self):
        return {
            "mode": self._get_value("2E04", "mode"),
            "until": self._get_value("2E04", "until"),
        }

    @property
    def heat_demand(self):  # 3150
        return self._get_value("3150", "heat_demand")


class Device(Entity):
    """The Device class."""

    def __init__(self, device_id, gateway) -> None:
        # _LOGGER.debug("Creating a new Device %s", device_id)
        super().__init__(device_id, gateway)

        gateway.device_by_id.update({device_id: self})
        gateway.devices.append(self)

        self._type = DEVICE_MAP.get(device_id[:2])
        self._parent_zone = None
        self._parent_zzzz = None

        self._discover()

    def _discover(self):
        if self._type not in ["BDR", "STA", "TRV", " 12"]:
            try:
                self._queue.put_nowait(Command(self, "10E0", self._id, "00"))
            except queue.Full:
                pass

    @property
    def device_id(self) -> Optional[str]:
        return self._id

    @property
    def device_type(self) -> Optional[str]:
        return self._type

    @property
    def description(self):  # 0100, 10E0,
        return self._get_value("10E0)", "description")

    @property
    def parent_zzzz(self) -> Optional[str]:
        if self._parent_zzzz:
            return self._parent_zzzz  # once set, never changes

        for code in COMMAND_EXPOSES_ZONE:
            if self._data.get(code):
                self._parent_zzzz = self._data[code]["_msg"].raw_payload[:2]
                break

        return self._parent_zzzz

    @property
    def parent_zone(self) -> Optional[str]:  # 0004
        return self._parent_zone

    @parent_zone.setter
    def parent_zone(self, zone_idx) -> None:
        self._parent_zone = zone_idx


class Controller(Device):
    """The Controller class."""

    def __init__(self, device_id, gateway) -> None:
        # _LOGGER.debug("Creating a new Controller %s", device_id)
        super().__init__(device_id, gateway)

        self._discover()

    def update(self, entity_dict, msg):
        super().update(entity_dict, msg)

    def _discover(self):
        super()._discover()

        # WIP: try to discover fault codes
        for num in range(0, 15):
            try:
                self._queue.put_nowait(Command(self, "0418", CTL_DEV_ID, f"0000{num:02X}"))
            except queue.Full:
                pass

        return

        # # WIP: these are an attempt to actively discover the CTL rather than by eavesdropping
        # for cmd in ["313F"]:
        #     try:
        #         self._queue.put_nowait(Command(self, cmd, ALL_DEV_ID, "FF"))
        #     except queue.Full:
        #         pass

        # a 'real' Zone will return 0004/zone_name != None
        for zone_idx in range(12):
            _zone = f"{zone_idx:02x}00"
            try:
                self._queue.put_nowait(Command(self, "0004", CTL_DEV_ID, _zone))
            except queue.Full:
                pass

        # the 'real' DHW controller will return 1260/dhw_temp != None
        for _zone in ["FA"]:
            try:
                self._queue.put_nowait(Command(self, "1260", CTL_DEV_ID, _zone))
            except queue.Full:
                pass

        # # WIP: the Controller, and 'real' Relays will respond to 0016/rf_check - to device ID
        # try:
        #     self._queue.put_nowait(
        #         Command(self, "0016", CTL_DEV_ID, f"{domain_id}FF")
        #     )
        # except queue.Full:
        #     pass

    def handle_313f(self):
        """Controllers will RP to a RQ at anytime."""
        pass


class DhwSensor(Device):
    """The DHW class, such as a CS92."""

    def __init__(self, dhw_id, gateway) -> None:
        # _LOGGER.debug("Creating a new DHW %s", dhw_id)
        super().__init__(dhw_id, gateway)

        self._discover()

    def _discover(self):
        for cmd in ["10A0", "1260", "1F41"]:
            try:
                self._queue.put_nowait(Command(self, cmd, CTL_DEV_ID, "00"))
            except queue.Full:
                pass

    @property
    def battery(self):  # 1060
        return self._get_value("1060", "battery_level")
        # return self._get_value("1060", "low_battery")

    @property
    def temperature(self):  # 1260
        return self._get_value("1260", "temperature")


class Trv(Device):
    """The TRV class, such as a HR92."""
    # 045 RQ     TRV:056057 CTL:145038            313F 001 00
    # at ~4:00:00, gets RP from CTL

    def __init__(self, device_id, gateway) -> None:
        # _LOGGER.debug("Creating a new TRV %s", device_id)
        super().__init__(device_id, gateway)

    @property
    def battery(self):  # 1060
        return self._get_value("1060", "battery_level")
        # return self._get_value("1060", "low_battery")

    @property
    def configuration(self):  # 0100, 10E0,
        return self._get_value("0100", "language")

    @property
    def heat_demand(self):  # 3150
        return self._get_value("3150", "heat_demand")

    @property
    def setpoint(self):  # 2309
        return self._get_value("2309", "setpoint")

    @property
    def temperature(self):  # 30C9
        return self._get_value("30C9", "temperature")

    @property
    def window_state(self):  # 12B0
        return self._get_value("12B0", "window_open")


class Bdr(Device):
    """The BDR class, such as a BDR91."""

    def __init__(self, device_id, gateway) -> None:
        # _LOGGER.debug("Creating a new BDR %s", device_id)
        super().__init__(device_id, gateway)

    def _discover(self):
        super()._discover()

        for cmd in ["3B00", "3EF0"]:
            try:
                self._queue.put_nowait(Command(self, cmd, self._id, "00"))
            except queue.Full:
                pass

        for cmd in ["3EF1"]:
            try:
                self._queue.put_nowait(Command(self, cmd, self._id, "0000"))
            except queue.Full:
                pass


class Thermostat(Device):
    """The STA class, such as a TR87RF."""
    # 045  I     STA:092243            >broadcast 3120 007 0070B0000000FF
    # every ~3:45:00 (each STA different, but each keeps its interval to the second)
    # payload never changes

    def __init__(self, device_id, gateway) -> None:
        # _LOGGER.debug("Creating a new STA %s", device_id)
        super().__init__(device_id, gateway)

    @property
    def battery(self):  # 1060
        return self._get_value("1060", "battery_level")
        # return self._get_value("1060", "low_battery")

    @property
    def setpoint(self):  # 2309
        return self._get_value("2309", "setpoint")

    @property
    def temperature(self):  # 30C9
        return self._get_value("30C9", "temperature")


class Zone(Entity):
    """Base for the 12 named Zones."""

    def __init__(self, zone_idx, gateway) -> None:
        # _LOGGER.debug("Creating a new Zone %s", zone_idx)
        super().__init__(zone_idx, gateway)

        gateway.zone_by_id.update({zone_idx: self})
        gateway.zones.append(self)

        self._type = None
        self._discover()

    def _discover(self):
        for cmd in ["0004", "000A", "2349", "30C9"]:
            zone_idx = f"{self._id}00" if cmd == "0004" else self._id
            try:
                self._queue.put_nowait(Command(self, cmd, CTL_DEV_ID, zone_idx))
            except queue.Full:
                pass

    def update(self, payload, msg):
        super().update(payload, msg)

        # # cast a new type (which _is_ based upon the current type)
        # if isinstance(self, Zone):
        #     if self._data.get("12B0"):
        #         self.__class__ = RadValve
        #     if self._data.get("0008"):  # TODO:check
        #         self.__class__ = Electric

    @property
    def zone_idx(self):
        return self._id

    @property
    def name(self) -> Optional[str]:
        return self._get_value("0004", "name")

    @property
    def zone_type(self) -> Optional[str]:
        return self._type

    @zone_type.setter
    def zone_type(self, zone_type):
        zone_class = {
            "Electric Heat": Electric,
            "Radiator Valve": RadValve,
            "Underfloor Heating": Underfloor,
            "Zone Valve": ZoneValve,
        }.get(zone_type)
        if zone_class:
            self.__class__ = zone_class
        self._type = zone_type

    @property
    def configuration(self):
        # if self._type != "Radiator Valve":
        #     return {}

        attrs = ["local_override", "multi_room_mode", "openwindow_function"]
        if self._data.get("zone_config"):
            return {
                k: v
                for k, v in self._data["zone_config"]["flags"].items()
                if k in attrs
            }
        return {k: None for k in attrs}

    @property
    def setpoint_capabilities(self):
        return {
            "max_heat_setpoint": self._get_value("000A", "max_temp"),
            "min_heat_setpoint": self._get_value("000A", "min_temp"),
        }

    @property
    def setpoint_status(self):
        return {
            "setpoint": self._get_value("2349", "setpoint"),
            "mode": self._get_value("2349", "mode"),
            "until": self._get_value("2349", "until"),
        }

    @property
    def temperature(self):
        return self._get_value("30C9", "temperature")

    @property
    def heat_demand(self):
        zone_demand = 0.0
        for dev in [v for v in self._gateway.device_by_id.values() if v._type == "TRV"]:
            if dev.parent_zone == self._id:
                device_demand = dev.heat_demand if dev.heat_demand else 0
                zone_demand = max(zone_demand, device_demand)

        return zone_demand


class DhwZone(Zone):
    """Base for the DHW (Fx) domain."""

    def __init__(self, zone_idx, gateway) -> None:
        # _LOGGER.debug("Creating a new Zone %s", zone_idx)
        super().__init__(zone_idx, gateway)

        self._type = None
        self._discover()

    def _discover(self):
        for cmd in ["10A0", "1260", "1F41"]:  # TODO: what about 1100?
            try:
                self._queue.put_nowait(Command(self, cmd, CTL_DEV_ID, "00"))
            except queue.Full:
                pass

    @property
    def name(self) -> Optional[str]:
        return "DHW Controller"

    @property
    def configuration(self):
        return {
            "setpoint": self._get_value("10A0", "setpoint"),
            "overrun": self._get_value("10A0", "overrun"),
            "differential": self._get_value("10A0", "differential"),
        }

    @property
    def setpoint_status(self):
        return {
            "active": self._get_value("1F41", "active"),
            "mode": self._get_value("1F41", "mode"),
            "until": self._get_value("1F41", "until"),
        }

    @property
    def temperature(self):
        return self._get_value("1260", "temperature")


class RadValve(Zone):
    """Base for Radiator Valve zones.

    For radiators controlled by HR92s or HR80s (will also call for heat).
    """

    # 3150 (heat_demand) but no 0008 (relay_demand)

    def _discover(self):
        super()._discover()

        for cmd in ["12B0"]:
            try:
                self._queue.put_nowait(Command(self, cmd, CTL_DEV_ID, self._id))
            except queue.Full:
                pass

    @property
    def window_open(self):
        return self._get_value("12B0", "window_open")


class Electric(Zone):
    """Base for Electric Heat zones.

    For a small (5A) electric load controlled by a BDR91 (never calls for heat).
    """

    # 0004 (zone_name)
    # 0008 (relay_demand) but no 3150 (heat_demand)
    # 0009 (ch_failsafe)
    # 000A (zone_config)
    # 1FC9 (bind_device)
    # 2309 (setpoint)
    # 2349 (zone_mode)


class ZoneValve(Electric):
    """Base for Zone Valve zones.

    For a motorised valve controlled by a BDR91 (will also call for heat).
    """


class Underfloor(Zone):
    """Base for Underfloor Heating zones.

    For underfloor heating controlled by an HCE80 or HCC80 (will also call for heat).
    """


class MixValve(Zone):
    """Base for Mixing Valve zones.

    For a modulating valve controlled by a HM80 (will also call for heat).
    """


DEVICE_CLASSES = {
    DEVICE_LOOKUP["CTL"]: Controller,
    DEVICE_LOOKUP["TRV"]: Trv,
    DEVICE_LOOKUP["DHW"]: DhwSensor,
    DEVICE_LOOKUP["BDR"]: Bdr,
    DEVICE_LOOKUP["STA"]: Thermostat,
}

ZONE_CLASSES = {
    "01": Controller,
    "04": Trv,
    "07": DhwSensor,
    "13": Bdr,
    "34": Thermostat,
}
