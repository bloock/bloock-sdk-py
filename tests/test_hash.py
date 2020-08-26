from enchaintesdk.entity.hash import Hash
import unittest
import numpy as np


class TestHash(unittest.TestCase):
    def test_fromHex(self):
        h = Hash.fromHex('123456789abcde')
        self.assertTrue(isinstance(h, Hash))
        self.assertTrue(Hash.identicalKeys(
            h.getHash(),
            'c4635b1a2898593fce2716446b429bd62396cba1e0189dbc9c34b5608deacc63'
        ))

    def test_fromString(self):
        h = Hash.fromString('enchainte')
        self.assertTrue(isinstance(h, Hash))
        self.assertTrue(Hash.identicalKeys(
            h.getHash(),
            'ab8e3ff984fce36be6e6cf01ec215df86556089bdebc20a663b4305f2fb67dc9'
        ))

    def test_fromUint8Array(self):
        h = Hash.fromUint8Array(
            np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype='uint8'))
        self.assertTrue(isinstance(h, Hash))
        self.assertTrue(Hash.identicalKeys(
            h.getHash(),
            'e283ce217acedb1b0f71fc5ebff647a1a17a2492a6d2f34fb76b994a23ca8931'
        ))

    def test_fromHash(self):
        h = Hash.fromHash(
            'c4635b1a2898593fce2716446b429bd62396cba1e0189dbc9c34b5608deacc63')
        self.assertTrue(isinstance(h, Hash))
        self.assertTrue(Hash.identicalKeys(
            h.getHash(),
            'c4635b1a2898593fce2716446b429bd62396cba1e0189dbc9c34b5608deacc63'
        ))

    def test_isValid_success(self):
        hash = Hash(
            '123456789abcdef123456789abcdef123456789abcdef123456789abcdef1234')
        self.assertTrue(Hash.isValid(hash))

    def test_isValid_error_type(self):
        hash = Hash(25)
        self.assertFalse(Hash.isValid(hash))

    def test_isValid_error_lenght(self):
        hash = Hash(
            '123456789abcdef123456789abcdef123456789abcdef123456789abcdef123456789abcdef')
        self.assertFalse(Hash.isValid(hash))

    def test_isValid_error_hex(self):
        hash = Hash(
            '123456789abcdef123456789abcdef123456789abcdef123456789abcdef123g')
        self.assertFalse(Hash.isValid(hash))

    # faltarà posar-nos d'acord entre en marc i jo per fer el test de Json
