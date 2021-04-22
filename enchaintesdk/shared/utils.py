import json
import string
from time import sleep


class Utils:
    @staticmethod
    def stringify(data: dict) -> str:
        return json.dumps(data, sort_keys=True, separators=(',', ':'), default=str)

    @staticmethod
    def stringToBytes(string: str) -> bytes:
        return bytes(string, 'utf-8')

    @staticmethod
    def isHex(h: str) -> bool:
        return all(e in string.hexdigits for e in h)

    @staticmethod
    def sleep(ms: int):
        return sleep(ms / 1000)
