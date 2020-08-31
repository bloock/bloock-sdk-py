import unittest
from unittest import mock
from unittest.mock import patch
import enchaintesdk.enchainteClient as ensdk
from enchaintesdk.entity.hash import Hash
from enchaintesdk.utils.constants import SEND_INTERVAL
from enchaintesdk.comms.apiService import ApiService


class mock_ApiService:
    apiKey = ""

    @staticmethod
    def getProof(dataH):
        data = [x.getHash() for x in dataH]
        if data == ['hash1', 'hash2']:
            return True
        raise BaseException('Api error during get proof')

    """@staticmethod
    def getMessages(dataH):

    """


def mocked_timer(seconds):
    pass


def mocked_writer_getInstance():
    class subscription:
        def __init__(self):
            pass

        def push(self, hs, t, f):
            return True

    return subscription()


class mock_Hash:
    def __init__(self, dataString):
        self._hash = dataString

    def getHash(self):
        return self._hash

    @staticmethod
    def fromHash(data):
        return mock_Hash(data)

    @staticmethod
    def sort(hashes):
        return hashes


class TestEnchainteClient(unittest.TestCase):

    """@mock.patch('enchaintesdk.writerTimer.WriterTimer.__init__', side_effect=mocked_timer)
    @mock.patch('enchaintesdk.comms.apiService.ApiService')
    def test_init(self, mock_Api, mock_WriterTimer):
        mock_Api.return_value = mock_ApiService()
        sdk = ensdk.EnchainteClient('apiKey')
        self.assertEqual(
            ApiService.apiKey, 'apiKey')
        self.assertEqual(sdk.apiKey, 'apiKey')

    @mock.patch('enchaintesdk.entity.hash.Hash')
    @mock.patch('enchaintesdk.writer.Writer.getInstance', side_effect=mocked_writer_getInstance)
    @mock.patch('enchaintesdk.writerTimer.WriterTimer.__init__', side_effect=mocked_timer)
    @mock.patch('enchaintesdk.comms.apiService.ApiService')
    def test_write_success(self, mockApi, mockWriterTimer, mockWriter, mockHash):
        mock_api = mock_ApiService()
        mockApi.return_value = mock_api
        mock_hash = mock_Hash('hash')
        mockHash.return_value = mock_hash
        sdk = ensdk.EnchainteClient('apiKey')
        pushed = sdk.write('hash', 'hash')
        self.assertTrue(pushed)

    @mock.patch('enchaintesdk.entity.hash.Hash')
    @mock.patch('enchaintesdk.writer.Writer.getInstance', side_effect=mocked_writer_getInstance)
    @mock.patch('enchaintesdk.writerTimer.WriterTimer.__init__', side_effect=mocked_timer)
    @mock.patch('enchaintesdk.comms.apiService.ApiService')
    def test_write_hash_exception(self, mockApi, mockWriterTimer, mockWriter, mockHash):
        mock_api = mock_ApiService()
        mockApi.return_value = mock_api
        mock_hash = mock_Hash('hash')
        mockHash.return_value = mock_hash
        sdk = ensdk.EnchainteClient('apiKey')
        self.assertRaises(BaseException, sdk.write, ['hash', 'hahs'])

    @mock.patch('enchaintesdk.entity.hash.Hash')
    @mock.patch('enchaintesdk.writerTimer.WriterTimer.__init__', side_effect=mocked_timer)
    @mock.patch('enchaintesdk.comms.apiService.ApiService')
    def test_getProof_success(self, mockApi, mockWriterTimer, mockHash):
        mockApi.return_value = mock_ApiService
        mockHash.return_value = mock_Hash
        sdk = ensdk.EnchainteClient('apiKey')
        self.assertTrue(sdk.getProof(
            [mock_Hash.fromHash('hash1'), mock_Hash.fromHash('hash2')]))

    def test_getProof_hash_exception:

    def test_getProof_api_exception:

    def test_verify_success:

    def test_verify_proof_error:

    def test_verify_web3_exception:

    def test_getMessages_success:

    def test_getMessages_proof_error:

    def test_getMessages_web3_exception:"""
