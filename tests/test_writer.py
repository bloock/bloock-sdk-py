import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
from enchaintesdk.writer import Writer
from enchaintesdk.entity.message import Message
import time

class TestWriter(unittest.TestCase):
    checker = [None]

    @staticmethod
    def resolve():
        TestWriter.checker[0] = True

    @staticmethod
    def reject(e):
        TestWriter.checker[0] = False
    
    @staticmethod
    def mocked_apiservice_write(data):
        if data[0].getMessage() == '012c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8':
            return ['012c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8']
        elif data[0].getMessage() == '112c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8':
            return []
        else:
            raise BaseException("Any api exception")

    def test_getInstance(self):
        writer = Writer.getInstance()
        writer.custom = True
        writer2 = Writer.getInstance()
        self.assertTrue(writer2.custom)
        del writer
        del writer2

    """
    @ mock.patch('enchaintesdk.comms.apiService.ApiService.write', side_effect=mocked_apiservice_write)
    def test_send_success(self, mock_write):
        writer = Writer.getInstance()
        writer.push(
            Message.fromMessage('012c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8'),
            TestWriter.resolve, 
            TestWriter.reject)
        Writer.send()
        time.sleep(2)
        self.assertTrue(TestWriter.checker[0])
        self.checker[0] = None
    
    @ mock.patch('enchaintesdk.comms.apiService.ApiService.write', side_effect=mocked_apiservice_write)
    def test_send_not_inserted(self, mock_write):
        global checker
        writer = Writer.getInstance()
        writer.push(
            Message.fromMessage('112c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8'),
            resolve, 
            reject)
        Writer.send()
        self.assertFalse(checker)

    @ mock.patch('enchaintesdk.comms.apiService.ApiService.write', side_effect=mocked_apiservice_write)
    def test_send_api_exception(self, mock_write):
        global checker
        writer = Writer.getInstance()
        writer.push(
            Message.fromMessage('212c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8'),
            resolve, 
            reject)
        Writer.send()
        self.assertFalse(checker)
    """