from web3 import Web3
import json
from config.service.config_service import ConfigService
from ..blockchain_client import BlockchainClient


class Web3Service:

    @staticmethod
    def validateRoot(root, config):
        #w3 = Web3(Web3.WebsocketProvider(config.provider))
        w3 = Web3(Web3.HTTPProvider(config.http_provider))
        contract = w3.eth.contract(
            address=config.contract_address, abi=config.contract_abi)
        return contract.functions.getCheckpoint('0x'+root).call()
