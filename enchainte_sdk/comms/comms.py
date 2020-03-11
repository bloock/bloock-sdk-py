import json
import requests

def send(dataH):
    response = requests.post(url = 'https://enchainte-api.azurewebsites.net/send',
        data = {'hash': dataH})
    if response.ok:
        return response.json()
    return None

def verify(dataH):
    response = requests.post(url = 'https://enchainte-api.azurewebsites.net/verify',
        data = {'hash': dataH})
    if response.ok:
        return response.json()
    raise ValueError('POST response = not OK')

