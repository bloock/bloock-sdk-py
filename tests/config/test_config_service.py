import unittest
from unittest import TestCase, mock
from enchaintesdk.config.entity.configuration_entity import Configuration
from enchaintesdk.config.entity.config_env_entity import ConfigEnv
from enchaintesdk.config.service.config_service import ConfigService


class ConfigServiceTestCase(TestCase):

    @mock.patch('enchaintesdk.config.repository.config_repository.ConfigRepository')
    def test_setup_environment(self, MockConfigRepo):
        config = ConfigService(MockConfigRepo)
        config.setupEnvironment(ConfigEnv.TEST)
        MockConfigRepo.fetchConfiguration.assert_called_once()

    @mock.patch('enchaintesdk.config.repository.config_repository.ConfigRepository')
    def test_get_configuration(self, MockConfigRepo):
        config = ConfigService(MockConfigRepo)
        config.getConfiguration()
        MockConfigRepo.getConfiguration.assert_called_once()

    @mock.patch('enchaintesdk.config.repository.config_repository.ConfigRepository')
    def test_get_base_url(self, MockConfigRepo):
        config = ConfigService(MockConfigRepo)
        ret = Configuration()
        ret.host = 'test'
        ret.api_version = 'ing'
        MockConfigRepo.getConfiguration.return_value = ret
        self.assertEqual(config.getApiBaseUrl(), 'testing',
                         'Expecting "testing", found something else.')
        MockConfigRepo.getConfiguration.assert_called_once()
