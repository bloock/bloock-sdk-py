from enchaintesdk.config.service.config_service import ConfigService
from enchaintesdk.shared.utils import Utils
from ..entity.anchor_entity import Anchor
from ..repository.anchor_repository import AnchorRepository
from enchaintesdk.infrastructure.http.exception.http_exception import HttpRequestException
import time


class AnchorService:
    def __init__(self, anchor_repository: AnchorRepository, config_service: ConfigService, timeout=120000):
        self.__anchor_repository = anchor_repository
        self.__config_service = config_service
        self.__timeout = timeout

    def getAnchor(self, anchor_id: int) -> Anchor:
        return self.__anchor_repository.getAnchor(anchor_id)

    def waitAnchor(self, anchor_id: int) -> Anchor:
        attempts = 0
        anchor = None
        start = time.time()
        next_try_time = start + \
            self.__config_service.getConfiguration().wait_message_interval_default/1000
        timeout_time = start+self.__timeout/1000
        while True:
            try:
                anchor = self.__anchor_repository.getAnchor(anchor_id)
                if anchor.status == 'Success':
                    break
                current_time = time.time()
                if current_time > timeout_time:
                    anchor = None
                    break
                Utils.sleep(1000)

            except HttpRequestException:
                current_time = time.time()
                while current_time < next_try_time and current_time < timeout_time:
                    Utils.sleep(200)
                    current_time = time.time()
                next_try_time += attempts * \
                    self.__config_service.getConfiguration().wait_message_interval_factor
                attempts += 1
                if current_time > timeout_time:
                    anchor = None
                    break
        return anchor
