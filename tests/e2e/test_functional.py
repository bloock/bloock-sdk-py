from unittest import TestCase
import os
from enchaintesdk.enchainte_client import EnchainteClient
from enchaintesdk.message.entity.message_entity import Message
from enchaintesdk.anchor.entity.anchor_entity import Anchor
from enchaintesdk.proof.entity.proof_entity import Proof
from enchaintesdk.config.entity.config_env_entity import ConfigEnv


def getSDK():
    api_key = os.environ['API_KEY']
    return EnchainteClient(api_key, ConfigEnv.TEST)


class testFunctionalSendMessage(TestCase):

    def test_send_message_okay(self):
        sdk = getSDK()
        messages = [
            Message.fromString("Example Data")
        ]
        try:
            sendReceipt = sdk.sendMessages(messages)
            anchor = sdk.waitAnchor(sendReceipt[0].anchor)
            self.assertIsInstance(anchor, Anchor)
        except Exception:
            self.fail('Should not return exception.')


class testFunctionalWaitAnchor(TestCase):
    def test_wait_anchor_okay(self):
        sdk = getSDK()
        messages = [
            Message.fromString("Example Data 1"),
            Message.fromString("Example Data 2"),
            Message.fromString("Example Data 3")
        ]
        send_receipt = sdk.sendMessages(messages)
        self.assertIsNotNone(send_receipt)

        receipt = sdk.waitAnchor(send_receipt[0].anchor)
        self.assertIsNotNone(receipt)
        self.assertGreater(receipt.id, 0)
        self.assertGreater(len(receipt.block_roots), 0)
        self.assertGreater(len(receipt.networks), 0)
        self.assertIsNotNone(receipt.root)
        self.assertIsNotNone(receipt.status)


class testFetchMessages(TestCase):
    def test_fetch_messages_okay(self):
        sdk = getSDK()
        messages = [
            Message.fromString("Example Data 1"),
            Message.fromString("Example Data 2"),
            Message.fromString("Example Data 3")
        ]
        send_receipt = sdk.sendMessages(messages)
        self.assertIsNotNone(send_receipt)

        sdk.waitAnchor(send_receipt[0].anchor)
        message_receipts = sdk.getMessages(messages)
        for mr in message_receipts:
            self.assertEqual(mr.status, 'Success',
                             'Status does not match with the expected.')


class testGetProof(TestCase):
    def test_get_proof_okay(self):
        sdk = getSDK()
        messages = [
            Message.fromString("Example Data 1"),
            Message.fromString("Example Data 2"),
            Message.fromString("Example Data 3")
        ]
        proof = sdk.getProof(messages)
        self.assertIsNotNone(proof)
        self.assertIsInstance(proof, Proof)
