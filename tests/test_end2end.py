import unittest
from enchaintesdk import *
import time
import json


class TestEnd2end(object):
    '''def test_end2end_success(self):
        sdk = EnchainteSDK(
            'VBO7uIR7xt7rfrJCPbcVvpMmm26OipFutXP9s5xkD79CCs30PoRqGGPyzgF55iXf')
        h = Hash.fromString('Jordi Estapé')
        print('Start writing: ' + h.getHash())
        result = sdk.write(h, 'hash')
        print('Write result: ' + h.getHash())

        if result == None:
            return

        found = False
        while not found:
            messages = sdk.getMessages([h])
            for m in messages:
                if m != None and m.status == 'success':
                    found = True
                else:
                    print('message status: '+m.status)
            time.sleep(0.5)

        proof = sdk.getProof([h])
        print('proof: '+proof.depth)

        valid = False
        while not valid:
            valid = sdk.verify(proof)
            time.sleep(0.5)
            print('valid: ' + valid)'''
