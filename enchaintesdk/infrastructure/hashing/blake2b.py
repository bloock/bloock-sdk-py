from Crypto.Hash import BLAKE2b


class Blake2b:
    ''' Object in charge of generating Blake2b hashes sent to Enchainte's API.'''

    def __init__(self):
        pass

    def generateHash(self, data: bytes) -> str:
        ''' Returns the hash in hexadecimal string (with no 0x) format 
            given an object in Bytes.
        '''
        return BLAKE2b.new(digest_bits=256).update(data).hexdigest()
