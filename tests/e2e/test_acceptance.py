import os
import binascii
from unittest import TestCase
from enchaintesdk.infrastructure.http.http_exception import HttpRequestException
from enchaintesdk.infrastructure.http.http_data import HttpData
from enchaintesdk.infrastructure.http.http_client import HttpClient
from enchaintesdk.enchainte_client import EnchainteClient
from enchaintesdk.message.entity.message_entity import Message
from enchaintesdk.anchor.entity.anchor_entity import Anchor
from enchaintesdk.proof.entity.proof_entity import Proof
from enchaintesdk.exceptions import InvalidMessageException
from enchaintesdk.config.entity.config_env_entity import ConfigEnv


def randHex(len: int) -> bytes:
    return binascii.b2a_hex(os.urandom(len))


def getSDK():
    api_key = os.environ['API_KEY']
    return EnchainteClient(api_key, ConfigEnv.TEST)


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

    def test_send_messages_invalid_message_input_wrong_char(self):
        sdk = getSDK()
        messages = [Message(
            'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aG')]
        with self.assertRaises(InvalidMessageException):
            sdk.sendMessages(messages)

    def test_send_messages_invalid_message_input_missing_chars(self):
        sdk = getSDK()
        messages = [Message(
            'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aa'),
            Message('e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994')]
        with self.assertRaises(InvalidMessageException):
            sdk.sendMessages(messages)

    def test_send_messages_invalid_message_input_wrong_start(self):
        sdk = getSDK()
        messages = [Message(
            '0xe016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aa'),
            Message('0xe016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994bb')]
        with self.assertRaises(InvalidMessageException):
            sdk.sendMessages(messages)

    def test_send_messages_invalid_message_input_string(self):
        sdk = getSDK()
        messages = [
            'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aa']
        with self.assertRaises(AttributeError):
            sdk.sendMessages(messages)

    def test_send_messages_empty_message_input(self):
        sdk = getSDK()
        self.assertEqual(sdk.sendMessages([]), [])

    def test_get_messages_invalid_message_input_wrong_char(self):
        sdk = getSDK()
        messages = [Message(
            'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aG')]
        with self.assertRaises(InvalidMessageException):
            sdk.getMessages(messages)

    def test_get_messages_invalid_message_input_missing_chars(self):
        sdk = getSDK()
        messages = [Message(
            'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aa'),
            Message('e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994')]
        with self.assertRaises(InvalidMessageException):
            sdk.getMessages(messages)

    def test_get_messages_invalid_message_input_wrong_start(self):
        sdk = getSDK()
        messages = [Message(
            '0xe016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aa'),
            Message('0xe016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994bb')]
        with self.assertRaises(InvalidMessageException):
            sdk.getMessages(messages)

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

    def test_get_proof_invalid_message_input_wrong_char(self):
        sdk = getSDK()
        messages = [Message(
            'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aG')]
        with self.assertRaises(InvalidMessageException):
            sdk.getProof(messages)

    def test_get_proof_invalid_message_input_missing_chars(self):
        sdk = getSDK()
        messages = [Message(
            'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aa'),
            Message('e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994')]
        with self.assertRaises(InvalidMessageException):
            sdk.getProof(messages)

    def test_get_proof_invalid_message_input_wrong_start(self):
        sdk = getSDK()
        messages = [Message(
            '0xe016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aa'),
            Message('0xe016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994bb')]
        with self.assertRaises(InvalidMessageException):
            sdk.getProof(messages)

    def test_get_proof_empty_message_input(self):
        sdk = getSDK()
        self.assertEqual(sdk.getProof([]), None)

    def test_get_proof_none_existing_leaf(self):
        sdk = getSDK()
        with self.assertRaises(HttpRequestException):
            sdk.getProof(
                [Message('0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef')])

    def test_verify_messages_invalid_message_input_wrong_char(self):
        sdk = getSDK()
        messages = [Message(
            'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aG')]
        with self.assertRaises(InvalidMessageException):
            sdk.verifyMessages(messages)

    def test_verify_messages_invalid_message_input_missing_chars(self):
        sdk = getSDK()
        messages = [Message(
            'e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aa'),
            Message('e016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994')]
        with self.assertRaises(InvalidMessageException):
            sdk.verifyMessages(messages)

    def test_verify_messages_invalid_message_input_wrong_start(self):
        sdk = getSDK()
        messages = [Message(
            '0xe016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994aa'),
            Message('0xe016214a5c4abb88b8b614a916b1a6f075dfcf6fbc16c1e9d6e8ebcec81994bb')]
        with self.assertRaises(InvalidMessageException):
            sdk.verifyMessages(messages)

    def test_verify_messages_empty_message_input(self):
        sdk = getSDK()
        self.assertEqual(sdk.verifyMessages([]), None)

    def test_verify_messages_none_existing_leaf(self):
        sdk = getSDK()
        with self.assertRaises(HttpRequestException):
            sdk.verifyMessages(
                [Message('0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef')])
