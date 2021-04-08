from ..entity.message_entity import Message
from ..entity.dto.message_retrieve_response_entity import MessageRetrieveResponse
from ..entity.dto.message_write_response_entity import MessageWriteResponse


class MessageRepository:
    def sendMessages(self, messages: [Message]) -> MessageWriteResponse:
        pass

    def fetchMessages(self, messages: [Message]) -> [MessageRetrieveResponse]:
        pass
