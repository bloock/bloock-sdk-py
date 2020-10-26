from ..entity.config import Config
from ..utils.utils import Utils
import requests
from requests.exceptions import RequestException
import base64
import hashlib
import hmac
from datetime import datetime
import six 

class ConfigService:
    stop_timers = [False]
    config = [None]
    __ENVIRONMENT = 'PROD'
    __ENDPOINT = 'enchainte-config.azconfig.io'
    __CREDENTIAL = 'ihs8-l9-s0:JPRPUeiXJGsAzFiW9WDc'
    __SECRET = '1UA2dijC0SIVyrPKUKG0gT0oXxkVaMrUfJuXkLr+i0c='

    def __init__(self):
        try:
            self.__fetchConfig()
        except BaseException as e:
            print('Error while fetching the SDK configuration:')
            print(str(e))

    def __fetchConfig(self):
        path = '/kv?key=SDK_*&label='+self.__ENVIRONMENT
        headers_req = self.__getAuthHeaders(path, '') 
        try:
            response = requests.get(url='https://' + self.__ENDPOINT + path,
                                     headers=headers_req)
            res_json = response.json()

            if response.ok:
                conf_items = res_json['items']
                conf_dic = {}
                for row in conf_items:
                    conf_dic[row['key']] = row['value']
                self.config[0] = Config(
                    conf_dic['SDK_HOST'],
                    conf_dic['SDK_WRITE_ENDPOINT'],
                    conf_dic['SDK_PROOF_ENDPOINT'],
                    conf_dic['SDK_FETCH_ENDPOINT'],
                    conf_dic['SDK_HTTP_PROVIDER'],
                    conf_dic['SDK_CONTRACT_ADDRESS'],
                    conf_dic['SDK_CONTRACT_ABI'],
                    conf_dic['SDK_PROVIDER'],
                    conf_dic['SDK_WRITE_INTERVAL'],
                    conf_dic['SDK_CONFIG_INTERVAL'],
                    conf_dic['SDK_WAIT_MESSAGE_INTERVAL_FACTOR'],
                    conf_dic['SDK_WAIT_MESSAGE_INTERVAL_DEFAULT']
                )
            else:
                raise RequestException(res_json['message'])

        except RequestException as e:
            raise e

    def setTestEnvironment(self, isTest):
        ''' Sets the environment to testing or production porpuses. Inputs a boolean: if True,
            it is set to "TEST", else it defaults to "PROD".'''
        
        if isTest:
            self.__ENVIRONMENT = 'TEST'
        else:
            self.__ENVIRONMENT = 'PROD'
    
    def getConfig(self):
        return self.config[0]
    
    def __getAuthHeaders(self, url, body):
        verb = 'GET'

        utc_now = str(datetime.utcnow().strftime("%b, %d %Y %H:%M:%S ")) + "GMT"

        if six.PY2:
            content_digest = hashlib.sha256(bytes(body)).digest()
        else:
            content_digest = hashlib.sha256(bytes(body, 'utf-8')).digest()

        content_hash = base64.b64encode(content_digest).decode('utf-8')

        # Signed Headers
        signed_headers = "x-ms-date;host;x-ms-content-sha256"  # Semicolon separated header names

        # String-To-Sign
        string_to_sign = verb + '\n' + \
                        url + '\n' + \
                        utc_now + ';' + self.__ENDPOINT + ';' + content_hash  # Semicolon separated SignedHeaders values

        # Decode secret
        if six.PY2:
            decoded_secret = base64.b64decode(self.__SECRET)
            digest = hmac.new(decoded_secret, bytes(
                string_to_sign), hashlib.sha256).digest()
        else:
            decoded_secret = base64.b64decode(self.__SECRET, validate=True)
            digest = hmac.new(decoded_secret, bytes(
                string_to_sign, 'utf-8'), hashlib.sha256).digest()

        # Signature
        signature = base64.b64encode(digest).decode('utf-8')

        # Result request headers
        return {
            "x-ms-date": utc_now,
            "x-ms-content-sha256": content_hash,
            "Authorization": "HMAC-SHA256 Credential=" + self.__CREDENTIAL + "&SignedHeaders=" + signed_headers + "&Signature=" + signature
        }

