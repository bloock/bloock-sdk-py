import unittest
from unittest import TestCase, mock
from enchaintesdk.config.entity.config_env_entity import ConfigEnv
from enchaintesdk.config.repository.config_impl_repository import ConfigRepositoryImpl


class ConfigImplRepositoryTestCase(TestCase):
    @mock.patch('enchaintesdk.config.repository.config_data.ConfigData')
    def test_fetch_configuration_prod(self, MockConfigData):
        config = ConfigRepositoryImpl(MockConfigData)
        config.fetchConfiguration(ConfigEnv.PROD)
        MockConfigData.setConfiguration.assert_called_once()

    @mock.patch('enchaintesdk.config.repository.config_data.ConfigData')
    def test_fetch_configuration_test(self, MockConfigData):
        config = ConfigRepositoryImpl(MockConfigData)
        config.fetchConfiguration(ConfigEnv.TEST)
        MockConfigData.setTestConfiguration.assert_called_once()

    @mock.patch('enchaintesdk.config.repository.config_data.ConfigData')
    def test_fetch_configuration_random_environment(self, MockConfigData):
        config = ConfigRepositoryImpl(MockConfigData)
        config.fetchConfiguration('RAND')
        MockConfigData.setConfiguration.assert_called_once()
