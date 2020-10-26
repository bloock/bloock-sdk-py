from hashlib import blake2b
import numpy as np
import json
from ..utils.utils import Utils


class Message:
    def __init__(self, dataString):
        self._message = dataString

    def getMessage(self):
        return self._message

    @staticmethod
    def generateBlake2b(data):
        hashBlake = blake2b(digest_size=32)
        hashBlake.update(data)
        return Message(hashBlake.hexdigest())

    @staticmethod
    def fromHex(data):
        dataBytes = np.frombuffer(bytes.fromhex(data), dtype=np.uint8)
        return Message.generateBlake2b(dataBytes)

    @staticmethod
    def fromString(data):
        dataBytes = np.frombuffer(data.encode(), dtype=np.uint8)
        return Message.generateBlake2b(dataBytes)

    @staticmethod
    def fromUint8Array(data):
        return Message.generateBlake2b(data)

    @staticmethod
    def fromJson(data):
        jsnDic = json.loads(data)
        newJsn = json.dumps(jsnDic, sort_keys=True, separators=(",", ":"))
        return Message.fromString(newJsn)

    @staticmethod
    def fromMessage(data):
        return Message(data)

    def isValid(self):
        return (isinstance(self._message, str) and len(self._message) == 64 and Utils.is_hex(self._message))

    @staticmethod
    def mergeHex(a, b):
        c = np.concatenate((a, b), axis=None)
        hashBlake = blake2b(digest_size=32)
        hashBlake.update(c)
        return Utils.hexToBytes(hashBlake.hexdigest())

    @staticmethod
    def identicalKeys(a, b):
        return np.array_equal(a, b)

    @staticmethod
    def sort(messages):
        return sorted(messages, key=lambda h: h.getMessage())
