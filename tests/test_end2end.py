import unittest
from enchaintesdk.enchainteClient import EnchainteClient
from enchaintesdk.entity.hash import Hash
import time
import json


class TestEnd2end(unittest.TestCase):
    '''def test_end2end_success(self):
        sdk = EnchainteClient(
            'gj6mIevvurbf0466EMTWk3pCiF9ZzTxqIl81Sjtfn80DC37yFW4QbHpJp-2uBEOH')
        h = Hash.fromString('Jordi ')
        print('Start writing: ' + h.getHash())
        result = sdk.write(h.getHash(), 'hash')
        print('Write result: ' + h.getHash())

        if result == None:
            raise ValueError('Deferred not created.')

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
            time.sleep(10)
            print('valid: ' + str(valid))
    '''