from unittest import TestCase
from unittest import TestCase, mock
from bloock.record.entity.record_entity import Record
from bloock.record.entity.record_receipt_entity import RecordReceipt
from bloock.record.entity.dto.record_write_response_entity import RecordWriteResponse
from bloock.record.repository.record_repository import RecordRepository
from bloock.infrastructure.http.dto.api_response_entity import ApiResponse


class RecordRepositoryTestCase(TestCase):

    @mock.patch('bloock.config.service.config_service.ConfigService')
    @mock.patch('bloock.infrastructure.http.http_client.HttpClient')
    def test_send_records_okay(self, MockHttpClient, MockConfigService):
        MockHttpClient.post.return_value = {
            'anchor': 80,
            'client': 'ce10c769-022b-405e-8e7c-3b52eeb2a4ea',
            'messages': ['02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5'],
            'status': 'Pending'}
        MockConfigService.getApiBaseUrl.return_value = "api url"
        m_repo = RecordRepository(MockHttpClient, MockConfigService)
        r = m_repo.sendRecords([])
        self.assertIsInstance(r, RecordWriteResponse, "Wrong return type")
        self.assertEqual(r.anchor, 80, 'Wrong anchor')
        self.assertEqual(
            r.client, 'ce10c769-022b-405e-8e7c-3b52eeb2a4ea', 'Wrong client')
        self.assertEqual(r.records, [
                         '02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5'], 'Wrong records')
        self.assertEqual(r.status, 'Pending', 'Wrong anchor')

    @mock.patch('bloock.config.service.config_service.ConfigService')
    @mock.patch('bloock.infrastructure.http.http_client.HttpClient')
    def test_send_records_okay_but_empty_fields(self, MockHttpClient, MockConfigService):
        MockHttpClient.post.return_value = {}
        MockConfigService.getApiBaseUrl.return_value = "api url"
        m_repo = RecordRepository(MockHttpClient, MockConfigService)
        r = m_repo.sendRecords([])
        self.assertIsInstance(r, RecordWriteResponse, "Wrong return type")
        self.assertEqual(r.anchor, 0, 'Wrong anchor')
        self.assertEqual(
            r.client, '', 'Wrong client')
        self.assertEqual(r.records, [], 'Wrong records')
        self.assertEqual(r.status, '', 'Wrong anchor')

    @mock.patch('bloock.config.service.config_service.ConfigService')
    @mock.patch('bloock.infrastructure.http.http_client.HttpClient')
    def test_fetch_records_okay(self, MockHttpClient, MockConfigService):
        MockHttpClient.post.return_value = [{
            'anchor': 80,
            'client': 'ce10c769-022b-405e-8e7c-3b52eeb2a4ea',
            'messages': ['02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5'],
            'status': 'Pending'}]
        MockConfigService.getApiBaseUrl.return_value = "api url"
        m_repo = RecordRepository(MockHttpClient, MockConfigService)
        r = m_repo.fetchRecords([])
        self.assertIsInstance(r[0], RecordReceipt, "Wrong return type")
        self.assertEqual(r[0].anchor, 80, 'Wrong anchor')
        self.assertEqual(
            r[0].client, 'ce10c769-022b-405e-8e7c-3b52eeb2a4ea', 'Wrong client')
        self.assertEqual(r[0].record, [
                         '02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5'], 'Wrong records')
        self.assertEqual(r[0].status, 'Pending', 'Wrong anchor')

    @mock.patch('bloock.config.service.config_service.ConfigService')
    @mock.patch('bloock.infrastructure.http.http_client.HttpClient')
    def test_fetch_records_okay_but_empty_fields(self, MockHttpClient, MockConfigService):
        MockHttpClient.post.return_value = [{
            'anchor': None,
            'client': None,
            'record': None,
            'status': None}]
        MockConfigService.getApiBaseUrl.return_value = "api url"
        m_repo = RecordRepository(MockHttpClient, MockConfigService)
        r = m_repo.fetchRecords([])
        self.assertIsInstance(r[0], RecordReceipt, "Wrong return type")
        self.assertEqual(r[0].anchor, 0, 'Wrong anchor')
        self.assertEqual(
            r[0].client, '', 'Wrong client')
        self.assertEqual(r[0].record, '', 'Wrong records')
        self.assertEqual(r[0].status, 'Pending', 'Wrong anchor')
