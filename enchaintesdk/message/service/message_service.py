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

        r = self.__message_repo.sendMessages(messages)
        return [MessageReceipt(r.anchor, r.client, m, r.status) for m in r.message]

    def getMessages(self, messages: [Message]) -> [MessageReceipt]:
        if (len(messages) == 0):
            return []

        for m in messages:
            if not Message.isValid(m):
                raise InvalidMessageException(m.getHash())
        return self.__message_repo.fetchMessages(messages)
