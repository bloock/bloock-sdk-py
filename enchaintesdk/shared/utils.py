import numpy as np
import json
import string
from time import sleep


class Utils:
    @staticmethod
    def stringify(data) -> str:
        return str(data)

    @staticmethod
    def stringToBytes(string: str) -> [np.uint8]:
        return np.frombuffer(str.encode(string), dtype=np.uint8).tobytes()

    @staticmethod
    def hexToUint8Array(hex: str) -> [np.uint8]:
        return np.frombuffer(bytes.fromhex(hex), dtype=np.uint8).tobytes()

    @staticmethod
    def bytesToString(array: [np.uint8]) -> str:
        return ''.join([chr(e) for e in array])

    @staticmethod
    def bytesToHex(array: [np.uint8]) -> str:
        return ''.join(['{:02x}'.format(e) for e in array])

    @staticmethod
    def isHex(h: str) -> bool:
        return all(e in string.hexdigits for e in h)

    @staticmethod
    def sleep(ms: int):
        return sleep(ms / 1000)
