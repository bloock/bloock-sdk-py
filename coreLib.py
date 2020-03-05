from hashlib import blake2b
import json
import comms

#TODO: discover why blake2b returns 40 bytes instead of 32
def genHash(data):
    dataDict = json.loads(data)
    dataBytes = json.dumps(dataDict).encode('utf-8')
    hashBlake = blake2b(digest_size=32)
    hashBlake.update(dataBytes)
    return hashBlake.hexdigest()

def write(data):
    hashS = genHash(data)
    return comms.send(hashS)

def getProof(data):
    hashS = genHash(data)
    return comms.verify(hashS)
