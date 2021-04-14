from ..entity.config_env_entity import ConfigEnv
from ..entity.configuration_entity import Configuration
from .config_data import ConfigData


class ConfigRepository:
    ''' Repository in charge of managing Enchainte API's
        configuration.'''

    def __init__(self, config_data: ConfigData):
        ''' Requieres a ConfigData object to be maintained.'''
        self.__config_data = config_data

    def fetchConfiguration(self, environment: ConfigEnv) -> Configuration:
        ''' Updates the configuration accordingly to the especified
            environment.
        '''
        if environment == ConfigEnv.PROD:
            return self.__config_data.setConfiguration()
        elif environment == ConfigEnv.TEST:
            return self.__config_data.setTestConfiguration()
        else:
            return self.__config_data.setConfiguration()

    def getConfiguration(self) -> Configuration:
        ''' Returns a Configuration object with the current
            configuration for the API.
        '''
        return self.__config_data.getConfiguration()
