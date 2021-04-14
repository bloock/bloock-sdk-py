from unittest import TestCase
from unittest import TestCase, mock
from enchaintesdk.message.entity.message_entity import Message
from enchaintesdk.message.repository.message_repository import MessageRepository
import numpy as np


class MessageRepositoryTestCase(TestCase):

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.infrastructure.http.http_client.HttpClient')
    def test_send_messages_okay(self, MockHttpClient, MockConfigService):
        MockHttpClient.post.return_value = "Post_return value"
        MockConfigService.getApiBaseUrl.return_value = "api url"
        m_repo = MessageRepository(MockHttpClient, MockConfigService)
        self.assertEqual(m_repo.sendMessages([]), "Post_return value")

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.infrastructure.http.http_client.HttpClient')
    def test_send_messages_raise_exception(self, MockHttpClient, MockConfigService):
        MockHttpClient.post.return_value = "Post_return value"
        MockConfigService.getApiBaseUrl.return_value = "api url"
        m_repo = MessageRepository(MockHttpClient, MockConfigService)
        self.assertEqual(m_repo.sendMessages([]), "Post_return value")
