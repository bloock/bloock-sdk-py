import numpy as np


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
