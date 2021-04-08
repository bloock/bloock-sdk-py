from Crypto.Hash import BLAKE2b
from ..hashing_client import HashingClient


class Blake2b(HashingClient):
    ''' Object in charge of hashing life it self. Santa madona TODO'''

    def __init__(self):
        pass

    def generateHash(self, data: bytes) -> str:
        return BLAKE2b.new(digest_bits=256).update(data).hexdigest()
