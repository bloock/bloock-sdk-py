import json
from web3 import Web3
from requests.exceptions import RequestException
from enchaintesdk.config.service.config_service import ConfigService
from .web3_exception import Web3Exception


class Web3Client:
    ''' Object in charge of connecting to blockchain.'''

    def __init__(self, configService: ConfigService):
        self.__config_service = configService

    def validateRoot(self, root: str) -> int:
        ''' ValidateRoot: given the root identifier as a hexadecimal
            string (with no "0x" in front) returns the timestamp as int 
            of its insertion in the blockchain. '''
        try:
            config = self.__config_service.getConfiguration()
            web3 = Web3(Web3.HTTPProvider(config.http_provider))
            contract = web3.eth.contract(
                address=config.contract_address, abi=json.loads(config.contract_abi))
            return contract.functions.getState('0x'+root).call()
        except RequestException as e:
            raise Web3Exception(str(e))
