from web3 import Web3
from ..entity.hash import Hash
from ..utils.constants import *
import json


class Web3Service:
    w3 = Web3(Web3.WebsocketProvider(WEB3_PROVIDER))
    contract = w3.eth.contract(
        address=CONTRACT_ADDRESS, abi=CONTRACT_ABI)

    @staticmethod
    def validateRoot(root):
        return Web3Service.contract.functions.getCheckpoint('0x'+root).call()
