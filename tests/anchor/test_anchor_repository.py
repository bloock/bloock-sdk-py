from bloock.anchor.repository.anchor_repository import AnchorRepository
from bloock.anchor.entity.anchor_entity import Anchor
from bloock.infrastructure.http.dto.api_response_entity import ApiResponse
from unittest import TestCase, mock


class testAnchorRepository(TestCase):

    @mock.patch('bloock.config.service.config_service.ConfigService')
    @mock.patch('bloock.infrastructure.http.http_client.HttpClient')
    def test_get_anchor_okay(self, MockHttpClient, MockConfig):
        MockConfig.getApiBaseUrl.returning("i'm definitely a URL")
        MockHttpClient.get.return_value = {
            'anchor_id': 1,
            'block_roots': ['block_root'],
            'networks': [],
            'root': 'root',
            'status': 'Success'
        }
        anchor_repo = AnchorRepository(MockHttpClient, MockConfig)
        anchor = anchor_repo.getAnchor(1)
        self.assertIsInstance(anchor, Anchor,
                              'Returning incorrect instance of object.')
        self.assertEqual(anchor.id, 1, 'ID do not match.')
        self.assertEqual(anchor.block_roots, [
                         'block_root'], 'block_root do not match.')
        self.assertEqual(anchor.networks, [], 'networks do not match.')
        self.assertEqual(anchor.root, 'root', 'networks do not match.')
        self.assertEqual(anchor.status, 'Success', 'networks do not match.')
