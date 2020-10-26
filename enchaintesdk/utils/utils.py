import numpy as np
import threading
import time


class Utils:

    def __init__(self):
        self

    @staticmethod
    def is_hex(hex_str):
        ''' Returns True if "hex_str" is an hexadecimal string, otherwise
            returns False.'''

        try:
            if not isinstance(hex_str, str):
                return False
            int(hex_str, 16)
            return True
        except ValueError:
            return False

    @staticmethod
    def hexToBytes(hex_str):
        ''' Converts a string of hexadecimal bytes (2 characters per byte) 
            to its array of UInt8 value.'''
        hx = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
        return np.fromiter((int(x, 16) for x in hx), dtype='uint8')

    @staticmethod
    def bytesToHex(byte_array):
        ''' Converts a string of hexadecimal bytes (2 characters per byte) 
            to its array of UInt8 value.'''
        result = ''
        for b in byte_array:
            value = '%x' % b
            if len(value) == 1:
                result += '0'
            result += value
        return result

    @staticmethod
    def periodic_task(interval):
        ''' Decorator method for executing a function periodically in a 
            different thread. Interval represents the time between 
            executions, and killers a list with only one bool that when
            when set True stops the execution.'''
            
        def outer_wrap(function):
            def wrap(*args, **kwargs):
                stop = threading.Event()
                def inner_wrap():
                    nextTime = time.time()+interval
                    while not stop.isSet() and not stop.wait(nextTime-time.time()):
                        nextTime += interval
                        function(*args, **kwargs)

                t = threading.Timer(0, inner_wrap)
                #t.daemon = True
                t.start()
                return stop
            return wrap
        return outer_wrap