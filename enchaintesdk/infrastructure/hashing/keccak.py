from Crypto.Hash import keccak
import numpy as np
from ..hashing_client import HashingClient


class Keccak(HashingClient):
    def __init__(self):
        pass

    def generateHash(self, data: bytes) -> str:
        return keccak.new(digest_bits=256).update(data).hexdigest()
