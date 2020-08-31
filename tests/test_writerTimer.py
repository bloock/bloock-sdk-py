import unittest
from unittest import mock
from unittest.mock import patch
from enchaintesdk.writerTimer import WriterTimer
from enchaintesdk.writer import Writer
import time


class MockedWriter:
    counter = 0
    __instance = None

    def __new__(self):
        self.counter = 0
        pass

    def push(self, value, resolve, reject):
        pass

    @staticmethod
    def send():
        MockedWriter.counter += 1

    @staticmethod
    def getInstance():
        return MockedWriter()


class TestWriterTimer(unittest.TestCase):

    """@mock.patch('enchaintesdk.writer.Writer')
    def test_timer(self, m):
        m.return_value = MockedWriter()
        timer = WriterTimer(0.2)
        time.sleep(1.1)
        timer.cancel()
        self.assertEqual(
            5, timer._WriterTimer__writer.counter, 'Writer.send() was not executed as many times as expected.')"""
