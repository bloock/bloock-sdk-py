import hash.hash as hash
import comms.comms as comms
#import json

class EnchainteSDK:
    def __init__(self):
        return
    #input: JSON, output: [String] containing the response's value form enchainte
    def write_Json(self, data):
        hs = hash.Hash(data).fromJson()
        res = comms.send(hs.getHash())
        return res['hash']

    #input: JSON, output: List containing Strings of the hashes forming the proof
    def getProof(self, data):
        hs = hash.Hash(data).fromJson()
        proof = comms.verify(hs.getHash())
        return proof['proof']
        #return comms.verify(data)

'''
newJsn = json.dumps({
  "name": "John",
  "age": 30,
  "married": True,
  "pets": None,
})
en = EnchainteSDK()
res = en.write_Json(newJsn)
prof = en.getProof(newJsn)
print(prof)'''