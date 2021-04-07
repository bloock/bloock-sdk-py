from ..entity.config_env_entity import ConfigEnv
from ..entity.configuration_entity import Configuration
from .config_data import ConfigData
from .config_repository import ConfigRepository


class ConfigRepositoryImpl (ConfigRepository):

    def __init__(self, config_data: ConfigData):
        self.__config_data = config_data

    def fetchConfiguration(self, environment: ConfigEnv) -> Configuration:
        if environment == ConfigEnv.PROD:
            return self.__config_data.setConfiguration()
        elif environment == ConfigEnv.TEST:
            return self.__config_data.setTestConfiguration()
        else:
            return self.__config_data.setConfiguration()

    def getConfiguration(self) -> Configuration:
        return self.__config_data.getConfiguration()
