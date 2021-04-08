from unittest import TestCase
from enchaintesdk.infrastructure.http.http_data import HttpData
from enchaintesdk.infrastructure.http.http_impl import HttpClientImpl
from enchaintesdk.infrastructure.http.dto.api_response_entity import ApiResponse


class HttpClientImplTestCase(TestCase):
    def setUp(self):
        self.http_data = HttpData(api_key='test_api_key')

    def test_http_client_impl_init(self):
        self.assertEqual(HttpClientImpl(
            self.http_data)._HttpClientImpl__http_data.api_key,
            'test_api_key',
            "ApiKey values differs from the expected one")

    def test_http_client_impl_set_api_key(self):
        new_api_key = 'definetly_not_a_test_api_key'
        hci = HttpClientImpl(self.http_data)
        hci.setApiKey(new_api_key)
        self.assertEqual(hci._HttpClientImpl__http_data.api_key,
                         new_api_key,
                         "ApiKey values differs from the expected one")
