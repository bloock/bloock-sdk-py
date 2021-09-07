from unittest import TestCase, mock
from bloock.record.entity.record_entity import Record


class RecordTestCase(TestCase):

    def test_from_hash(self):
        self.assertEqual(Record.fromHash('test_hash')._Record__hash,
                         Record('test_hash')._Record__hash, "Records do not match.")

    def test_from_hex(self):
        s = '10101010101010101010101010101010101010101010101010101010101010101111111111111111111111111111111111111111111111111111111111111111'
        p = 'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994a5'
        self.assertEqual(Record.fromHex(s)._Record__hash,
                         p, "Records do not match.")

    def test_from_hex_contents_not_hex_error(self):
        s = '101010101010101010101010101010101010101010101010101010101010101g'
        with self.assertRaises(ValueError):
            Record.fromHex(s)

    def test_from_hex_contents_not_string_error(self):
        with self.assertRaises(TypeError):
            Record.fromHex(23)

    def test_from_string(self):
        s = 'testing keccak'
        self.assertEqual(Record.fromString(s)._Record__hash,
                         '7e5e383e8e70e55cdccfccf40dfc5d4bed935613dffc806b16b4675b555be139',
                         'Hashes do not match')

    def test_from_string_not_string_error(self):
        with self.assertRaises(TypeError):
            Record.fromString(125)

    def test_from_bytes(self):
        b = bytes.fromhex(
            '10101010101010101010101010101010101010101010101010101010101010101111111111111111111111111111111111111111111111111111111111111111')
        p = 'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994a5'
        self.assertEqual(Record.fromBytes(b)._Record__hash,
                         p,
                         'Hashes do not match')

    def test_from_bytes_not_bytes_error(self):
        with self.assertRaises(TypeError):
            Record.fromBytes(125)

    def test_is_valid_okay(self):
        self.assertTrue(Record.isValid(Record(
            '1010101010101010101010101010101010101010101010101010101010101010')), 'Record is not valid')

    def test_is_valid_missing_char(self):
        self.assertFalse(Record.isValid(Record(
            '010101010101010101010101010101010101010101010101010101010101010')), 'Record is not valid')

    def test_is_valid_wrong_char(self):
        self.assertFalse(Record.isValid(Record(
            'G010101010101010101010101010101010101010101010101010101010101010')), 'Record is not valid')

    def test_is_valid_not_record_instance(self):
        self.assertFalse(Record.isValid('test Record'),
                         'Record is not valid')
