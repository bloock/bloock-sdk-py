from bloock.config.service.config_service import ConfigService
from bloock.infrastructure.http.http_client import HttpClient
from ..entity.anchor_entity import Anchor
from bloock.infrastructure.http.dto.api_response_entity import ApiResponse


class AnchorRepository:

    def __init__(self, http_client: HttpClient, config_service: ConfigService):
        self.__http_client = http_client
        self.__config_service = config_service

    def getAnchor(self, anchor: int) -> Anchor:
        url = f'{self.__config_service.getApiBaseUrl()}/core/anchor/{anchor}'
        r = self.__http_client.get(url)
        return Anchor(
            r['anchor_id'],
            r['block_roots'],
            r['networks'],
            r['root'],
            r['status'])
