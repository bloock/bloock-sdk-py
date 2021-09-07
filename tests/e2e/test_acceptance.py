import os
import binascii
from unittest import TestCase
from bloock.infrastructure.http.http_exception import HttpRequestException
from bloock.bloock_client import BloockClient
from bloock.record.entity.record_entity import Record
from bloock.exceptions import InvalidRecordException

from bloock import BloockClient, Record, Network
import random
import time
import os
import binascii


def randHex(len: int) -> bytes:
    return binascii.b2a_hex(os.urandom(len))


def getSDK():
    api_key = os.environ['API_KEY']
    host = os.environ['API_HOST']
    client = BloockClient(api_key)
    client.setApiHost(host)
    return client


class testE2EAcceptanceBloockClient(TestCase):

    def test_basic_e2e(self):
        sdk = getSDK()
        records = [Record.fromBytes(randHex(64))]
        send_receipt = sdk.sendRecords(records)
        self.assertIsNotNone(send_receipt)
        sdk.waitAnchor(send_receipt[0].anchor)
        proof = sdk.getProof(records)
        timestamp = sdk.verifyProof(proof, Network.BLOOCK_CHAIN)
        self.assertGreater(timestamp, 0, 'Timestamp was not greater than 0.')

    def test_send_records_invalid_record_input_wrong_char(self):
        sdk = getSDK()
        records = [Record(
            'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aG')]
        with self.assertRaises(InvalidRecordException):
            sdk.sendRecords(records)

    def test_send_records_invalid_record_input_missing_chars(self):
        sdk = getSDK()
        records = [Record(
            'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aa'),
            Record('e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994')]
        with self.assertRaises(InvalidRecordException):
            sdk.sendRecords(records)

    def test_send_records_invalid_record_input_wrong_start(self):
        sdk = getSDK()
        records = [Record(
            '0xe016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aa'),
            Record('0xe016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994bb')]
        with self.assertRaises(InvalidRecordException):
            sdk.sendRecords(records)

    def test_send_records_invalid_record_input_string(self):
        sdk = getSDK()
        records = [
            'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aa']
        with self.assertRaises(AttributeError):
            sdk.sendRecords(records)

    def test_send_records_empty_record_input(self):
        sdk = getSDK()
        self.assertEqual(sdk.sendRecords([]), [])

    def test_get_records_invalid_record_input_wrong_char(self):
        sdk = getSDK()
        records = [Record(
            'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aG')]
        with self.assertRaises(InvalidRecordException):
            sdk.getRecords(records)

    def test_get_records_invalid_record_input_missing_chars(self):
        sdk = getSDK()
        records = [Record(
            'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aa'),
            Record('e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994')]
        with self.assertRaises(InvalidRecordException):
            sdk.getRecords(records)

    def test_get_records_invalid_record_input_wrong_start(self):
        sdk = getSDK()
        records = [Record(
            '0xe016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aa'),
            Record('0xe016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994bb')]
        with self.assertRaises(InvalidRecordException):
            sdk.getRecords(records)

    def test_get_anchor_non_existing_anchor(self):
        sdk = getSDK()
        with self.assertRaises(HttpRequestException):
            sdk.getAnchor(666666666666666666)

    def test_get_anchor_invalid_input(self):
        sdk = getSDK()
        with self.assertRaises(TypeError):
            sdk.getAnchor('anchor')

    def test_wait_anchor_non_existing_anchor(self):
        sdk = getSDK()
        self.assertIsNone(sdk.waitAnchor(666666666666666666, 3000),
                          'It should have not found any anchor')

    def test_wait_anchor_invalid_input(self):
        sdk = getSDK()
        with self.assertRaises(TypeError):
            sdk.waitAnchor('anchor')

    def test_get_proof_invalid_record_input_wrong_char(self):
        sdk = getSDK()
        records = [Record(
            'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aG')]
        with self.assertRaises(InvalidRecordException):
            sdk.getProof(records)

    def test_get_proof_invalid_record_input_missing_chars(self):
        sdk = getSDK()
        records = [Record(
            'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aa'),
            Record('e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994')]
        with self.assertRaises(InvalidRecordException):
            sdk.getProof(records)

    def test_get_proof_invalid_record_input_wrong_start(self):
        sdk = getSDK()
        records = [Record(
            '0xe016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aa'),
            Record('0xe016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994bb')]
        with self.assertRaises(InvalidRecordException):
            sdk.getProof(records)

    def test_get_proof_empty_record_input(self):
        sdk = getSDK()
        self.assertEqual(sdk.getProof([]), None)

    def test_get_proof_none_existing_leaf(self):
        sdk = getSDK()
        with self.assertRaises(HttpRequestException):
            sdk.getProof(
                [Record('0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef')])

    def test_verify_records_invalid_record_input_wrong_char(self):
        sdk = getSDK()
        records = [Record(
            'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aG')]
        with self.assertRaises(InvalidRecordException):
            sdk.verifyRecords(records, Network.BLOOCK_CHAIN)

    def test_verify_records_invalid_record_input_missing_chars(self):
        sdk = getSDK()
        records = [Record(
            'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aa'),
            Record('e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994')]
        with self.assertRaises(InvalidRecordException):
            sdk.verifyRecords(records, Network.BLOOCK_CHAIN)

    def test_verify_records_invalid_record_input_wrong_start(self):
        sdk = getSDK()
        records = [Record(
            '0xe016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aa'),
            Record('0xe016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994bb')]
        with self.assertRaises(InvalidRecordException):
            sdk.verifyRecords(records, Network.BLOOCK_CHAIN)

    def test_verify_records_empty_record_input(self):
        sdk = getSDK()
        self.assertEqual(sdk.verifyRecords([], Network.BLOOCK_CHAIN), None)

    def test_verify_records_none_existing_leaf(self):
        sdk = getSDK()
        with self.assertRaises(HttpRequestException):
            sdk.verifyRecords(
                [Record('0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef')], Network.BLOOCK_CHAIN)
