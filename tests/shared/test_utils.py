from unittest import TestCase
from enchaintesdk.shared.utils import Utils
from datetime import datetime


class SharedTestCase(TestCase):
    def test_stringify(self):
        d = {'test': 'Perpetual Testing Initiative',
             'data': 'even more data'}
        self.assertEqual(Utils.stringify(d),
                         '{"data":"even more data","test":"Perpetual Testing Initiative"}',
                         'Expecting different string.')

    def test_stringify_not_serde(self):
        d = {'test': 'Perpetual Testing Initiative',
             'data': 'even more data',
             'timestamp': datetime(2020, 4, 21, 11, 10, 11)}
        self.assertEqual(Utils.stringify(d),
                         '{"data":"even more data","test":"Perpetual Testing Initiative","timestamp":"2020-04-21 11:10:11"}',
                         'Expecting different string.')

    def test_is_hex_okay(self):
        self.assertTrue(Utils.isHex('0123456789abcdef'),
                        'The input was a hex, hence should be True.')

    def test_is_hex_invalid_char(self):
        self.assertFalse(Utils.isHex('gg'),
                         'The input was a hex, hence should be True.')

    def test_is_hex_invalid_input(self):
        with self.assertRaises(TypeError):
            Utils.isHex(34)
