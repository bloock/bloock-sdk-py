from ..entity.config_env_entity import ConfigEnv
from ..entity.configuration_entity import Configuration
from ..repository.config_repository import ConfigRepository
from .config_service import ConfigService


class ConfigServiceImpl (ConfigService):

    def __init__(self, config_repo: ConfigRepository):
        self.__config_repository = config_repo

    def setupEnvironment(self, environment: ConfigEnv) -> Configuration:
        return self.__config_repository.fetchConfiguration(environment)

    def getConfiguration(self) -> Configuration:
        return self.__config_repository.getConfiguration()

    def getApiBaseUrl(self) -> str:
        conf = self.__config_repository.getConfiguration()
        return "{}{}".format(conf.host, conf.api_version)
