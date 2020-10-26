import json
import requests
from requests.exceptions import RequestException
from ..entity.messageReceipt import MessageReceipt
from ..entity.message import Message
from ..entity.proof import Proof



#CONFIG: API_URL
class ApiService:
    apiKey = ""

    @staticmethod
    def write(dataH, config):
        ''' Sends to EnchainteApi a "list of Hashes" (dataH), and returns or a "list of strings"
            containg newly inserted leaves or an Exception.'''

        try:
            data = [x.getMessage() for x in dataH]
            response = requests.post(url=config.host + config.write_endpoint,
                                     json={'hashes': data},
                                     headers={'Authorization': 'Bearer ' + ApiService.apiKey})
            res_json = response.json()

            if response.ok:
                return res_json['hashes']
            else:
                raise RequestException(res_json['message'])

        except RequestException as e:
            raise e

    @staticmethod
    def getProof(dataH, config):
        ''' Sends to EnchainteApi a "list of Hashes" (dataH), and returns or a "Proof" for the
            previous set of leaves or an Exception.'''

        try:
            data = [x.getMessage() for x in dataH]
            response = requests.post(url=config.host + config.proof_endpoint,
                                     json={'hashes': data},
                                     headers={'Authorization': 'Bearer ' + ApiService.apiKey})
            res_json = response.json()

            if response.ok:
                return Proof(data, res_json['nodes'], res_json['depth'], res_json['bitmap'])
            else:
                raise RequestException(res_json['message'])

        except RequestException as e:
            raise e

    @staticmethod
    def getMessages(dataH, config):
        data = [x.getMessage() for x in dataH]
        response = requests.post(url=config.host + config.fetch_endpoint,
                                 json={'hashes': data},
                                 headers={'Authorization': 'Bearer ' + ApiService.apiKey})

        try:
            if response.ok:
                res_json = response.json()
                result = []
                if res_json == None:
                    return result
                for mes in res_json:
                    result.append(
                        MessageReceipt(mes['root'], mes['message'], mes['tx_hash'], mes['status'], mes['error']))
                return result
            else:
                raise RequestException(
                    'Error while requesting Messages to EnchainteAPI.')
        except RequestException as e:
            raise e
