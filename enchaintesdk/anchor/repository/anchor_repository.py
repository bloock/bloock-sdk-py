from enchaintesdk.config.service.config_service import ConfigService
from enchaintesdk.infrastructure.http.http_client import HttpClient
from ..entity.dto.anchor_retrieve_response_entity import AnchorRetrieveResponse


class AnchorRepository:

    def __init__(self, http_client: HttpClient, config_service: ConfigService):
        self.__http_client = http_client
        self.__config_service = config_service

    def getAnchor(self, anchor: int) -> AnchorRetrieveResponse:
        url = f'{self.__config_service.getApiBaseUrl()}/anchors/{anchor}'
        return self.__http_client.get(url)
