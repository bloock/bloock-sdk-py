from hashlib import blake2b
import numpy as np
import json

class Hash:
    def __init__(self, dataString):
        self.hash = dataString
    
    def getHash(self):
        return self.hash
    
    @staticmethod
    def generateBlake2b(data):
        hashBlake = blake2b(digest_size=32)
        hashBlake.update(data)
        return Hash(hashBlake.hexdigest())

    def fromHex(self):
        dataBytes = np.frombuffer(bytes.fromhex(self.hash),dtype=np.uint8)
        return Hash.generateBlake2b(dataBytes)

    def fromString(self):
        dataBytes = np.frombuffer(self.hash.encode(),dtype=np.uint8)
        return Hash.generateBlake2b(dataBytes)
    
    def fromUint8Array(self):
        return Hash.generateBlake2b(self.hash)
    
    def fromJson(self):
        jsnDic = json.loads(self.hash)
        newJsn = json.dumps(jsnDic, sort_keys=True, separators=(",",":"))
        return Hash(newJsn).fromString()

'''
newJsn = json.dumps({
  "name": "John",
  "age": 30,
  "married": True,
  "pets": None,
})
hs = Hash(newJsn).fromJson()
print(hs.getHash())'''