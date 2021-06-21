from requests.exceptions import RequestException
import requests
from .http_data import HttpData
from .dto.api_response_entity import ApiResponse
from .http_exception import HttpRequestException


class HttpClient:

    def __init__(self, http_data: HttpData):
        self.__http_data = http_data

    def setApiKey(self, api_key: str):
        self.__http_data.api_key = api_key

    def get(self, url: str, headers={}):
        ''' Wrapper for request library. Can raise HttpRequestException. '''
        try:
            new_headers = dict(
                {"X-API-KEY": self.__http_data.api_key}, **headers)
            response = requests.get(url=url, headers=new_headers)
            response_json = response.json()
            if response.ok:
                return response_json
            raise HttpRequestException(response_json['message'])
        except RequestException as e:
            raise HttpRequestException(str(e))

    def post(self, url: str, body, headers={}):
        ''' Wrapper for request library. Can raise HttpRequestException. '''
        try:
            new_headers = dict(
                {"X-API-KEY": self.__http_data.api_key}, **headers)
            response = requests.post(url=url, json=body, headers=new_headers)
            response_json = response.json()
            if response.ok:
                return response_json
            raise HttpRequestException(response_json['message'])
        except RequestException as e:
            raise HttpRequestException(str(e))
