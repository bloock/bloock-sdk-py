import unittest
from unittest import mock
import numpy as np
from requests.exceptions import RequestException
from enchaintesdk.comms.configService import ConfigService
from enchaintesdk.entity.message import Message

class TestConfigService(unittest.TestCase):
    def test_send_success(self):
        conf = ConfigService()
        c =  conf.getConfig()
        self.assertNotEqual(c, None)
        self.assertNotEqual(c.provider, None)