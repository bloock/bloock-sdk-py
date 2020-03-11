import hash.hash as hash
import comms.comms as comms

class EnchainteSDK:
    def __init__(self):
        return

    def write(self, data):
        return comms.send(data)

    def getProof(self, data):
        return comms.verify(data)
