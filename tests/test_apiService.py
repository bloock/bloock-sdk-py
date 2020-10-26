import unittest
from unittest import mock
import numpy as np
from requests.exceptions import RequestException
from enchaintesdk.entity.message import Message
from enchaintesdk.comms.apiService import ApiService
from enchaintesdk.utils.constants import API_URL, API_KEY
from enchaintesdk.entity.messageReceipt import MessageReceipt


def mocked_requests_post(*args, **kwargs):
    class MockResponse:
        def __init__(self, json_data, status_code):
            self.json_data = json_data
            self.ok = status_code

        def json(self):
            return self.json_data

    if kwargs["url"] == API_URL+'/write':
        if kwargs["json"]["hashes"] == ['012c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8']:
            return MockResponse(
                {
                    "error": True,
                    "message": "Error 1062: Duplicate entry '012c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8' for key 'registries.leaf'"
                }, False)

        else:
            return MockResponse(
                {
                    "success": True,
                    "hashes": kwargs["json"]["hashes"]
                }, True)
    elif kwargs["url"] == API_URL+'/proof':
        if kwargs["json"]["hashes"] == ['012c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8']:
            return MockResponse(
                {
                    "error": True,
                    "message": "record not found"
                }, False)

        else:
            return MockResponse(
                {
                    "success": True,
                    "error": "",
                    "nodes": [
                        "14fbb91c028d6dcf4d2158637a2e816bf41e497ddee084fcac0399c40f61c003",
                        "65e7b0de2a9dbf3ca81a966cc5e19410680d1bc4f9fa4f2926e9bd4f547ea4aa",
                        "2ec687a123697756f5df0ce68008c8a1f6197578bafbadb91e74e5b75a448baf",
                        "b6d108dfb1ee71b641a7c6ae5275ee28584952e184dae232a22e5e060f3f7fa2",
                        "02aaa3c0621c95ae6a0788cd7a606f62d39cd346d81d365e5f6224ce65441471",
                        "6e3bc705142a10c44e2eb61d4087674e3812730bb1f3e82eb052957165c47595",
                        "02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee9",
                        "02af91db429c4991c4ced5f6eb20e49aeb8377881c99ddca13e355b6feea9e36",
                        "a7cbe33e37f2cd970282439dca67b43b8270da3ff434d4d8cccdc78020724b1d",
                        "311e924403b9bfcb729cd979ef439f0bd975ca3a48153bc7a621de4fce2c3c53",
                        "54c30bd2dfaf5e36623484b27138d365002ba437c847cf64091b6f4c1b6581d2",
                        "84ca0d61486cc2207daea9db9504a1e725705de4429a89f72c958ef2dade41dd",
                        "bc38d128c34e0a079e44c2d782a953f8a500b2c963be306cc03aceb0ca137fac",
                        "735e27fa1657205786007c7c91cc48ea8d59754d0bbf81d1a5aa6f3bb175f94e",
                        "75fbd15a6312a702c99dc1e4a8ce579c29291a1ec00111acf26bcfdb74b3d94c",
                        "f018cb9367a56478494ce6276dfe19df26fe27659e0b10866362eefeddac2ba7",
                        "f8922956c9db7b948fe68d9f2f46f506f2b0b065f753653f27e17d056e6e0bdc",
                        "64b6df888eabcaad36d27566faac9df198c9b9d3a64a6816e5d8558d81952a7a"
                    ],
                    "depth": "07090b0d0f1011110e0c0a0806050403020100",
                    "bitmap": "020000"
                }, True)
    elif kwargs["url"] == API_URL+'/message/fetch':
        if kwargs["json"]["hashes"] == ['012c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8']:
            return MockResponse(
                [], False)
        elif kwargs["json"]["hashes"] == ['ggggggggggggggggggggggggggggg']:
            return MockResponse(
                {
                    "error": True,
                    "message": "404: web not found or something (any connection problem)."
                }, False)
        else:
            return MockResponse(
                [{"root": "23987c0121b07172b5995d0890bdf8a234c3ff8015d87c034a42792213b2ae60",
                    "message": "02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee6",
                    "tx_hash": "0x4ea5c7d431fef1150f63d1dac89b02427d56ef7ef0035269edf6b2a083a1ab44",
                    "status": "success", "error": 0}], True)
    return MockResponse(None, False)


class TestApiService(unittest.TestCase):
    """@ mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_send_success(self, mock_post):
        try:
            ApiService.apiKey = API_KEY
            response = ApiService.write(
                [Hash.fromHash('032c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8')])
            self.assertEqual(
                response, ['032c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8'])
        except BaseException as e:
            self.fail(e)

    @ mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_send_already_inserted(self, mock_post):
        ApiService.apiKey = API_KEY
        self.assertRaises(RequestException, ApiService.write,
                          [Hash.fromHash('012c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8')])

    @ mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_verify_okay(self, mock_post):
        try:
            ApiService.apiKey = API_KEY
            response = ApiService.getProof(
                [Hash.fromHash('032c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8')])
            self.assertIsNotNone(response.leaves)
            self.assertIsNotNone(response.nodes)
            self.assertIsNotNone(response.bitmap)
            self.assertIsNotNone(response.depth)
        except BaseException as e:
            self.fail(e)

    @ mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_verify_non_existing_leaf(self, mock_post):
        ApiService.apiKey = API_KEY
        self.assertRaises(RequestException, ApiService.getProof,
                          [Hash.fromHash('012c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8')])

    @ mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_getMessage_existing_leaf(self, mock_post):
        try:
            ApiService.apiKey = API_KEY
            self.assertTrue(isinstance([Hash.fromHash(
                '02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee6')], list))
        except BaseException as e:
            self.fail(e)

    @ mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_getMessage_non_existing_leaf(self, mock_post):
        try:
            ApiService.apiKey = API_KEY
            self.assertTrue(isinstance(
                [Hash.fromHash('012c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8'),
                 Hash.fromHash('022c2b3cdc772ebff11b795490f6f1f4ef2caa5e5f712c00149f18410d6fbfe8')], list))
        except BaseException as e:
            self.fail(e)

    @ mock.patch('requests.post', side_effect=mocked_requests_post)
    def test_getMessage_error(self, mock_post):
        ApiService.apiKey = API_KEY
        self.assertRaises(RequestException, ApiService.getMessages,
                          [Hash.fromHash('ggggggggggggggggggggggggggggg')])"""
