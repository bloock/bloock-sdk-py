from unittest import TestCase
from unittest import TestCase, mock
from enchaintesdk.message.entity.message_entity import Message
import numpy as np


class MessageTestCase(TestCase):

    def test_from_hash(self):
        self.assertEqual(Message.fromHash('test_hash')._Message__hash,
                         Message('test_hash')._Message__hash, "Messages do not match.")

    def test_from_hex(self):
        s = '10101010101010101010101010101010101010101010101010101010101010101111111111111111111111111111111111111111111111111111111111111111'
        p = 'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994a5'
        self.assertEqual(Message.fromHex(s)._Message__hash,
                         p, "Messages do not match.")

    def test_from_string(self):
        s = 'testing keccak'
        self.assertEqual(Message.fromString(s)._Message__hash,
                         '7e5e383e8e70e55cdccfccf40dfc5d4bed935613dffc806b16b4675b555be139',
                         'Hashes do not match')

    def test_from_bytes(self):
        b = bytes.fromhex(
            '10101010101010101010101010101010101010101010101010101010101010101111111111111111111111111111111111111111111111111111111111111111')
        p = 'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994a5'
        self.assertEqual(Message.fromBytes(b)._Message__hash,
                         p,
                         'Hashes do not match')

    def test_from_uint8(self):
        ar = np.asarray([16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16,
                        16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16,
                        17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
                        17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17], dtype=np.uint8)
        self.assertEqual(Message.fromUint8Array(ar)._Message__hash,
                         'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994a5',
                         'Hashes do not match')

    def test_is_valid_okay(self):
        self.assertTrue(Message.isValid(Message(
            '1010101010101010101010101010101010101010101010101010101010101010')), 'Message is not valid')

    def test_is_valid_missing_char(self):
        self.assertFalse(Message.isValid(Message(
            '010101010101010101010101010101010101010101010101010101010101010')), 'Message is not valid')

    def test_is_valid_wrong_char(self):
        self.assertFalse(Message.isValid(Message(
            'G010101010101010101010101010101010101010101010101010101010101010')), 'Message is not valid')

    def test_is_valid_not_message_instance(self):
        self.assertFalse(Message.isValid('test Message'),
                         'Message is not valid')
