import numpy as np
import json
import string
from time import sleep
from enchaintesdk.message.entity.message_entity import Message


class Utils:
    @staticmethod
    def stringify(data) -> str:
        return str(data)

    @staticmethod
    def stringToBytes(string: str) -> [np.uint8]:
        return np.frombuffer(bytes.fromString(string), dtype=np.uint8)

    @staticmethod
    def hexToBytes(hex: str) -> [np.uint8]:
        return np.frombuffer(bytes.fromhex(hex), dtype=np.uint8)

    @staticmethod
    def bytesToString(array: [np.uint8]) -> str:
        return ''.join([chr(e) for e in array])

    @staticmethod
    def bytesToHex(array: [np.uint8]) -> str:
        return ''.join(['{:02x}'.format(e) for e in array])

    @staticmethod
    def isHex(h: str) -> bool:
        all(e in string.hexdigits for e in h)

    @staticmethod
    def sleep(ms: int):
        return sleep(ms / 1000)

    @staticmethod
    def merge(left: [np.uint8], right: [np.uint8]) -> [np.uint8]:
        return Message.fromUint8Array(np.concatenate([left, right]).getUint8ArrayHash()
