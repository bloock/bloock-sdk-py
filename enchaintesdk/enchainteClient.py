from .writer import Writer
from .verifier import Verifier
from .entity.hash import Hash
from .entity.proof import Proof
from .comms.apiService import ApiService
from .comms.web3Service import Web3Service
from .utils.utils import Utils
import json


class EnchainteSDK:
    def __init__(self, apiKey):
        self.apiKey = apiKey
        ApiService.apiKey = apiKey

    # input: JSON, output: [String] containing the response's value form enchainte
    def write(self, data, data_type):
        if data_type == 'hex':
            hs = Hash.fromHex(data)
        elif data_type == 'str':
            hs = Hash.fromString(data)
        elif data_type == 'u8a':
            hs = Hash.fromUint8Array(data)
        elif data_type == 'json':
            hs = Hash.fromJson(data)
        elif data_type == 'hash':
            hs = Hash.fromHash(data)
        else:
            return ValueError('Non valid data_type value.')
        subscription = Writer.getInstance()
        return subscription.push(hs, True, False)  # s'ha de canviar òbviament

    def getProof(self, hashes):
        if not (hashes and isinstance(hashes, list) and all(isinstance(x, Hash)) for x in hashes):
            return ValueError
        sorted_hashes = Hash.sort(hashes)
        return ApiService.getProof(sorted_hashes)

    def verify(self, proof):
        if not proof.isValid():
            return ValueError('Proof is no valid')
        parsedLeaves = [Utils.hexToBytes(x) for x in proof.leaves]
        parsedNodes = [Utils.hexToBytes(x) for x in proof.nodes]
        parsedDepth = Utils.hexToBytes(proof.depth)
        parsedBitmap = Utils.hexToBytes(proof.bitmap)
        root = Verifier.verify(parsedLeaves, parsedNodes,
                               parsedDepth, parsedBitmap)
        web3value = Web3Service.validateRoot(root)
        return web3value

    def getMessages(self, hashes):
        if not (hashes and isinstance(hashes, list) and all(isinstance(x, Hash)) for x in hashes):
            return ValueError
        return ApiService.getMessages(hashes)
