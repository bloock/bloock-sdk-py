from ..entity.config_env_entity import ConfigEnv
from ..entity.configuration_entity import Configuration


class ConfigService():
    ''' Interface for the service in charge of keeping the
        Enchainte API's configuration.
    '''

    def __init__(self):
        pass

    def setupEnvironment(self, environment: ConfigEnv) -> Configuration:
        ''' Initializes the configuration accordingly to the especified
            environment.'''
        pass

    def getConfiguration(self) -> Configuration:
        ''' Returns a Configuration object with the current
            configuration for the API.
        '''
        pass

    def getApiBaseUrl(self) -> str:
        ''' Returns a string containing the API'S base URL.'''
        pass
