from bloock.config.entity.networks_entity import Network
from unittest import TestCase
import os, time
from bloock.bloock_client import BloockClient
from bloock.record.entity.record_entity import Record
from bloock.anchor.entity.anchor_entity import Anchor
from bloock.proof.entity.proof_entity import Proof
from bloock.config.entity.config_env_entity import ConfigEnv


def getSDK():
    api_key = os.environ['API_KEY']
    host = os.environ['API_HOST']
    client = BloockClient(api_key)
    client.setApiHost(host)
    return client


class testFunctionalSendRecord(TestCase):

    def test_send_record_okay(self):
        sdk = getSDK()
        records = [
            Record.fromString("Example Data")
        ]
        try:
            sendReceipt = sdk.sendRecords(records)
            anchor = sdk.waitAnchor(sendReceipt[0].anchor)
            self.assertIsInstance(anchor, Anchor)
        except Exception:
            self.fail('Should not return exception.')


class testFunctionalWaitAnchor(TestCase):
    def test_wait_anchor_okay(self):
        sdk = getSDK()
        records = [
            Record.fromString("Example Data 1"),
            Record.fromString("Example Data 2"),
            Record.fromString("Example Data 3")
        ]
        send_receipt = sdk.sendRecords(records)
        self.assertIsNotNone(send_receipt)

        receipt = sdk.waitAnchor(send_receipt[0].anchor)
        self.assertIsNotNone(receipt)
        self.assertGreater(receipt.id, 0)
        self.assertGreater(len(receipt.block_roots), 0)
        self.assertGreater(len(receipt.networks), 0)
        self.assertIsNotNone(receipt.root)
        self.assertIsNotNone(receipt.status)


class testFetchRecords(TestCase):
    def test_fetch_records_okay(self):
        sdk = getSDK()
        records = [
            Record.fromString("Example Data 1"),
            Record.fromString("Example Data 2"),
            Record.fromString("Example Data 3")
        ]
        send_receipt = sdk.sendRecords(records)
        self.assertIsNotNone(send_receipt)

        sdk.waitAnchor(send_receipt[0].anchor)
        record_receipts = sdk.getRecords(records)
        for mr in record_receipts:
            self.assertEqual(mr.status, 'Success',
                             'Status does not match with the expected.')


class testGetProof(TestCase):
    def test_get_proof_okay(self):
        sdk = getSDK()
        records = [
            Record.fromString("Example Data 1"),
            Record.fromString("Example Data 2"),
            Record.fromString("Example Data 3")
        ]
        proof = sdk.getProof(records)
        self.assertIsNotNone(proof)
        self.assertIsInstance(proof, Proof)
    
    def test_get_proof_bloockchain_okay(self):
        sdk = getSDK()
        records = [
            Record.fromString("Example Data 1"),
            Record.fromString("Example Data 2"),
            Record.fromString("Example Data 3")
        ]
        proof = sdk.getProof(records, network = Network.BLOOCK_CHAIN)
        self.assertIsNotNone(proof)
        self.assertIsInstance(proof, Proof)
