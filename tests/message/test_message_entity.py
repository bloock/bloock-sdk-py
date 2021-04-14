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
        p = 'd8a0e356c183fccc77faa797f273905ade2baab574a98af314ff7acf7bf4d329'
        self.assertEqual(Message.fromHex(s)._Message__hash,
                         p, "Messages do not match.")

    def test_from_string(self):
        s = 'testing blake'
        self.assertEqual(Message.fromString(s)._Message__hash,
                         'bbe426afe3fae78c3d3e25502a3e197762ada886da94c1b8104a1984c8c4d886',
                         'Hashes do not match')

    def test_from_bytes(self):
        b = bytes.fromhex(
            '10101010101010101010101010101010101010101010101010101010101010101111111111111111111111111111111111111111111111111111111111111111')
        p = 'd8a0e356c183fccc77faa797f273905ade2baab574a98af314ff7acf7bf4d329'
        self.assertEqual(Message.fromBytes(b)._Message__hash,
                         p,
                         'Hashes do not match')

    def test_from_uint8(self):
        ar = np.asarray([16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16,
                        16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 16,
                        17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17,
                        17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17, 17], dtype=np.uint8)
        self.assertEqual(Message.fromUint8Array(ar)._Message__hash,
                         'd8a0e356c183fccc77faa797f273905ade2baab574a98af314ff7acf7bf4d329',
                         'Hashes do not match')

    def test_sort(self):
        arr = [Message('A0B0C0'), Message('FFFFFF'), Message('000201')]
        self.assertEquals([x._Message__hash for x in Message.sort(arr)],
                          ['000201', 'A0B0C0', 'FFFFFF'],
                          'arrays do not match')

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

    '''def test_merge(self):
        m1 = '1010101010101010101010101010101010101010101010101010101010101010'
        m2 = '1111111111111111111111111111111111111111111111111111111111111111'
        p = 'd8a0e356c183fccc77faa797f273905ade2baab574a98af314ff7acf7bf4d329'
        self.assertEqual(Message.merge(
            Message(m1), Message(m2)), p, "Merge does not match")'''
