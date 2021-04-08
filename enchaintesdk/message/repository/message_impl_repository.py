from enchaintesdk.config.service.config_service import ConfigService
from enchaintesdk.infrastructure.http_client import HttpClient
from ..entity.dto.message_retrieve_request_entity import MessageRetrieveRequest
from ..entity.dto.message_retrieve_response_entity import MessageRetrieveResponse
from ..entity.dto.message_write_request_entity import MessageWriteRequest
from ..entity.dto.message_write_response_entity import MessageWriteResponse
from ..entity.message_entity import Message
from .message_repository import MessageRepository


class MessageRepositoryImpl (MessageRepository):

    def __init__(self, http_client: HttpClient, config_service: ConfigService):
        self.__http_client = http_client
        self.__config_service = config_service

    def sendMessages(self, messages: [Message]) -> MessageWriteResponse:
        url = "{}/messages".format(self.__config_service.getApiBaseUrl())
        body = MessageWriteRequest([m.getHash() for m in messages])
        return self.__http_client.post(url, body)

    def fetchMessages(self, messages: [Message]) -> [MessageRetrieveResponse]:
        url = "{}/messages/fetch".format(self.__config_service.getApiBaseUrl())
        body = MessageRetrieveRequest([m.getHash() for m in messages])
        return self.__http_client.post(url, body)
