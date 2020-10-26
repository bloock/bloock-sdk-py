from enchaintesdk.entity.message import Message
import unittest
import numpy as np
import json


class TestMessage(unittest.TestCase):
    def test_fromHex(self):
        h = Message.fromHex('123456789abcde')
        self.assertTrue(isinstance(h, Message))
        self.assertTrue(Message.identicalKeys(
            h.getMessage(),
            'c4635b1a2898593fce2716446b429bd62396cba1e0189dbc9c34b5608deacc63'
        ))

    def test_fromString(self):
        h = Message.fromString('enchainte')
        self.assertTrue(isinstance(h, Message))
        self.assertTrue(Message.identicalKeys(
            h.getMessage(),
            'ab8e3ff984fce36be6e6cf01ec215df86556089bdebc20a663b4305f2fb67dc9'
        ))

    def test_fromUint8Array(self):
        h = Message.fromUint8Array(
            np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype='uint8'))
        self.assertTrue(isinstance(h, Message))
        self.assertTrue(Message.identicalKeys(
            h.getMessage(),
            'e283ce217acedb1b0f71fc5ebff647a1a17a2492a6d2f34fb76b994a23ca8931'
        ))

    def test_fromJson(self):
        j1 = '{"color":"gold","null":null, "number":  123,"object":  {"a":"b","c":"d"},"string":"Hello World","array":[1,2,3],"boolean":true}'
        r1 = Message.fromJson(j1).getMessage()
        self.assertEqual(
            r1, 'd8a82f8d74e0665f9604cd2e8f76a88a478a3d22068fa074c444158ea3d08887')
        j2 = '{"array": [1,2,3],"boolean":true,"color":"gold","null":null, "number":  123,"object":  {"a":"b","c":"d"},"string":"Hello World"}'
        r2 = Message.fromJson(j2).getMessage()
        self.assertEqual(
            r2, 'd8a82f8d74e0665f9604cd2e8f76a88a478a3d22068fa074c444158ea3d08887')

    def test_fromMessage(self):
        h = Message.fromMessage(
            'c4635b1a2898593fce2716446b429bd62396cba1e0189dbc9c34b5608deacc63')
        self.assertTrue(isinstance(h, Message))
        self.assertTrue(Message.identicalKeys(
            h.getMessage(),
            'c4635b1a2898593fce2716446b429bd62396cba1e0189dbc9c34b5608deacc63'
        ))

    def test_isValid_success(self):
        message = Message(
            '123456789abcdef123456789abcdef123456789abcdef123456789abcdef1234')
        self.assertTrue(Message.isValid(message))

    def test_isValid_error_type(self):
        message = Message(25)
        self.assertFalse(Message.isValid(message))

    def test_isValid_error_lenght(self):
        message = Message(
            '123456789abcdef123456789abcdef123456789abcdef123456789abcdef123456789abcdef')
        self.assertFalse(Message.isValid(message))

    def test_isValid_error_hex(self):
        message = Message(
            '123456789abcdef123456789abcdef123456789abcdef123456789abcdef123g')
        self.assertFalse(Message.isValid(message))

    # faltarà posar-nos d'acord entre en marc i jo per fer el test de Json
