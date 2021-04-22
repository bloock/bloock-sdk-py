from enchaintesdk.config.service.config_service import ConfigService
from enchaintesdk.shared.utils import Utils
from ..entity.anchor_entity import Anchor
from ..repository.anchor_repository import AnchorRepository
from enchaintesdk.infrastructure.http.http_exception import HttpRequestException
import time


class AnchorService:
    def __init__(self, anchor_repository: AnchorRepository, config_service: ConfigService):
        self.__anchor_repository = anchor_repository
        self.__config_service = config_service

    def getAnchor(self, anchor_id: int) -> Anchor:
        if not isinstance(anchor_id, int):
            raise TypeError('Invalid input type. Expecting "int".')
        return self.__anchor_repository.getAnchor(anchor_id)

    def waitAnchor(self, anchor_id: int, timeout: int) -> Anchor:
        if not isinstance(anchor_id, int):
            raise TypeError('Invalid input type. Expecting "int".')
        anchor = None
        start = time.time()
        next_try_time = start + \
            self.__config_service.getConfiguration().wait_message_interval_default/1000
        timeout_time = start+timeout/1000
        old_fib = 0
        fib = 1
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
                next_try_time += old_fib+fib
                aux = old_fib
                old_fib = fib
                fib = old_fib + aux

                if current_time > timeout_time:
                    anchor = None
                    break
        return anchor
