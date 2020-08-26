import json
import requests
from requests.exceptions import RequestException
import asyncio
from ..entity.message import Message
from ..utils.constants import API_URL
from ..entity.hash import Hash
from ..entity.proof import Proof


class ApiService:
    apiKey = ""

    @staticmethod
    def write(dataH):
        ''' Sends to EnchainteApi a "list of Hashes" (dataH), and returns or a "list of strings"
            containg newly inserted leaves or an Exception.'''

        try:
            data = [x.getHash() for x in dataH]
            response = requests.post(url=API_URL+'/write',
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
    def getProof(dataH):
        ''' Sends to EnchainteApi a "list of Hashes" (dataH), and returns or a "Proof" for the
            previous set of leaves or an Exception.'''

        try:
            data = [x.getHash() for x in dataH]
            response = requests.post(url=API_URL+'/proof',
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
    def getMessages(dataH):
        data = [x.getHash() for x in dataH]
        response = requests.post(url=API_URL+'/message/fetch',
                                 json={'hashes': data}, headers={'Authorization': 'Bearer ' + ApiService.apiKey})

        try:
            if response.ok:
                res_json = response.json()
                result = []
                if res_json == None:
                    return result
                for mes in res_json:
                    result.append(
                        Message(mes['root'], mes['message'], mes['tx_hash'], mes['status'], mes['error']))
                return result
            else:
                raise RequestException(
                    'Error while requesting Messages to EnchainteAPI.')
        except RequestException as e:
            raise e
