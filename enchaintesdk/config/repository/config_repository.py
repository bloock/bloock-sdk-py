from ..entity.config_env_entity import ConfigEnv
from ..entity.configuration_entity import Configuration


class ConfigRepository:
    def __init__(self):
        pass

    def fetchConfiguration(self, environment: ConfigEnv) -> Configuration:
        pass

    def getConfiguration(self) -> Configuration:
        pass
