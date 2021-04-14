from ..entity.config_env_entity import ConfigEnv
from ..entity.configuration_entity import Configuration
from ..repository.config_repository import ConfigRepository


class ConfigService:
    ''' Service in charge of managing Enchainte API's
        configuration.'''

    def __init__(self, config_repo: ConfigRepository):
        self.__config_repository = config_repo

    def setupEnvironment(self, environment: ConfigEnv) -> Configuration:
        ''' Initializes the configuration accordingly to the especified
            environment.'''
        return self.__config_repository.fetchConfiguration(environment)

    def getConfiguration(self) -> Configuration:
        ''' Returns a Configuration object with the current
            configuration for the API.
        '''
        return self.__config_repository.getConfiguration()

    def getApiBaseUrl(self) -> str:
        ''' Returns a string containing the API'S base URL.'''
        conf = self.__config_repository.getConfiguration()
        return "{}{}".format(conf.host, conf.api_version)
