from ..entity.exception.invalid_message_exception import InvalidMessageException
from ..entity.message_receipt_entity import MessageReceipt
from ..entity.message_entity import Message
from ..repository.message_repository import MessageRepository


class MessageService:

    def __init__(self, message_repository: MessageRepository):
        self.__message_repo = message_repository

    def sendMessages(self, messages: [Message]) -> [MessageReceipt]:
        if (len(messages) == 0):
            return []

        for m in messages:
            if not Message.isValid(m):
                raise InvalidMessageException(m.getHash())

        response = self.__message_repo.sendMessages(messages)

        result = []
        if response.data['anchor'] == None:
            response.data['anchor'] = 0
        if response.data['client'] == None:
            response.data['client'] = ""
        if response.data['status'] == None:
            response.data['status'] = ""

        for m in messages:
            result.append(MessageReceipt(
                response.data['anchor'],
                response.data['client'],
                m.getHash(),
                response.data['status']
            ))

        return result

    def getMessages(self, messages: [Message]) -> [MessageReceipt]:
        response = self.__message_repo.fetchMessages(messages)
        if response == None:
            return []

        result = []
        for m in response.data:
            if m['anchor'] == None:
                m['anchor'] = 0
            if m['client'] == None:
                m['client'] = ""
            if m['message'] == None:
                m['message'] = ""
            if m['status'] == None:
                m['status'] = ""
            result.append(MessageReceipt(
                m['anchor'], m['client'], m['message'], m['status']))
        return result
