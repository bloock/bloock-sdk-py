import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
from enchaintesdk.writer import Writer
from enchaintesdk.entity.hash import Hash
from enchaintesdk.writerTimer import WriterTimer

checker = None

def resolve():
    global checker
    checker = True

def reject(e):
    global checker
    checker = False

def mocked_apiservice_write(data):
    if data[0].getHash() == '012c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8':
        return ['012c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8']
    elif data[0].getHash() == '112c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8':
        return []
    else:
        raise BaseException("Any api exception")


def mocked_setinterval_init(b, writer):
    return


class TestWriter(unittest.TestCase):
    
    def test_getInstance(self):
        writer = Writer.getInstance()
        writer.custom = True
        writer2 = Writer.getInstance()
        self.assertTrue(writer2.custom)
        del writer
        del writer2

    @ mock.patch('enchaintesdk.comms.apiService.ApiService.write', side_effect=mocked_apiservice_write)
    def test_send_success(self, mock_write):
        global checker
        writer = Writer.getInstance()
        writer.push(
            Hash.fromHash('012c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8'),
            resolve, 
            reject)
        Writer.send()
        self.assertTrue(checker)
        checker = None

    @ mock.patch('enchaintesdk.comms.apiService.ApiService.write', side_effect=mocked_apiservice_write)
    def test_send_not_inserted(self, mock_write):
        global checker
        writer = Writer.getInstance()
        writer.push(
            Hash.fromHash('112c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8'),
            resolve, 
            reject)
        Writer.send()
        self.assertFalse(checker)

    @ mock.patch('enchaintesdk.comms.apiService.ApiService.write', side_effect=mocked_apiservice_write)
    def test_send_api_exception(self, mock_write):
        global checker
        writer = Writer.getInstance()
        writer.push(
            Hash.fromHash('212c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8'),
            resolve, 
            reject)
        Writer.send()
        self.assertFalse(checker)
