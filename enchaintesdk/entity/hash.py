from hashlib import blake2b
import numpy as np
from collections import deque
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

    """@staticmethod
    def verifyProof(leaves, proof):
        '''Validates de correctness of the proof return by the Enchainte Api.
        - Inputs::  leaves: list of hashes from the leaves sent to Enchainte in hexadecimal strings.
                    proof: dictionary returned from Enchainte.
        - Output::  boolean: True if the current proof is valid.'''

        dic_bm = proof['bitmap']
        dic_de = proof['depth']
        dic_no = proof['nodes']
        bitmap = [np.uint8(int(dic_bm[i:i+2],16)) for i in range(0, len(str_bm), 2)]
        mp_depth = [np.uint8(int(dic_de[i:i+2],16)) for i in range(0, len(str_de), 2)]
        nodes = [[h for h in n.replace('[','').split(',')] for n in str_no.split(']')] # suposo que ho parsejo a la llista de lista d'uint8

        it_leaves = 0
        it_nodes = 0
        it_bitmap = 0
        curr_bit = 0
        stack = deque()
        while it_nodes < nodes.len()-1 or it_leaves < leaves.len():
            is_leaf = bitmap[it_bitmap] & (1 << (7 - (curr_bit%8))) > 0
            if is_leaf:
                act_hash = leaves[it_leaves]
            else:
                act_hash = nodes[it_nodes]"""


'''
newJsn = json.dumps({
  "name": "John",
  "age": 30,
  "married": True,
  "pets": None,
})
hs = Hash(newJsn).fromJson()
print(hs.getHash())'''
