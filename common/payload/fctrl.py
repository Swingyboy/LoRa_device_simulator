from __future__ import annotations
import ctypes
import typing
from dataclasses import dataclass

c_uint8 = ctypes.c_uint8


class _FctrlUpBits(ctypes.BigEndianStructure):
    _fields_ = [
        ("adr", c_uint8, 1),
        ("adr_ack_req", c_uint8, 1),
        ("ack", c_uint8, 1),
        ("class_b", c_uint8, 1),
        ("fopts_len", c_uint8, 4)
    ]


class _FctrlDownBits(ctypes.BigEndianStructure):
    _fields_ = [
        ("adr", c_uint8, 1),
        ("rfu", c_uint8, 1),
        ("ack", c_uint8, 1),
        ("fpending", c_uint8, 1),
        ("fopts_len", c_uint8, 4)
    ]


class _FctrlUp:

    def __init__(self, adr=0, adr_ack_req=0, ack=0, class_b=0, fopts_len=0):
        self.__bits = _FctrlUpBits()
        self.__bits.adr = adr
        self.__bits.adr_ack_req = adr_ack_req
        self.__bits.ack = ack
        self.__bits.class_b = class_b
        self.__bits.fopts_len = fopts_len

    @property
    def adr(self):
        return self.__bits.adr

    @adr.setter
    def adr(self, value: int):
        if not isinstance(value, int):
            raise ValueError("ADR param should a bit/int instance.")
        if (value < 0x0) or (value > 0x1):
            raise ValueError("ADR param should be in range from 0x0 to  0x1.")
        self.__bits.adr = value

    @property
    def adr_ack_req(self):
        return self.__bits.adr_ack_req

    @adr_ack_req.setter
    def adr_ack_req(self, value):
        if not isinstance(value, int):
            raise ValueError("ADR_ACK_REQ param should a bit/int instance.")
        if (value < 0x0) or (value > 0x1):
            raise ValueError("ADR_ACK param should be in range from 0x0 to  0x1.")
        self.__bits.adr_ack_req = value

    @property
    def ack(self):
        return self.__bits.ack

    @ack.setter
    def ack(self, value):
        if not isinstance(value, int):
            raise ValueError("ACK param should a bit/int instance.")
        if (value < 0x0) or (value > 0x1):
            raise ValueError("ACK param should be in range from 0x0 to  0x1.")
        self.__bits.ack = value

    @property
    def class_b(self):
        return self.__bits.class_b

    @class_b.setter
    def class_b(self, value):
        if not isinstance(value, int):
            raise ValueError("CLASS B param should a bit/int instance.")
        if (value < 0x0) or (value > 0x1):
            raise ValueError("CLASS B param should be in range from 0x0 to  0x1.")
        self.__bits.class_b = value

    @property
    def fopts_len(self):
        return self.__bits.fopts_len

    @class_b.setter
    def fopts_len(self, value):
        if not isinstance(value, int):
            raise ValueError("FOPTS LEN param should a bit/int instance.")
        if (value < 0x0) or (value > 0xf):
            raise ValueError("FOPTS LEN param should be in range from 0x0 to  0xf.")
        self.__bits.class_b = value

    def to_bytes(self):
        return bytes(self.__bits)

    @classmethod
    def from_bits(cls, bits: int) -> FCtrlUp:
        return cls(
            adr=(bits >> 7) & 1,
            adr_ack_req=(bits >> 6) & 1,
            ack=(bits >> 5) & 1,
            class_b=(bits >> 4) & 1,
            fopts_len=(bits & 0xf)
        )


class _FctrlDown:
    def __init__(self, adr=0, ack=0, fpending=0, fopts_len=0):
        self.__bits = _FctrlDownBits()
        self.__bits.adr = adr
        self.__bits.ack = ack
        self.__bits.fpending = fpending
        self.__bits.fopts_len = fopts_len

    @property
    def adr(self):
        return self.__bits.adr

    @adr.setter
    def adr(self, value: int):
        if not isinstance(value, int):
            raise ValueError("ADR param should a bit/int instance.")
        if (value < 0x0) or (value > 0x1):
            raise ValueError("ADR param should be in range from 0x0 to  0x1.")
        self.__bits.adr = value

    @property
    def ack(self):
        return self.__bits.ack

    @ack.setter
    def ack(self, value:int):
        if not isinstance(value, int):
            raise ValueError("ACK param should a bit/int instance.")
        if (value < 0x0) or (value > 0x1):
            raise ValueError("ACK param should be in range from 0x0 to  0x1.")
        self.__bits.ack = value

    @property
    def fpending(self):
        return self.__bits.fpending

    @fpending.setter
    def fpending(self, value: int):
        if not isinstance(value, int):
            raise ValueError("FPENDING param should a bit/int instance.")
        if (value < 0x0) or (value > 0x1):
            raise ValueError("FPENDING param should be in range from 0x0 to  0x1.")
        self.__bits.fpending = value

    @property
    def fopts_len(self):
        return self.__bits.fopts_len

    @fopts_len.setter
    def fopts_len(self, value):
        if not isinstance(value, int):
            raise ValueError("FOPTS LEN param should a bit/int instance.")
        if (value < 0x0) or (value > 0xf):
            raise ValueError("FOPTS LEN param should be in range from 0x0 to  0xf.")
        self.__bits.class_b = value

    def to_bytes(self):
        return bytes(self.__bits)

    @classmethod
    def from_bits(cls, bits: int) -> FCtrlUp:
        return cls(
            adr=(bits >> 7) & 1,
            adr_ack_req=(bits >> 6) & 1,
            ack=(bits >> 5) & 1,
            class_b=(bits >> 4) & 1,
            fopts_len=(bits & 0xf)
        )


class Fctrl:
    @classmethod
    def from_fields(cls, fields: dict, uplink: bool) -> typing.Union[_FctrlDown, _FctrlUp]:
        if uplink:
            return _FctrlUp(**fields)
        else:
            return _FctrlDown(**fields)

    @classmethod
    def from_bits(cls, bits: int, uplink: bool) -> typing.Union[_FctrlDown, _FctrlUp]:
        if uplink:
            return _FctrlUp.from_bits(bits)
        else:
            return _FctrlDown.from_bits(bits)
