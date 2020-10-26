from .writer import Writer
from .verifier import Verifier
from .entity.message import Message
from .entity.proof import Proof
from .comms import ApiService, Web3Service, ConfigService
from .utils.utils import Utils
import json, time

class EnchainteClient:
    def __init__(self, apiKey):
        self.apiKey = apiKey
        self.configService = ConfigService()
        self.config = [self.configService.getConfig()]
        Writer.set_config(self.config)
        ApiService.apiKey = apiKey
        self.writer = Writer.getInstance()
        self.writer.send()

    def write(self, data, data_type, resolve, reject):
        ''' Inputs a "data" value and its type to return to return a "deferred" object containing
            its the state inside the Enchainte API (queued, sent or failed). Current accepted datatypes
            are: hexadecimal strings "hex", strings "str", byte arrays "u8a", "json", and enchainte's
            message objects "Message".'''

        if data_type == 'hex':
            hs = Message.fromHex(data)
        elif data_type == 'str':
            hs = Message.fromString(data)
        elif data_type == 'u8a':
            hs = Message.fromUint8Array(data)
        elif data_type == 'json':
            hs = Message.fromJson(data)
        elif data_type == 'message':
            hs = Message.fromMessage(data)
        else:
            return ValueError('Non valid data_type value.')
        subscription = Writer.getInstance()
        return subscription.push(hs, resolve, reject)

    def getProof(self, messages):
        ''' Returns a "Proof" object for a given "list of Message" elements.'''

        if not self.__verifyAreMessages:
            return ValueError
        sorted_messages = Message.sort(messages)
        return ApiService.getProof(sorted_messages, self.config[0])

    def verifyProof(self, proof):
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
        web3value = Web3Service.validateRoot(Utils.bytesToHex(root), self.config[0])
        return web3value

    def getMessages(self, messages):
        ''' Returns a list of "MessageReceipt" elements containing rellevant information about the 
            list of "Hash" elements recived as input.'''

        if not self.__verifyAreMessages:
            return ValueError
        return ApiService.getMessages(messages, self.config[0])

    def waitMessageReceipt(self, messages):
        if not self.__verifyAreMessages:
            return ValueError
        completed = False
        attempts = 0
        
        while not completed:
            messageReceipts = self.getMessages(messages)
            completed = all([r.status == 'success' for r in messageReceipts])
            if not completed:
                time.sleep(self.config[0].wait_message_interval_default +
                    attempts * self.config[0].wait_message_interval_factor)
            attempts += 1
        
        return messageReceipts

    def verifyMessages(self, messages):
        proof = self.getProof(messages)
        return self.verifyProof(proof)

    @staticmethod
    def __verifyAreMessages(messages):
        if not (messages and isinstance(messages, list) and all(isinstance(x, Message)) for x in messages):
            return False
        return True
