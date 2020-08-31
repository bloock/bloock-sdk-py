from enchaintesdk.utils.utils import *
import unittest
import numpy as np
import time


class TestUtils(unittest.TestCase):
    def test_isHex_success(self):
        self.assertTrue(Utils.is_hex('abcdef0123456789'))

    def test_isHex_type_error(self):
        self.assertFalse(Utils.is_hex(1234567890))

    def test_isHex_value_error(self):
        self.assertFalse(Utils.is_hex('abcdef0123456789g'))

    def test_hexToBytes_success(self):
        self.assertTrue(Utils.hexToBytes('0a')[0] == 10)
