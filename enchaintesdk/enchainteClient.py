from .writer import Writer
from .verifier import Verifier
from enchaintesdk.entity.hash import Hash
from enchaintesdk.entity.proof import Proof
from enchaintesdk.comms.apiService import ApiService
from enchaintesdk.comms.web3Service import Web3Service
from enchaintesdk.utils.utils import Utils
from enchaintesdk.writerTimer import WriterTimer
import json
from .utils.constants import SEND_INTERVAL


class EnchainteClient:
    def __init__(self, apiKey):
        self.apiKey = apiKey
        ApiService.apiKey = apiKey
        self.wTimer = WriterTimer(SEND_INTERVAL)

    def write(self, data, data_type):
        ''' Inputs a "data" value and its type to return to return a "deferred" object containing
            its the state inside the Enchainte API (queued, sent or failed). Current accepted datatypes
            are: hexadecimal strings "hex", strings "str", byte arrays "u8a", "json", and enchainte's
            hash objects "Hash".'''

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
        ''' Returns a "Proof" object for a given "list of Hash" elements.'''

        if not (hashes and isinstance(hashes, list) and all(isinstance(x, Hash)) for x in hashes):
            return ValueError
        sorted_hashes = Hash.sort(hashes)
        return ApiService.getProof(sorted_hashes)

    def verify(self, proof):
        ''' Returns a boolean asserting if the root obtained form the "Proof" input is successfully
            inserted in a blockchain block.'''

        if not proof.isValid():
            return ValueError('Proof is no valid')
        parsedLeaves = [Utils.hexToBytes(x) for x in proof.leaves]
        parsedNodes = [Utils.hexToBytes(x) for x in proof.nodes]
        parsedDepth = Utils.hexToBytes(proof.depth)
        parsedBitmap = Utils.hexToBytes(proof.bitmap)
        root = Verifier.verify(parsedLeaves, parsedNodes,
                               parsedDepth, parsedBitmap)
        web3value = Web3Service.validateRoot(Utils.bytesToHex(root))
        return web3value

    def getMessages(self, hashes):
        ''' Returns a list of "Message" elements containing rellevant information about the 
            list of "Hash" elements recived as input.'''

        if not (hashes and isinstance(hashes, list) and all(isinstance(x, Hash)) for x in hashes):
            return ValueError
        return ApiService.getMessages(hashes)
