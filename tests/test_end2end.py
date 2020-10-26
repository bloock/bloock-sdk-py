import unittest
from enchaintesdk.enchainteClient import EnchainteClient
from enchaintesdk.entity.message import Message
import time
import json


class TestEnd2end(unittest.TestCase):

    def test_end2end_success(self):
        def resolve():
            pass
        
        def reject(e):
            raise e
        
        sdk = EnchainteClient(
            'APIKEY')
        h = Message.fromString('Albert Canyelles ')
        #print('Start writing: ' + h.getMessage())
        result = sdk.write(h.getMessage(), 'message', resolve, reject)
        #print('Write result: ' + h.getMessage())

        if result == None:
            raise ValueError('Deferred not created.')

        found = False
        while not found:
            messages = sdk.getMessages([h])
            for m in messages:
                if m != None and m.status == 'success':
                    found = True
                #else:
                    #print('message status: '+m.status)
            time.sleep(0.5)

        proof = sdk.getProof([h])
        #print('proof: '+proof.depth)

        valid = False
        while not valid:
            valid = sdk.verifyProof(proof)
            time.sleep(10)
            #print('valid: ' + str(valid))
    
    def test_end2end_success_2(self):
        def resolve():
            pass
        
        def reject(e):
            raise e
        
        sdk = EnchainteClient(
            'APIKEY')
        h = Message.fromString('Albert Canyelles ')
        #print('Start writing: ' + h.getMessage())
        result = sdk.write(h.getMessage(), 'message', resolve, reject)
        #print('Write result: ' + h.getMessage())

        if result == None:
            raise ValueError('Deferred not created.')

        found = False
        while not found:
            messages = sdk.getMessages([h])
            for m in messages:
                if m != None and m.status == 'success':
                    found = True
                #else:
                    #print('message status: '+m.status)
            time.sleep(0.5)

        valid = False
        while not valid:
            valid = sdk.verifyMessages([h])
            time.sleep(10)
            #print('valid: ' + str(valid))
    