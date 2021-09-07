import unittest
from unittest import TestCase, mock
from bloock.config.entity.configuration_entity import Configuration
from bloock.config.entity.config_env_entity import ConfigEnv
from bloock.config.service.config_service import ConfigService


class ConfigServiceTestCase(TestCase):

    @mock.patch('bloock.config.repository.config_repository.ConfigRepository')
    def test_set_api_host(self, MockConfigRepo):
        config = ConfigService(MockConfigRepo)
        config.setApiHost("host")
        MockConfigRepo.setHost.assert_called_once()

    @mock.patch('bloock.config.repository.config_repository.ConfigRepository')
    def test_get_configuration(self, MockConfigRepo):
        config = ConfigService(MockConfigRepo)
        config.getConfiguration()
        MockConfigRepo.getConfiguration.assert_called_once()

    @mock.patch('bloock.config.repository.config_repository.ConfigRepository')
    def test_get_base_url(self, MockConfigRepo):
        config = ConfigService(MockConfigRepo)
        ret = Configuration()
        ret.host = 'test'
        MockConfigRepo.getConfiguration.return_value = ret
        self.assertEqual(config.getApiBaseUrl(), 'test',
                         'Expecting "testing", found something else.')
        MockConfigRepo.getConfiguration.assert_called_once()
