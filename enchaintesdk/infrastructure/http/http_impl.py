import requests
from requests.exceptions import RequestException
from ..http_client import HttpClient
from .http_data import HttpData
from .dto.api_response_entity import ApiResponse


class HttpClientImpl(HttpClient):

    def __init__(self, http_data: HttpData):
        self.__http_data = http_data

    def setApiKey(self, api_key: str):
        self.__http_data.api_key = api_key

    def get(self, url: str, headers={}):
        try:
            new_headers = dict(
                {"Authorization": self.__http_data.api_key}, **headers)
            response = requests.get(url, new_headers)
            # TODO: segur que està malament perquè el resopnse ha de ser de tipus ApiResponse
            # let response = await axios.get < ApiResponse < T >> (url, config)
            return response.data.data
        except RequestException as e:
            raise e

    def post(self, url: str, body, headers={}):
        try:
            new_headers = dict(
                {"Authorization": self.__http_data.api_key}, **headers)
            response = requests.post(url, new_headers)
            # TODO: segur que està malament perquè el resopnse ha de ser de tipus ApiResponse
            # let response = await axios.post < ApiResponse < T >> (url, body, config)
            return response.data.data
        except RequestException as e:
            raise e
