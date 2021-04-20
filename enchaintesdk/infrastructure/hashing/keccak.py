from Crypto.Hash import keccak


class Keccak:
    '''Object in charge of generating Keccak hashes sent to Enchainte's API.'''

    def __init__(self):
        pass

    def generateHash(self, data: bytes) -> str:
        ''' Returns the hash in hexadecimal string (with no 0x) format 
            given an object in Bytes.
        '''
        return keccak.new(digest_bits=256).update(data).hexdigest()
