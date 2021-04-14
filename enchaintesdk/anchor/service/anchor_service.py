from enchaintesdk.config.service.config_service import ConfigService
from enchaintesdk.shared.utils import Utils
from ..entity.anchor_entity import Anchor
from ..entity.exception.anchor_not_found_exception import AnchorNotFoundException
from ..repository.anchor_repository import AnchorRepository


class AnchorService:
    def __init__(self, anchor_repository: AnchorRepository, config_service: ConfigService):
        self.__anchor_repository = anchor_repository
        self.__config_service = config_service

    def getAnchor(self, anchor_id: int) -> Anchor:
        anchor = self.__anchor_repository.getAnchor(anchor_id)

        if anchor == None:
            raise AnchorNotFoundException(id)

        return Anchor(
            anchor.anchor_id,
            anchor.block_roots,
            anchor.networks,
            anchor.root,
            anchor.status
        )

    def waitAnchor(self, anchor_id: int) -> Anchor:
        attempts = 0
        anchor = None
        while anchor == None:
            try:
                response = self.__anchor_repository.getAnchor(anchor_id)
                if response != None:
                    tempAnchor = Anchor(
                        response.data['anchor_id'],
                        response.data['block_roots'],
                        response.data['networks'],
                        response.data['root'],
                        response.data['status']
                    )

                    if tempAnchor.status == "Success":
                        anchor = tempAnchor
                        break

            except Exception:
                Utils.sleep(
                    self.__config_service.getConfiguration().wait_message_interval_default +
                    attempts * self.__config_service.getConfiguration().wait_message_interval_factor
                )

            attempts += 1

        return anchor
