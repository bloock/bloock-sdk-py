from typing import List
from bloock.config.service.config_service import ConfigService
from bloock.infrastructure.http.http_client import HttpClient
from ..entity.record_receipt_entity import RecordReceipt
from ..entity.dto.record_write_response_entity import RecordWriteResponse
from ..entity.record_entity import Record


class RecordRepository:

    def __init__(self, http_client: HttpClient, config_service: ConfigService):
        self.__http_client = http_client
        self.__config_service = config_service

    def sendRecords(self, records: List[Record]) -> RecordWriteResponse:
        url = "{}/core/messages".format(self.__config_service.getApiBaseUrl())
        body = {'messages': [m.getHash() for m in records]}
        response = self.__http_client.post(url, body)
        return RecordWriteResponse(response)

    def fetchRecords(self, records: List[Record]) -> List[RecordReceipt]:
        url = "{}/core/messages/fetch".format(self.__config_service.getApiBaseUrl())
        body = {'messages': [m.getHash() for m in records]}
        response = self.__http_client.post(url, body)
        return [RecordReceipt(
            m.get('anchor', 0),
            m.get('client', ''),
            m.get('messages', ''),
            m.get('status', 'Pending')) for m in response]
