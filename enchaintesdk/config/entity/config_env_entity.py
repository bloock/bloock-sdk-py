from enum import Enum


class ConfigEnv(Enum):
    ''' Enumeration representing each environment.

        Values:
        - PROD: for production environment.
        - TEST: for testing environment.
    '''
    PROD = "prod"
    TEST = "test"
