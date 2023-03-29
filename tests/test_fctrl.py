import unittest
from random import randint

from src.common.payload.fctrl import Fctrl

class TestFctr(unittest.TestCase):
    def test_fctrl_ul_from_bits_ff(self):
        bits = 0xFF
        fctrl = Fctrl.from_bits(bits=bits, uplink=True)
        self.assertEqual(fctrl.adr, 0x1)
        self.assertEqual(fctrl.adr_ack_req, 0x1)
        self.assertEqual(fctrl.ack, 0x1)
        self.assertEqual(fctrl.class_b, 0x1)
        self.assertEqual(fctrl.fopts_len, 0xf)

    def test_fctrl_ul_from_bits_00(self):
        bits = 0x00
        fctrl = Fctrl.from_bits(bits=bits, uplink=True)
        self.assertEqual(fctrl.adr, 0x0)
        self.assertEqual(fctrl.adr_ack_req, 0x0)
        self.assertEqual(fctrl.ack, 0x0)
        self.assertEqual(fctrl.class_b, 0x0)
        self.assertEqual(fctrl.fopts_len, 0x0)

    def test_fctrl_ul_from_bits_random(self):
        bits = randint(0x0, 0xff)
        fctrl = Fctrl.from_bits(bits=bits, uplink=True)
        self.assertEqual(fctrl.adr, (bits >> 7) & 1)
        self.assertEqual(fctrl.adr_ack_req,(bits >> 6) & 1)
        self.assertEqual(fctrl.ack, (bits >> 5) & 1)
        self.assertEqual(fctrl.class_b, (bits >> 4) & 1)
        self.assertEqual(fctrl.fopts_len, (bits & 0xf))

    def test_fctrl_ul_from_fields_ff(self):
        fields = {
            "adr": 0x1,
            "adr_ack_req": 0x1,
            "ack": 0x1,
            "class_b": 0x1,
            "fopts_len": 0xf
        }
        fctrl = Fctrl.from_fields(fields=fields, uplink=True)
        self.assertEqual(fctrl.adr, 0x1)
        self.assertEqual(fctrl.adr_ack_req, 0x1)
        self.assertEqual(fctrl.ack, 0x1)
        self.assertEqual(fctrl.class_b, 0x1)
        self.assertEqual(fctrl.fopts_len, 0xf)

    def test_fctrl_ul_from_fields_00(self):
        fields = {
            "adr": 0x0,
            "adr_ack_req": 0x0,
            "ack": 0x0,
            "class_b": 0x0,
            "fopts_len": 0x0
        }
        fctrl = Fctrl.from_fields(fields=fields, uplink=True)
        self.assertEqual(fctrl.adr, 0x0)
        self.assertEqual(fctrl.adr_ack_req, 0x0)
        self.assertEqual(fctrl.ack, 0x0)
        self.assertEqual(fctrl.class_b, 0x0)
        self.assertEqual(fctrl.fopts_len, 0x0)

    def test_fctrl_ul_from_fields_random(self):
        fields = {
            "adr": randint(0x0, 0x1),
            "adr_ack_req": randint(0x0, 0x1),
            "ack": randint(0x0, 0x1),
            "class_b": randint(0x0, 0x1),
            "fopts_len": randint(0x0, 0xf),
        }
        fctrl = Fctrl.from_fields(fields=fields, uplink=True)
        self.assertEqual(fctrl.adr, fields.get("adr"))
        self.assertEqual(fctrl.adr_ack_req, fields.get("adr_ack_req"))
        self.assertEqual(fctrl.ack, fields.get("ack"))
        self.assertEqual(fctrl.class_b, fields.get("class_b"))
        self.assertEqual(fctrl.fopts_len, fields.get("fopts_len"))

    def test_fctrl_ul_to_bytes_ff(self):
        bits = 0xFF
        fctrl = Fctrl.from_bits(bits=bits, uplink=True)
        bytez = bits.to_bytes(1, "big")
        self.assertEqual(fctrl.to_bytes(), bytez)

    def test_fctrl_ul_to_bytes_00(self):
        bits = 0x00
        fctrl = Fctrl.from_bits(bits=bits, uplink=True)
        bytez = bits.to_bytes(1, "big")
        self.assertEqual(fctrl.to_bytes(), bytez)

    def test_fctrl_ul_to_bytes_random(self):
        bits = randint(0x0, 0xFF)
        fctrl = Fctrl.from_bits(bits=bits, uplink=True)
        bytez = bits.to_bytes(1, "big")
        self.assertEqual(fctrl.to_bytes(), bytez)

    def test_fctrl_dl_from_bits_ff(self):
        bits = 0xFF
        fctrl = Fctrl.from_bits(bits=bits, uplink=False)
        self.assertEqual(fctrl.adr, 0x1)
        self.assertEqual(fctrl.ack, 0x1)
        self.assertEqual(fctrl.fpending, 0x1)
        self.assertEqual(fctrl.fopts_len, 0xf)

    def test_fctrl_dl_from_bits_00(self):
        bits = 0x00
        fctrl = Fctrl.from_bits(bits=bits, uplink=False)
        self.assertEqual(fctrl.adr, 0x0)
        self.assertEqual(fctrl.ack, 0x0)
        self.assertEqual(fctrl.fpending, 0x0)
        self.assertEqual(fctrl.fopts_len, 0x0)

    def test_fctrl_dl_from_bits_random(self):
        bits = randint(0x0, 0xff)
        fctrl = Fctrl.from_bits(bits=bits, uplink=False)
        self.assertEqual(fctrl.adr, (bits >> 7) & 1)
        self.assertEqual(fctrl.ack, (bits >> 5) & 1)
        self.assertEqual(fctrl.fpending, (bits >> 4) & 1)
        self.assertEqual(fctrl.fopts_len, (bits & 0xf))

    def test_fctrl_dl_from_fields_ff(self):
        fields = {
            "adr": 0x1,
            "ack": 0x1,
            "fpending": 0x1,
            "fopts_len": 0xf
        }
        fctrl = Fctrl.from_fields(fields=fields, uplink=False)
        self.assertEqual(fctrl.adr, 0x1)
        self.assertEqual(fctrl.ack, 0x1)
        self.assertEqual(fctrl.fpending, 0x1)
        self.assertEqual(fctrl.fopts_len, 0xf)

    def test_fctrl_dl_from_fields_00(self):
        fields = {
            "adr": 0x0,
            "ack": 0x0,
            "fpending": 0x0,
            "fopts_len": 0x0
        }
        fctrl = Fctrl.from_fields(fields=fields, uplink=False)
        self.assertEqual(fctrl.adr, 0x0)
        self.assertEqual(fctrl.ack, 0x0)
        self.assertEqual(fctrl.fpending, 0x0)
        self.assertEqual(fctrl.fopts_len, 0x0)

    def test_fctrl_dl_from_fields_random(self):
        fields = {
            "adr": randint(0x0, 0x1),
            "ack": randint(0x0, 0x1),
            "fpending": randint(0x0, 0x1),
            "fopts_len": randint(0x0, 0xf),
        }
        fctrl = Fctrl.from_fields(fields=fields, uplink=False)
        self.assertEqual(fctrl.adr, fields.get("adr"))
        self.assertEqual(fctrl.ack, fields.get("ack"))
        self.assertEqual(fctrl.fpending, fields.get("fpending"))
        self.assertEqual(fctrl.fopts_len, fields.get("fopts_len"))

    def test_fctrl_dl_to_bytes_ff(self):
        bits = 0xFF
        bytez = (bits&0xBF).to_bytes(1, "big")
        fctrl = Fctrl.from_bits(bits=bits, uplink=False)
        fctrl_bytes = fctrl.to_bytes()
        res = (int.from_bytes(fctrl_bytes)&0xBF).to_bytes(1, "big")
        self.assertEqual(res, bytez)

    def test_fctrl_dl_to_bytes_00(self):
        bits = 0x00
        bytez = (bits&0xBF).to_bytes(1, "big")
        fctrl = Fctrl.from_bits(bits=bits, uplink=False)
        fctrl_bytes = fctrl.to_bytes()
        res = (int.from_bytes(fctrl_bytes)&0xBF).to_bytes(1, "big")
        self.assertEqual(res, bytez)

    def test_fctrl_dl_to_bytes_random(self):
        bits = randint(0x0, 0xFF)
        bytez = (bits&0xBF).to_bytes(1, "big")
        fctrl = Fctrl.from_bits(bits=bits, uplink=False)
        fctrl_bytes = fctrl.to_bytes()
        res = (int.from_bytes(fctrl_bytes)&0xBF).to_bytes(1, "big")
        self.assertEqual(res, bytez)


if __name__ == '__main__':
    unittest.main()
