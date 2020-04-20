import json
import requests

def send(dataH):
    response = requests.post(url = 'http://enchainte-demo-api.westeurope.azurecontainer.io:3000/send',
        json = {'messages': [dataH]})
    if response.ok:
        return response.json()
    return None

def verify(dataH):
    response = requests.get('http://enchainte-core.westeurope.azurecontainer.io:7878/proof?hash='+dataH)
    if response.ok:
        return response.json()
    raise ValueError('POST response = not OK')

