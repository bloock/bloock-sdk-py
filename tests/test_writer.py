import unittest
from unittest import mock
from unittest.mock import patch, MagicMock
from enchaintesdk.writer import Writer
from enchaintesdk.entity.hash import Hash
from enchaintesdk.writerTimer import WriterTimer


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

    def test_push(self):
        writer = Writer.getInstance()
        d = writer.push('element', True, False)
        self.assertTrue(d is writer._Writer__tasks['element'])
        del d
        del writer

    @ mock.patch('enchaintesdk.comms.apiService.ApiService.write', side_effect=mocked_apiservice_write)
    def test_send_success(self, mock_write):
        writer = Writer.getInstance()
        d = writer.push(
            Hash.fromHash('012c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8'), True, False)
        Writer.send()
        self.assertTrue(d.getPromise())

    @ mock.patch('enchaintesdk.comms.apiService.ApiService.write', side_effect=mocked_apiservice_write)
    def test_send_not_inserted(self, mock_write):
        writer = Writer.getInstance()
        d = writer.push(
            Hash.fromHash('112c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8'), True, False)
        Writer.send()
        self.assertFalse(d.getPromise())

    @ mock.patch('enchaintesdk.comms.apiService.ApiService.write', side_effect=mocked_apiservice_write)
    def test_send_api_exception(self, mock_write):
        writer = Writer.getInstance()
        d = writer.push(
            Hash.fromHash('212c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8'), True, False)
        Writer.send()
        self.assertFalse(d.getPromise())
