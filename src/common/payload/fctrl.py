from __future__ import annotations
import typing


class _FctrlUp:

    def __init__(self):
        self.__adr = 0
        self.__adr_ack_req = 0
        self.__ack = 0
        self.__class_b = 0
        self.__fopts_len = 0

    @property
    def adr(self):
        return self.__adr

    @adr.setter
    def adr(self, value: int):
        if not isinstance(value, int):
            raise ValueError("ADR param should a bit/int instance.")
        if (value < 0x0) or (value > 0x1):
            raise ValueError("ADR param should be in range from 0x0 to  0x1.")
        self.__adr = value

    @property
    def adr_ack_req(self):
        return self.__adr_ack_req

    @adr_ack_req.setter
    def adr_ack_req(self, value):
        if not isinstance(value, int):
            raise ValueError("ADR_ACK_REQ param should a bit/int instance.")
        if (value < 0x0) or (value > 0x1):
            raise ValueError("ADR_ACK param should be in range from 0x0 to  0x1.")
        self.__adr_ack_req = value

    @property
    def ack(self):
        return self.__ack

    @ack.setter
    def ack(self, value):
        if not isinstance(value, int):
            raise ValueError("ACK param should a bit/int instance.")
        if (value < 0x0) or (value > 0x1):
            raise ValueError("ACK param should be in range from 0x0 to  0x1.")
        self.__ack = value

    @property
    def class_b(self):
        return self.__class_b

    @class_b.setter
    def class_b(self, value):
        if not isinstance(value, int):
            raise ValueError("CLASS B param should a bit/int instance.")
        if (value < 0x0) or (value > 0x1):
            raise ValueError("CLASS B param should be in range from 0x0 to  0x1.")
        self.__class_b = value

    @property
    def fopts_len(self):
        return self.__fopts_len

    @fopts_len.setter
    def fopts_len(self, value):
        if not isinstance(value, int):
            raise ValueError("FOPTS LEN param should a bit/int instance.")
        if (value < 0x0) or (value > 0xf):
            raise ValueError("FOPTS LEN param should be in range from 0x0 to  0xf.")
        self.__fopts_len = value

    def to_bytes(self):
        bytez = (self.adr << 7) | (self.adr_ack_req << 6) | (self.ack << 5) | (self.class_b << 4) | (self.fopts_len)
        return bytez.to_bytes(1, "big")

    @classmethod
    def from_bits(cls, bits: int) -> _FctrlUp:
        obj = cls()
        obj.adr=(bits >> 7) & 1
        obj.adr_ack_req=(bits >> 6) & 1
        obj.ack=(bits >> 5) & 1
        obj.class_b=(bits >> 4) & 1
        obj.fopts_len=(bits & 0xf)
        return obj

    @classmethod
    def from_fields(cls, fields: dict) -> _FctrlUp:
        obj = cls()
        obj.adr=fields.get("adr")
        obj.adr_ack_req=fields.get("adr_ack_req")
        obj.ack=fields.get("ack")
        obj.class_b=fields.get("class_b")
        obj.fopts_len=fields.get("fopts_len")
        return obj


class _FctrlDown:
    def __init__(self):
        self.__adr = 0
        self.__ack = 0
        self.__fpending = 0
        self.__fopts_len = 0

    @property
    def adr(self):
        return self.__adr

    @adr.setter
    def adr(self, value: int):
        if not isinstance(value, int):
            raise ValueError("ADR param should a bit/int instance.")
        if (value < 0x0) or (value > 0x1):
            raise ValueError("ADR param should be in range from 0x0 to  0x1.")
        self.__adr = value

    @property
    def ack(self):
        return self.__ack

    @ack.setter
    def ack(self, value: int):
        if not isinstance(value, int):
            raise ValueError("ACK param should a bit/int instance.")
        if (value < 0x0) or (value > 0x1):
            raise ValueError("ACK param should be in range from 0x0 to  0x1.")
        self.__ack = value

    @property
    def fpending(self):
        return self.__fpending

    @fpending.setter
    def fpending(self, value: int):
        if not isinstance(value, int):
            raise ValueError("FPENDING param should a bit/int instance.")
        if (value < 0x0) or (value > 0x1):
            raise ValueError("FPENDING param should be in range from 0x0 to  0x1.")
        self.__fpending = value

    @property
    def fopts_len(self):
        return self.__fopts_len

    @fopts_len.setter
    def fopts_len(self, value):
        if not isinstance(value, int):
            raise ValueError("FOPTS LEN param should a bit/int instance.")
        if (value < 0x0) or (value > 0xf):
            raise ValueError("FOPTS LEN param should be in range from 0x0 to  0xf.")
        self.__fopts_len = value

    def to_bytes(self):
        bytez = (self.adr << 7) | (self.ack << 5) | (self.fpending << 4) | (self.fopts_len)
        return bytez.to_bytes(1, "big")

    @classmethod
    def from_bits(cls, bits: int) -> _FctrlDown:
        obj = cls()
        obj.adr=(bits >> 7) & 1
        obj.ack=(bits >> 5) & 1
        obj.fpending=(bits >> 4) & 1
        obj.fopts_len=(bits & 0xf)
        return obj

    @classmethod
    def from_fields(cls, fields: dict) -> _FctrlDown:
        obj = cls()
        obj.adr=fields.get("adr")
        obj.adr_ack_req=fields.get("adr_ack_req")
        obj.fpending=fields.get("fpending")
        obj.fopts_len=fields.get("fopts_len")
        return obj


class Fctrl:
    @classmethod
    def from_fields(cls, fields: dict, uplink: bool) -> typing.Union[_FctrlDown, _FctrlUp]:
        if uplink:
            return _FctrlUp.from_fields(fields)
        else:
            return _FctrlDown(**fields)

    @classmethod
    def from_bits(cls, bits: int, uplink: bool) -> typing.Union[_FctrlDown, _FctrlUp]:
        if uplink:
            return _FctrlUp.from_bits(bits)
        else:
            return _FctrlDown.from_bits(bits)
