from unittest import TestCase
from enchaintesdk.shared.utils import Utils


class SharedTestCase(TestCase):
    def test_stringify(self):
        d = {'test': 'Perpetual Testing Initiative',
             'data': 'even more data'}
        self.assertEqual(Utils.stringify(d),
                         '{"data":"even more data","test":"Perpetual Testing Initiative"}',
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
