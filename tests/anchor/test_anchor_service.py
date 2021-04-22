from enchaintesdk.anchor.service.anchor_service import AnchorService
from enchaintesdk.anchor.entity.anchor_entity import Anchor
from enchaintesdk.anchor.entity.anchor_entity import Anchor
from enchaintesdk.config.entity.configuration_entity import Configuration
from enchaintesdk.infrastructure.http.http_exception import HttpRequestException
from unittest import TestCase, mock
import time


class testAnchorService(TestCase):

    def sideeffect_getAnchor(self, id):
        if self.counter < self.maxCount:
            '''self.counter = self.counter+1
            return AnchorRetrieveResponse(
                1, ['block_root'], [], 'root', 'Pending')'''
            self.counter = self.counter+1
            raise HttpRequestException('anchor not ready yet')

        return Anchor(
            1, ['block_root'], [], 'root', 'Success')

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.anchor.repository.anchor_repository.AnchorRepository')
    def test_get_anchor_okay(self, MockAnchorRepo, MockConfig):
        MockAnchorRepo.getAnchor.return_value = Anchor(
            1, ['block_root'], [], 'root', 'Success')
        anchor_service = AnchorService(MockAnchorRepo, MockConfig)
        anchor = anchor_service.getAnchor(1)
        self.assertIsInstance(anchor, Anchor)
        self.assertEqual(anchor.id, 1, 'ID do not match.')
        self.assertEqual(anchor.block_roots, [
                         'block_root'], 'block_root do not match.')
        self.assertEqual(anchor.networks, [], 'networks do not match.')
        self.assertEqual(anchor.root, 'root', 'root do not match.')
        self.assertEqual(anchor.status, 'Success', 'status do not match.')

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.anchor.repository.anchor_repository.AnchorRepository')
    def test_wait_anchor_okay_first_try(self, MockAnchorRepo, MockConfig):
        self.counter = 0
        self.maxCount = 0
        MockAnchorRepo.getAnchor.side_effect = self.sideeffect_getAnchor
        anchor_service = AnchorService(MockAnchorRepo, MockConfig)
        anchor = anchor_service.waitAnchor(1, 120000)
        self.assertEqual(
            MockAnchorRepo.getAnchor.call_count, self.maxCount+1)
        self.assertIsInstance(anchor, Anchor)
        self.assertEqual(anchor.id, 1, 'ID do not match.')
        self.assertEqual(anchor.block_roots, [
                         'block_root'], 'block_root do not match.')
        self.assertEqual(anchor.networks, [], 'networks do not match.')
        self.assertEqual(anchor.root, 'root', 'root do not match.')
        self.assertEqual(anchor.status, 'Success', 'status do not match.')

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.anchor.repository.anchor_repository.AnchorRepository')
    def test_wait_anchor_okay_after_3_retries(self, MockAnchorRepo, MockConfig):
        self.counter = 0
        self.maxCount = 3
        config = Configuration()
        config.wait_message_interval_default = 1000
        MockConfig.getConfiguration.return_value = config
        MockAnchorRepo.getAnchor.side_effect = self.sideeffect_getAnchor
        anchor_service = AnchorService(MockAnchorRepo, MockConfig)
        start = time.time()
        anchor = anchor_service.waitAnchor(1, timeout=120000)
        finish = time.time()
        print(finish-start)
        self.assertIsInstance(anchor, Anchor)
        self.assertEqual(
            MockAnchorRepo.getAnchor.call_count, self.maxCount+1)
        self.assertIsInstance(anchor, Anchor)
        self.assertEqual(anchor.id, 1, 'ID do not match.')
        self.assertEqual(anchor.block_roots, [
                         'block_root'], 'block_root do not match.')
        self.assertEqual(anchor.networks, [], 'networks do not match.')
        self.assertEqual(anchor.root, 'root', 'root do not match.')
        self.assertEqual(anchor.status, 'Success', 'status do not match.')
        self.assertGreater(finish-start, 4, 'Everyting went too fast.')
        self.assertGreater(4.25, finish-start, 'Everyting went too slow.')

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.anchor.repository.anchor_repository.AnchorRepository')
    def test_wait_anchor_timeout(self, MockAnchorRepo, MockConfig):
        self.counter = 0
        self.maxCount = 3
        config = Configuration()
        config.wait_message_interval_default = 1
        MockConfig.getConfiguration.return_value = config

        MockAnchorRepo.getAnchor.side_effect = self.sideeffect_getAnchor
        anchor_service = AnchorService(MockAnchorRepo, MockConfig)
        anchor = anchor_service.waitAnchor(1, timeout=1)
        self.assertIsNone(anchor)
