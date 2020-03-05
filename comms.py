import json
import requests

def send(data):
    dataDic = {'hash': data}
    response = requests.post(url = 'https://enchainte-api.azurewebsites.net/api/send', data = dataDic)
    if response.ok:
        return response.json()['hash'] == data
    return False

def verify(data):
    dataDic = {'hash': data}
    response = requests.post(url = 'https://enchainte-api.azurewebsites.net/api/verify', data = dataDic)
    if response.ok:
        return response.json()['proof']
    raise ValueError('POST response = not OK')

