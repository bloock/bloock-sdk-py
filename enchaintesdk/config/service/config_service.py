from ..entity.config_env_entity import ConfigEnv
from ..entity.configuration_entity import Configuration


class ConfigService():
    def __init__(self):
        pass

    def setupEnvironment(self, environment: ConfigEnv) -> Configuration:
        pass

    def getConfiguration(self) -> Configuration:
        pass

    def getApiBaseUrl(self) -> str:
        pass
