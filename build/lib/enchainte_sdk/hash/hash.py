from hashlib import blake2b
import numpy as np
import json

class Hash:
    def __init__(self, dataString):
        self.hash = dataString
    
    def getHash(self):
        return self.hash
    
    def fromHex(self):
        dataBytes = np.frombuffer(bytes.fromhex(self.hash),dtype=np.uint8)
        hashBlake = blake2b(digest_size=32)
        hashBlake.update(dataBytes)
        return Hash(hashBlake.hexdigest())

    def fromString(self):
        dataBytes = np.frombuffer(self.hash.encode(),dtype=np.uint8)
        hashBlake = blake2b(digest_size=32)
        hashBlake.update(dataBytes)
        return Hash(hashBlake.hexdigest())
    
    def fromUint8Array(self):
        hashBlake = blake2b(digest_size=32)
        hashBlake.update(self.hash)
        return Hash(hashBlake.hexdigest())
