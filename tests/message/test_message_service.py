from unittest import TestCase, mock
from bloock.record.entity.record_entity import Record
from bloock.record.entity.record_receipt_entity import RecordReceipt
from bloock.record.entity.exception.invalid_record_exception import InvalidRecordException
from bloock.record.entity.dto.record_write_response_entity import RecordWriteResponse
from bloock.record.service.record_service import RecordService
from bloock.record.repository.record_repository import RecordRepository


class RecordServiceTestCase(TestCase):

    @mock.patch('bloock.record.entity.record_entity.Record.isValid')
    @mock.patch('bloock.record.repository.record_repository.RecordRepository')
    def test_send_records_okay(self, MockRecordRepo, MockRecord):
        MockRecordRepo.sendRecords.return_value = RecordWriteResponse({
            'anchor': 80,
            'client': 'ce10c769-022b-405e-8e7c-3b52eeb2a4ea',
            'messages': ['02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5'],
            'status': 'Pending'})
        MockRecord.return_value = True
        m_repo = RecordService(MockRecordRepo)
        r = m_repo.sendRecords([Record('record')])
        self.assertIsInstance(r[0], RecordReceipt, "Wrong return type")
        self.assertEqual(r[0].anchor, 80, 'Wrong anchor')
        self.assertEqual(
            r[0].client, 'ce10c769-022b-405e-8e7c-3b52eeb2a4ea', 'Wrong client')
        self.assertEqual(r[0].record,
                         '02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5', 'Wrong records')
        self.assertEqual(r[0].status, 'Pending', 'Wrong anchor')

    @mock.patch('bloock.record.entity.record_entity.Record.isValid')
    @mock.patch('bloock.record.repository.record_repository.RecordRepository')
    def test_send_records_some_invalid_record_error(self, MockRecordRepo, MockRecord):
        MockRecordRepo.sendRecords.return_value = RecordWriteResponse({
            'anchor': 80,
            'client': 'ce10c769-022b-405e-8e7c-3b52eeb2a4ea',
            'records': ['02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5', 'record2', ''],
            'status': 'Pending'})
        MockRecord.return_value = False
        m_repo = RecordService(MockRecordRepo)
        with self.assertRaises(InvalidRecordException):
            m_repo.sendRecords([Record('record')])

    @mock.patch('bloock.record.repository.record_repository.RecordRepository')
    def test_get_records_okay(self, MockRecordRepo):
        MockRecordRepo.fetchRecords.return_value = [RecordReceipt(80,
                                                                     'ce10c769-022b-405e-8e7c-3b52eeb2a4ea',
                                                                     '02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5',
                                                                     'Pending')]
        m_service = RecordService(MockRecordRepo)
        r = m_service.getRecords(
            [Record('02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5')])
        self.assertEqual(r[0].anchor, 80, 'Wrong anchor')
        self.assertEqual(
            r[0].client, 'ce10c769-022b-405e-8e7c-3b52eeb2a4ea', 'Wrong client')
        self.assertEqual(
            r[0].record, '02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5', 'Wrong records')
        self.assertEqual(r[0].status, 'Pending', 'Wrong anchor')
