from ..entity.config_env_entity import ConfigEnv
from ..entity.configuration_entity import Configuration, NetworkConfiguration
from ..entity.networks_entity import Network
from .config_data import ConfigData


class ConfigRepository:
    ''' Repository in charge of managing Bloock API's
        configuration.'''

    def __init__(self, config_data: ConfigData):
        ''' Requieres a ConfigData object to be maintained.'''
        self.__config_data = config_data

    def getConfiguration(self) -> Configuration:
        ''' Returns a Configuration object with the current
            configuration for the API.
        '''
        return self.__config_data.getConfiguration()

    def getNetworkConfiguration(self, network: Network) -> NetworkConfiguration:
        ''' Returns the configuration of a specified network.'''
        return self.__config_data.getNetworkConfiguration(network)

    def setHost(self, host: str):
        ''' Updates the Configuration host '''
        self.__config_data.setHost(host)

    def setNetworkConfiguration(self, network: Network, config: NetworkConfiguration):
        ''' Overrides the selected network configuration value.'''
        self.__config_data.setNetworkConfiguration(network, config)