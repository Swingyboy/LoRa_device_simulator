import ctypes

from fctrl import Fctrl



class Fhdr(ctypes.BigEndianStructure):
    _fields_ = [
        ("dev_addr", c_uint32, 32),
        ("fcnt", c_uint16, 16)
    ]
