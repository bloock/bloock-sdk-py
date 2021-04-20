from unittest import TestCase
from unittest import TestCase, mock
from enchaintesdk.message.entity.message_entity import Message
from enchaintesdk.message.entity.message_receipt_entity import MessageReceipt
from enchaintesdk.message.entity.dto.message_write_response_entity import MessageWriteResponse
from enchaintesdk.message.repository.message_repository import MessageRepository
from enchaintesdk.infrastructure.http.dto.api_response_entity import ApiResponse


class MessageRepositoryTestCase(TestCase):

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.infrastructure.http.http_client.HttpClient')
    def test_send_messages_okay(self, MockHttpClient, MockConfigService):
        MockHttpClient.post.return_value = ApiResponse({'data': {
            'anchor': 80,
            'client': 'ce10c769-022b-405e-8e7c-3b52eeb2a4ea',
            'messages': ['02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5'],
            'status': 'Pending'},
            'success': True})
        MockConfigService.getApiBaseUrl.return_value = "api url"
        m_repo = MessageRepository(MockHttpClient, MockConfigService)
        r = m_repo.sendMessages([])
        self.assertIsInstance(r, MessageWriteResponse, "Wrong return type")
        self.assertEqual(r.anchor, 80, 'Wrong anchor')
        self.assertEqual(
            r.client, 'ce10c769-022b-405e-8e7c-3b52eeb2a4ea', 'Wrong client')
        self.assertEqual(r.message, [
                         '02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5'], 'Wrong messages')
        self.assertEqual(r.status, 'Pending', 'Wrong anchor')

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.infrastructure.http.http_client.HttpClient')
    def test_send_messages_okay_but_empty_fields(self, MockHttpClient, MockConfigService):
        MockHttpClient.post.return_value = ApiResponse({'data': {},
                                                        'success': True})
        MockConfigService.getApiBaseUrl.return_value = "api url"
        m_repo = MessageRepository(MockHttpClient, MockConfigService)
        r = m_repo.sendMessages([])
        self.assertIsInstance(r, MessageWriteResponse, "Wrong return type")
        self.assertEqual(r.anchor, 0, 'Wrong anchor')
        self.assertEqual(
            r.client, '', 'Wrong client')
        self.assertEqual(r.message, [], 'Wrong messages')
        self.assertEqual(r.status, '', 'Wrong anchor')

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.infrastructure.http.http_client.HttpClient')
    def test_fetch_messages_okay(self, MockHttpClient, MockConfigService):
        MockHttpClient.post.return_value = ApiResponse({'data': [{
            'anchor': 80,
            'client': 'ce10c769-022b-405e-8e7c-3b52eeb2a4ea',
            'message': ['02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5'],
            'status': 'Pending'}],
            'success': True})
        MockConfigService.getApiBaseUrl.return_value = "api url"
        m_repo = MessageRepository(MockHttpClient, MockConfigService)
        r = m_repo.fetchMessages([])
        self.assertIsInstance(r[0], MessageReceipt, "Wrong return type")
        self.assertEqual(r[0].anchor, 80, 'Wrong anchor')
        self.assertEqual(
            r[0].client, 'ce10c769-022b-405e-8e7c-3b52eeb2a4ea', 'Wrong client')
        self.assertEqual(r[0].message, [
                         '02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5'], 'Wrong messages')
        self.assertEqual(r[0].status, 'Pending', 'Wrong anchor')

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.infrastructure.http.http_client.HttpClient')
    def test_fetch_messages_okay_but_empty_fields(self, MockHttpClient, MockConfigService):
        MockHttpClient.post.return_value = ApiResponse({'data': [{
            'anchor': None,
            'client': None,
            'message': None,
            'status': None}],
            'success': True})
        MockConfigService.getApiBaseUrl.return_value = "api url"
        m_repo = MessageRepository(MockHttpClient, MockConfigService)
        r = m_repo.fetchMessages([])
        self.assertIsInstance(r[0], MessageReceipt, "Wrong return type")
        self.assertEqual(r[0].anchor, 0, 'Wrong anchor')
        self.assertEqual(
            r[0].client, '', 'Wrong client')
        self.assertEqual(r[0].message, '', 'Wrong messages')
        self.assertEqual(r[0].status, 'Pending', 'Wrong anchor')
