from ..entity.config_env_entity import ConfigEnv
from ..entity.configuration_entity import Configuration


class ConfigRepository:
    ''' Interface for the repository in charge of keeping the
        Enchainte API's configuration.
    '''

    def __init__(self):
        pass

    def fetchConfiguration(self, environment: ConfigEnv) -> Configuration:
        ''' Updates the configuration accordingly to the especified
            environment.
        '''
        pass

    def getConfiguration(self) -> Configuration:
        ''' Returns a Configuration object with the current
            configuration for the API.
        '''
        pass
