import os
import binascii
from unittest import TestCase
from enchaintesdk.infrastructure.http.exception.http_exception import HttpRequestException
from enchaintesdk.infrastructure.http.http_data import HttpData
from enchaintesdk.infrastructure.http.http_client import HttpClient
from enchaintesdk.enchainte_client import EnchainteClient
from enchaintesdk.message.entity.message_entity import Message
from enchaintesdk.anchor.entity.anchor_entity import Anchor
from enchaintesdk.proof.entity.proof_entity import Proof


def randHex(len: int) -> bytes:
    return binascii.b2a_hex(os.urandom(len))


def getSDK():
    api_key = os.environ['API_KEY']
    return EnchainteClient(api_key)


class testE2EEnchainteClient(TestCase):

    def test_basic_e2e(self):
        sdk = getSDK()
        messages = [Message.fromBytes(randHex(64))]
        send_receipt = sdk.sendMessages(messages)
        self.assertIsNotNone(send_receipt)
        sdk.waitAnchor(send_receipt[0].anchor)
        proof = sdk.getProof(messages)
        timestamp = sdk.verifyProof(proof)
        self.assertGreater(timestamp, 0, 'Timestamp was not greater than 0.')
