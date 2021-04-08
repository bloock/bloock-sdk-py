from enchaintesdk.infrastructure.hashing_client import HashingClient
from enchaintesdk.infrastructure.hashing.blake2b import Blake2b
from enchaintesdk.shared.utils import Utils
import numpy as np


class Message:
    __hashAlgorithm: HashingClient = Blake2b()

    def __init__(self, hash: str):
        self.hash = hash

    @staticmethod
    def from_(data):
        '''Returns message'''
        return Message.fromString(Utils.stringify(data))

    @staticmethod
    def fromHash(self, hash: str):
        '''Returns message'''
        return Message(hash)

    @staticmethod
    def fromHex(hex: str):
        '''Returns message'''
        dataArray = Utils.hexToBytes(hex)
        return Message(Message.__hashAlgorithm.generateHash(dataArray))

    @staticmethod
    def fromString(string: str):
        '''Returns message'''
        dataArray = Utils.stringToBytes(string)
        return Message(Message.__hashAlgorithm.generateHash(dataArray))

    @staticmethod
    def fromUint8Array(uint8Array: [np.uint8]):
        '''Returns message'''
        return Message(Message.__hashAlgorithm.generateHash(uint8Array))

    @staticmethod
    def sort(messages: [Message]):
        '''Returns message'''
        return messages.sort(key=lambda x: x.getHash().upper())

    @staticmethod
    def isValid(message) -> bool:
        if isinstance(message, Message):
            _message = message.getHash()

            if (len(_message) == 64 and Utils.isHex(_message)):
                return True
        return False

    def getHash(self) -> str:
        return self.hash

    def getUint8ArrayHash(self) -> [np.uint8]:
        return Utils.hexToBytes(self.hash)
