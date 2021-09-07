from ..entity.config_env_entity import ConfigEnv
from ..entity.configuration_entity import Configuration, NetworkConfiguration
from ..entity.networks_entity import Network
from ..repository.config_repository import ConfigRepository

class ConfigService:
    ''' Service in charge of managing Bloock API's
        configuration.'''

    def __init__(self, config_repo: ConfigRepository):
        self.__config_repository = config_repo

    def setApiHost(self, host: str):
        ''' Updates the host with the provided one.'''
        self.__config_repository.setHost(host)

    def setNetworkConfiguration(self, network: Network, config: NetworkConfiguration):
        ''' Overrides the selected network configuration value.'''
        self.__config_repository.setNetworkConfiguration(network, config)

    def getConfiguration(self) -> Configuration:
        ''' Returns a Configuration object with the current
            configuration for the API.
        '''
        return self.__config_repository.getConfiguration()

    def getNetworkConfiguration(self, network: Network):
        ''' Returns the configuration of a specified network.'''
        return self.__config_repository.getNetworkConfiguration(network)

    def getApiBaseUrl(self) -> str:
        ''' Returns a string containing the API'S base URL.'''
        conf = self.__config_repository.getConfiguration()
        return conf.host
