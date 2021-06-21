from typing import List
from enchaintesdk.config.service.config_service import ConfigService
from enchaintesdk.infrastructure.http.http_client import HttpClient
from ..entity.message_receipt_entity import MessageReceipt
from ..entity.dto.message_write_response_entity import MessageWriteResponse
from ..entity.message_entity import Message


class MessageRepository:

    def __init__(self, http_client: HttpClient, config_service: ConfigService):
        self.__http_client = http_client
        self.__config_service = config_service

    def sendMessages(self, messages: List[Message]) -> MessageWriteResponse:
        url = "{}/core/messages".format(self.__config_service.getApiBaseUrl())
        body = {'messages': [m.getHash() for m in messages]}
        response = self.__http_client.post(url, body)
        return MessageWriteResponse(response)

    def fetchMessages(self, messages: List[Message]) -> List[MessageReceipt]:
        url = "{}/core/messages/fetch".format(self.__config_service.getApiBaseUrl())
        body = {'messages': [m.getHash() for m in messages]}
        response = self.__http_client.post(url, body)
        return [MessageReceipt(
            m.get('anchor', 0),
            m.get('client', ''),
            m.get('message', ''),
            m.get('status', 'Pending')) for m in response]
