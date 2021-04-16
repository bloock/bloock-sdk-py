from enchaintesdk.config.service.config_service import ConfigService
from enchaintesdk.infrastructure.http.http_client import HttpClient
from ..entity.anchor_entity import Anchor
from enchaintesdk.infrastructure.http.dto.api_response_entity import ApiResponse


class AnchorRepository:

    def __init__(self, http_client: HttpClient, config_service: ConfigService):
        self.__http_client = http_client
        self.__config_service = config_service

    def getAnchor(self, anchor: int) -> Anchor:
        url = f'{self.__config_service.getApiBaseUrl()}/anchors/{anchor}'
        r = self.__http_client.get(url)
        return Anchor(
            r.data['anchor_id'],
            r.data['block_roots'],
            r.data['networks'],
            r.data['root'],
            r.data['status'])
