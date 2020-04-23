import json
import requests

def send(dataH):
    response = requests.post(url = 'https://api.enchainte.com/send',
        json = {'messages': [dataH]})
    if response.ok:
        return response.json()
    return None

def verify(dataH):
    response = requests.get('https://api.enchainte.com/verify?hash='+dataH)
    if response.ok:
        return response.json()
    raise ValueError('POST response = not OK')

