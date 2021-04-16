import requests
from requests.exceptions import RequestException
from .http_data import HttpData
from .dto.api_response_entity import ApiResponse
from .exception.http_exception import HttpRequestException


class HttpClient:

    def __init__(self, http_data: HttpData):
        self.__http_data = http_data

    def setApiKey(self, api_key: str):
        self.__http_data.api_key = api_key

    def get(self, url: str, headers={}):
        new_headers = dict(
            {"Authorization": self.__http_data.api_key}, **headers)
        response = requests.get(url=url, headers=new_headers)
        response_json = response.json()
        if response.ok:
            return ApiResponse(response_json)
        raise HttpRequestException(response_json['error']['message'])

    def post(self, url: str, body, headers={}):
        ''' Wrapper for request library. Can raise RequestException or HttpRequestException. '''
        new_headers = dict(
            {"Authorization": 'Bearer ' + self.__http_data.api_key}, **headers)
        response = requests.post(url=url, json=body, headers=new_headers)
        response_json = response.json()
        if response.ok:
            return ApiResponse(response_json)
        raise HttpRequestException(response_json['error']['message'])
