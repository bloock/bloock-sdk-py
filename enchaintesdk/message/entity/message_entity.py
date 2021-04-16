#from enchaintesdk.infrastructure.hashing.blake2b import Blake2b
from enchaintesdk.infrastructure.hashing.keccak import Keccak
from enchaintesdk.shared.utils import Utils
import numpy as np


class Message:
    __hashAlgorithm = Keccak()

    def __init__(self, hash: str):
        self.__hash = hash

    @staticmethod
    def fromDict(data: dict):
        '''Returns message'''
        return Message.fromString(Utils.stringify(data))

    @staticmethod
    def fromHash(hash: str):
        '''Returns message'''
        return Message(hash)

    @staticmethod
    def fromHex(hex: str):
        '''Returns message'''
        dataArray = bytes.fromhex(hex)
        return Message(Message.__hashAlgorithm.generateHash(dataArray))

    @staticmethod
    def fromString(string: str):
        '''Returns message'''
        dataArray = Utils.stringToBytes(string)
        return Message(Message.__hashAlgorithm.generateHash(dataArray))

    @staticmethod
    def fromBytes(b: bytes):
        '''Returns message'''
        return Message(Message.__hashAlgorithm.generateHash(b))

    @staticmethod
    def fromUint8Array(uint8Array: [np.uint8]):
        '''Returns message'''
        return Message(Message.__hashAlgorithm.generateHash(uint8Array.tobytes()))

    @staticmethod
    def isValid(message) -> bool:
        if isinstance(message, Message):
            _message = message.getHash()

            if (len(_message) == 64 and Utils.isHex(_message)):
                return True
        return False

    def getHash(self) -> str:
        return self.__hash
