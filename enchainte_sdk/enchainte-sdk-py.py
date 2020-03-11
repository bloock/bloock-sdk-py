import hash.hash as hash
import comms.comms as comms
#import numpy as np
class EnchainteSDK:
    def __init__(self):
        return

    def write(self, data):
        return comms.send(data)

    def getProof(self, data):
        return comms.verify(data)

#hhex = hash.Hash('123456789abcde').fromHex().getHash()
#print( hhex == "c4635b1a2898593fce2716446b429bd62396cba1e0189dbc9c34b5608deacc63")
#print(Hash('enchainte').fromString().getHash() == "ab8e3ff984fce36be6e6cf01ec215df86556089bdebc20a663b4305f2fb67dc9")
#print(Hash(np.uint8([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])).fromUint8Array().getHash() == "e283ce217acedb1b0f71fc5ebff647a1a17a2492a6d2f34fb76b994a23ca8931")
#prova = EnchainteSDK()
#print(prova.write(hhex))
#print(prova.getProof(hhex))