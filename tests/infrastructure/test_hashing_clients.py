from unittest import TestCase
from enchaintesdk.infrastructure.hashing.blake2b import Blake2b
from enchaintesdk.infrastructure.hashing.keccak import Keccak


class Blake2bTestCase(TestCase):

    def setUp(self):
        self.blake = Blake2b()

    def test_blake_generate_hash_64_zeros_string(self):
        data = b'0000000000000000000000000000000000000000000000000000000000000000'
        self.assertEqual(self.blake.generateHash(
            data), '681df247e1ece8365db91166ed273590019df392004d2ea25543335c71bbe2d2',
            'Hashes do not match')

    def test_blake_generate_hash_string(self):
        data = b'testing blake'
        self.assertEqual(self.blake.generateHash(
            data), 'bbe426afe3fae78c3d3e25502a3e197762ada886da94c1b8104a1984c8c4d886',
            'Hashes do not match')


class KeccakTestCase(TestCase):

    def setUp(self):
        self.keccak = Keccak()

    def test_keccak_generate_hash_64_zeros_hexa(self):
        data = bytes.fromhex(
            '0000000000000000000000000000000000000000000000000000000000000000')
        self.assertEqual(self.keccak.generateHash(
            data), '290decd9548b62a8d60345a988386fc84ba6bc95484008f6362f93160ef3e563',
            'Hashes do not match')

    def test_keccak_generate_hash_64_zeros_string(self):
        data = b'0000000000000000000000000000000000000000000000000000000000000000'
        self.assertEqual(self.keccak.generateHash(
            data), 'd874d9e5ad41e13e8908ab82802618272c3433171cdc3d634f3b1ad0e6742827',
            'Hashes do not match')

    def test_keccak_generate_hash_string(self):
        data = b'testing keccak'
        self.assertEqual(self.keccak.generateHash(
            data), '7e5e383e8e70e55cdccfccf40dfc5d4bed935613dffc806b16b4675b555be139',
            'Hashes do not match')
