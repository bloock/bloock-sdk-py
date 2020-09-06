from hashlib import blake2b
import numpy as np
import json
from ..utils.utils import Utils


class Hash:
    def __init__(self, dataString):
        self._hash = dataString

    def getHash(self):
        return self._hash

    @staticmethod
    def generateBlake2b(data):
        hashBlake = blake2b(digest_size=32)
        hashBlake.update(data)
        return Hash(hashBlake.hexdigest())

    @staticmethod
    def fromHex(data):
        dataBytes = np.frombuffer(bytes.fromhex(data), dtype=np.uint8)
        return Hash.generateBlake2b(dataBytes)

    @staticmethod
    def fromString(data):
        dataBytes = np.frombuffer(data.encode(), dtype=np.uint8)
        return Hash.generateBlake2b(dataBytes)

    @staticmethod
    def fromUint8Array(data):
        return Hash.generateBlake2b(data)

    @staticmethod
    def fromJson(data):
        jsnDic = json.loads(data)
        newJsn = json.dumps(jsnDic, sort_keys=True, separators=(",", ":"))
        return Hash.fromString(newJsn)

    @staticmethod
    def fromHash(data):
        return Hash(data)

    def isValid(self):
        return (isinstance(self._hash, str) and len(self._hash) == 64 and Utils.is_hex(self._hash))

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
    def sort(hashes):
        return sorted(hashes, key=lambda h: h.getHash())
