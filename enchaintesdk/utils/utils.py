import time
import threading
import numpy as np


class Utils:

    def __init__(self):
        self

    @staticmethod
    def is_hex(hex_str):
        try:
            if not isinstance(hex_str, str):
                return False
            int(hex_str, 16)
            return True
        except ValueError:
            return False

    @staticmethod
    def hexToBytes(hex_str):
        hx = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
        return np.fromiter((int(x, 16) for x in hx), dtype='uint8')


class SetInterval:
    def __init__(self, interval, writer):
        self.interval = interval
        self.__writer = writer
        self.stopEvent = threading.Event()
        thread = threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self):
        nextTime = time.time()+self.interval
        while not self.stopEvent.wait(nextTime-time.time()):
            nextTime += self.interval
            self.__writer.send()

    def cancel(self):
        self.stopEvent.set()
