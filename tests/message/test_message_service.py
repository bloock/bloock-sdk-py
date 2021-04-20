from unittest import TestCase, mock
from enchaintesdk.message.entity.message_entity import Message
from enchaintesdk.message.entity.message_receipt_entity import MessageReceipt
from enchaintesdk.message.entity.exception.invalid_message_exception import InvalidMessageException
from enchaintesdk.message.entity.dto.message_write_response_entity import MessageWriteResponse
from enchaintesdk.message.service.message_service import MessageService
from enchaintesdk.message.repository.message_repository import MessageRepository


class MessageServiceTestCase(TestCase):

    @mock.patch('enchaintesdk.message.entity.message_entity.Message.isValid')
    @mock.patch('enchaintesdk.message.repository.message_repository.MessageRepository')
    def test_send_messages_okay(self, MockMessageRepo, MockMessage):
        MockMessageRepo.sendMessages.return_value = MessageWriteResponse({
            'anchor': 80,
            'client': 'ce10c769-022b-405e-8e7c-3b52eeb2a4ea',
            'messages': ['02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5'],
            'status': 'Pending'})
        MockMessage.return_value = True
        m_repo = MessageService(MockMessageRepo)
        r = m_repo.sendMessages([Message('message')])
        self.assertIsInstance(r[0], MessageReceipt, "Wrong return type")
        self.assertEqual(r[0].anchor, 80, 'Wrong anchor')
        self.assertEqual(
            r[0].client, 'ce10c769-022b-405e-8e7c-3b52eeb2a4ea', 'Wrong client')
        self.assertEqual(r[0].message,
                         '02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5', 'Wrong messages')
        self.assertEqual(r[0].status, 'Pending', 'Wrong anchor')

    @mock.patch('enchaintesdk.message.entity.message_entity.Message.isValid')
    @mock.patch('enchaintesdk.message.repository.message_repository.MessageRepository')
    def test_send_messages_some_invalid_message_error(self, MockMessageRepo, MockMessage):
        MockMessageRepo.sendMessages.return_value = MessageWriteResponse({
            'anchor': 80,
            'client': 'ce10c769-022b-405e-8e7c-3b52eeb2a4ea',
            'messages': ['02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5', 'message2', ''],
            'status': 'Pending'})
        MockMessage.return_value = False
        m_repo = MessageService(MockMessageRepo)
        with self.assertRaises(InvalidMessageException):
            m_repo.sendMessages([Message('message')])

    @mock.patch('enchaintesdk.message.repository.message_repository.MessageRepository')
    def test_get_messages_okay(self, MockMessageRepo):
        MockMessageRepo.fetchMessages.return_value = [MessageReceipt(80,
                                                                     'ce10c769-022b-405e-8e7c-3b52eeb2a4ea',
                                                                     '02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5',
                                                                     'Pending')]
        m_service = MessageService(MockMessageRepo)
        r = m_service.getMessages(
            [Message('02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5')])
        self.assertEqual(r[0].anchor, 80, 'Wrong anchor')
        self.assertEqual(
            r[0].client, 'ce10c769-022b-405e-8e7c-3b52eeb2a4ea', 'Wrong client')
        self.assertEqual(
            r[0].message, '02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5', 'Wrong messages')
        self.assertEqual(r[0].status, 'Pending', 'Wrong anchor')
