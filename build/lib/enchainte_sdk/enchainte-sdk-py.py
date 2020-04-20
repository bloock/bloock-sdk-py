import hash.hash as hash
import comms.comms as comms

class EnchainteSDK:
    def __init__(self):
        return

    def write(self, data):
        return comms.send(data.getHash())

    def getProof(self, data):
        return comms.verify(data.getHash())
