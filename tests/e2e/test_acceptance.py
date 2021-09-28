import os
import binascii
from unittest import TestCase
from bloock.infrastructure.http.http_exception import HttpRequestException
from bloock.bloock_client import BloockClient
from bloock.record.entity.record_entity import Record
from bloock.exceptions import InvalidRecordException

from bloock import BloockClient, Record, Network, NetworkConfiguration
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
    bloockchain_config = NetworkConfiguration()
    bloockchain_config.contract_address = '0xd2d1BBcbee7741f8C846826F55b7c17fc5cf969a'
    bloockchain_config.contract_abi = '[{"inputs":[{"internalType":"address","name":"role_manager","type":"address"},{"internalType":"address","name":"state_manager","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"previousAdminRole","type":"bytes32"},{"indexed":true,"internalType":"bytes32","name":"newAdminRole","type":"bytes32"}],"name":"RoleAdminChanged","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleGranted","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"bytes32","name":"role","type":"bytes32"},{"indexed":true,"internalType":"address","name":"account","type":"address"},{"indexed":true,"internalType":"address","name":"sender","type":"address"}],"name":"RoleRevoked","type":"event"},{"inputs":[],"name":"DEFAULT_ADMIN_ROLE","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"STATE_MANAGER","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"}],"name":"getRoleAdmin","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"state_root","type":"bytes32"}],"name":"getState","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"grantRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"hasRole","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"state_root","type":"bytes32"}],"name":"isStatePresent","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"renounceRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32","name":"role","type":"bytes32"},{"internalType":"address","name":"account","type":"address"}],"name":"revokeRole","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"bytes32","name":"state_root","type":"bytes32"}],"name":"updateState","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes32[]","name":"content","type":"bytes32[]"},{"internalType":"bytes32[]","name":"hashes","type":"bytes32[]"},{"internalType":"bytes","name":"bitmap","type":"bytes"},{"internalType":"uint32[]","name":"depths","type":"uint32[]"}],"name":"verifyInclusionProof","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]'
    bloockchain_config.http_provider = os.environ['HOST_GANACHE_TEST']
    client.setNetworkConfiguration(Network.BLOOCK_CHAIN, bloockchain_config)
    return client


class testE2EAcceptanceBloockClient(TestCase):

    def test_basic_e2e(self):
        sdk = getSDK()
        records = [Record.fromBytes(randHex(64))]
        send_receipt = sdk.sendRecords(records)
        self.assertIsNotNone(send_receipt)
        sdk.waitAnchor(send_receipt[0].anchor)
        proof = sdk.getProof(records)
        timestamp = sdk.verifyProof(proof)
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

    #TODO: no sé si es podrà fer aquest test per assegurar que la xarxa que especifico
    #      és la xarxa on entra l'anchor
    #def test_get_proof_network_specific_okay(self):

    def test_get_proof_valid_date_filter(self):
        sdk = getSDK()
        records = [Record.fromBytes(randHex(64))]
        send_receipt = sdk.sendRecords(records)
        self.assertIsNotNone(send_receipt)
        sdk.waitAnchor(send_receipt[0].anchor)
        date = time.time()
        proof = sdk.getProof(records, date = date)
        timestamp = sdk.verifyProof(proof)
        self.assertGreater(date, timestamp, 'Date was not greater than blockchain timestamp.')

    def test_get_proof_impossible_date_filter(self):
        date = time.time()
        sdk = getSDK()
        records = [Record.fromBytes(randHex(64))]
        send_receipt = sdk.sendRecords(records)
        self.assertIsNotNone(send_receipt)
        sdk.waitAnchor(send_receipt[0].anchor)
        with self.assertRaises(Exception) as context:
            sdk.getProof(records, date = date)
        self.assertTrue("HttpClient response was not successful: Proof not found." in str(context.exception))

    def test_verify_records_valid_date_filter(self):
        sdk = getSDK()
        records = [Record.fromBytes(randHex(64))]
        send_receipt = sdk.sendRecords(records)
        self.assertIsNotNone(send_receipt)
        sdk.waitAnchor(send_receipt[0].anchor)
        date = time.time()
        timestamp = sdk.verifyRecords(records, network = Network.BLOOCK_CHAIN, date = date)
        self.assertGreater(date, timestamp, 'Date was not greater than blockchain timestamp.')

    def test_verify_records_impossible_date_filter(self):
        date = time.time()-120
        sdk = getSDK()
        records = [Record.fromBytes(randHex(64))]
        send_receipt = sdk.sendRecords(records)
        self.assertIsNotNone(send_receipt)
        sdk.waitAnchor(send_receipt[0].anchor)
        with self.assertRaises(Exception) as context:
            sdk.verifyRecords(records, network = Network.BLOOCK_CHAIN, date = date)
        self.assertTrue("HttpClient response was not successful: Proof not found." in str(context.exception))


