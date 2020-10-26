from enchaintesdk.utils.utils import Utils
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

    def test_periodic_task(self):
        @Utils.periodic_task(0.1)
        def sum1(l):
            l[0] = l[0] + 1
        
        l = [0]
        algo = sum1(l)
        time.sleep(0.3)
        algo.set()
        time.sleep(1.1)
        time.sleep(1.1)
        self.assertEqual(l[0], 3)