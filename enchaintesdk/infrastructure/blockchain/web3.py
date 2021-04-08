import json
from web3 import Web3
from ..blockchain_client import BlockchainClient
from enchaintesdk.config.service.config_service import ConfigService


class Web3Client (BlockchainClient):
    ''' Object in charge of connecting to blockchain.'''

    def __init__(self, configService: ConfigService):
        self.__config_service = configService

    # TODO: assegurar que realment és un int/float
    def validateRoot(self, root: str) -> float:
        ''' ValidateRoot: given the root identifier as a hexadecimal
            string (with no "0x" in front) returns the timestamp as int/float 
            of its insertion in the blockchain. '''
        config = self.__config_service.getConfiguration()
        web3 = Web3(Web3.WebsocketProvider(config.provider))
        contract = web3.eth.contract(
            address=config.contract_address, abi=config.contract_abi)
        return contract.functions.getCheckpoint('0x'+root).call()
