from unittest import TestCase, mock
from enchaintesdk.shared.utils import Utils
from enchaintesdk.proof.repository.proof_repository import ProofRepository
from enchaintesdk.proof.entity.proof_entity import Proof
from enchaintesdk.infrastructure.http.dto.api_response_entity import ApiResponse
from enchaintesdk.message.entity.message_entity import Message
from enchaintesdk.proof.entity.exception.proof_verification_exception import ProofVerificationException


class testProofRepository(TestCase):

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.infrastructure.blockchain.web3.Web3Client')
    @mock.patch('enchaintesdk.infrastructure.http.http_client.HttpClient')
    def test_retrieve_proof_okay(self, MockHttpClient, MockBlockchainClient, MockConfig):
        MockHttpClient.post.return_value = ApiResponse({
            "data": {
                "bitmap": "bfdf7000",
                "depth": "000400060006000500030002000400060007000800090009",
                "leaves": [
                    "02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5",
                ],
                "nodes": [
                    "bb6986853646d083929d1d92638f3d4741a3b7149bd2b63c6bfedd32e3c684d3",
                    "0616067c793ac533815ae2d48d785d339e0330ce5bb5345b5e6217dd9d1dbeab",
                    "68b8f6b25cc700e64ed3e3d33f2f246e24801f93d29786589fbbab3b11f5bcee"
                ],
                "root": "c6372dab6a48637173a457e3ae0c54a500bb50346e847eccf2b818ade94d8ccf"
            },
            "success": True
        })
        proof_repo = ProofRepository(
            MockHttpClient, MockBlockchainClient, MockConfig)
        proof = proof_repo.retrieveProof([Message(
            "02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5")])
        self.assertIsInstance(proof, Proof)
        self.assertEqual(proof.bitmap, 'bfdf7000',
                         'Expecting different bitmap.')
        self.assertEqual(
            proof.depth, '000400060006000500030002000400060007000800090009', 'Expecting different depth')
        self.assertEqual(proof.leaves, [
                         '02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5'], 'Expecting different leaves array')
        self.assertEqual(proof.nodes, [
            "bb6986853646d083929d1d92638f3d4741a3b7149bd2b63c6bfedd32e3c684d3",
            "0616067c793ac533815ae2d48d785d339e0330ce5bb5345b5e6217dd9d1dbeab",
            "68b8f6b25cc700e64ed3e3d33f2f246e24801f93d29786589fbbab3b11f5bcee"
        ], 'Expecting different nodes array')

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.infrastructure.blockchain.web3.Web3Client')
    @mock.patch('enchaintesdk.infrastructure.http.http_client.HttpClient')
    def test_verify_proof_keccak(self, MockHttpClient, MockBlockchainClient, MockConfig):
        leaves = [
            '0000000000000000000000000000000000000000000000000000000000000000']
        nodes = [
            '1111111111111111111111111111111111111111111111111111111111111111'
        ]
        depth = '00010001'
        bitmap = '40'
        root = '8e4b8e18156a1c7271055ce5b7ef53bb370294ebd631a3b95418a92da46e681f'
        proof_repo = ProofRepository(
            MockHttpClient, MockBlockchainClient, MockConfig)
        proof = Proof(leaves, nodes, depth, bitmap)
        self.assertEqual(proof_repo.verifyProof(proof).getHash(), root,
                         'Proof not verifying correctly.')

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.infrastructure.blockchain.web3.Web3Client')
    @mock.patch('enchaintesdk.infrastructure.http.http_client.HttpClient')
    def test_verify_proof_keccak_2(self, MockHttpClient, MockBlockchainClient, MockConfig):
        leaves = [
            '0000000000000000000000000000000000000000000000000000000000000000']
        nodes = [
            '0101010101010101010101010101010101010101010101010101010101010101'
        ]
        depth = '00000000'
        bitmap = '40'
        root = 'd5f4f7e1d989848480236fb0a5f808d5877abf778364ae50845234dd6c1e80fc'
        proof_repo = ProofRepository(
            MockHttpClient, MockBlockchainClient, MockConfig)
        proof = Proof(leaves, nodes, depth, bitmap)
        self.assertEqual(proof_repo.verifyProof(proof).getHash(), root,
                         'Proof not verifying correctly.')

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.infrastructure.blockchain.web3.Web3Client')
    @mock.patch('enchaintesdk.infrastructure.http.http_client.HttpClient')
    def test_verify_proof_keccak_3(self, MockHttpClient, MockBlockchainClient, MockConfig):

        leaves = [
            '0000000000000000000000000000000000000000000000000000000000000000']
        nodes = [
            'f49d70da1c2c8989766908e06b8d2277a6954ec8533696b9a404b631b0b7735a'
        ]
        depth = '00010001'
        bitmap = '4000'
        root = '5c67902dc31624d9278c286ef4ce469451d8f1d04c1edb29a5941ca0e03ddc8d'
        proof_repo = ProofRepository(
            MockHttpClient, MockBlockchainClient, MockConfig)
        proof = Proof(leaves, nodes, depth, bitmap)
        self.assertEqual(proof_repo.verifyProof(proof).getHash(), root,
                         'Proof not verifying correctly.')

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.infrastructure.blockchain.web3.Web3Client')
    @mock.patch('enchaintesdk.infrastructure.http.http_client.HttpClient')
    def test_verify_proof_failing_invalid_leaf(self, MockHttpClient, MockBlockchainClient, MockConfig):
        leaves = [
            '000000000000000000000000000000000000000000000000000000000000000']
        nodes = [
            '0101010101010101010101010101010101010101010101010101010101010101'
        ]
        depth = '00000000'
        bitmap = '40'
        proof_repo = ProofRepository(
            MockHttpClient, MockBlockchainClient, MockConfig)
        proof = Proof(leaves, nodes, depth, bitmap)
        with self.assertRaises(ProofVerificationException):
            proof_repo.verifyProof(proof)

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.infrastructure.blockchain.web3.Web3Client')
    @mock.patch('enchaintesdk.infrastructure.http.http_client.HttpClient')
    def test_verify_proof_failing_invalid_node(self, MockHttpClient, MockBlockchainClient, MockConfig):
        leaves = [
            '0000000000000000000000000000000000000000000000000000000000000000']
        nodes = [
            '010101010101010101010101010101010101010101010101010101010101010'
        ]
        depth = '00000000'
        bitmap = '40'
        proof_repo = ProofRepository(
            MockHttpClient, MockBlockchainClient, MockConfig)
        proof = Proof(leaves, nodes, depth, bitmap)
        with self.assertRaises(ProofVerificationException):
            proof_repo.verifyProof(proof)

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.infrastructure.blockchain.web3.Web3Client')
    @mock.patch('enchaintesdk.infrastructure.http.http_client.HttpClient')
    def test_verify_proof_failing_invalid_depth(self, MockHttpClient, MockBlockchainClient, MockConfig):
        leaves = [
            '0000000000000000000000000000000000000000000000000000000000000000']
        nodes = [
            '0101010101010101010101010101010101010101010101010101010101010101'
        ]
        depth = '0000000'
        bitmap = '40'
        proof_repo = ProofRepository(
            MockHttpClient, MockBlockchainClient, MockConfig)
        proof = Proof(leaves, nodes, depth, bitmap)
        with self.assertRaises(ProofVerificationException):
            proof_repo.verifyProof(proof)

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.infrastructure.blockchain.web3.Web3Client')
    @mock.patch('enchaintesdk.infrastructure.http.http_client.HttpClient')
    def test_verify_proof_failing_invalid_bitmap(self, MockHttpClient, MockBlockchainClient, MockConfig):
        leaves = [
            '0000000000000000000000000000000000000000000000000000000000000000']
        nodes = [
            '0101010101010101010101010101010101010101010101010101010101010101'
        ]
        depth = '000000000'
        bitmap = '4'
        proof_repo = ProofRepository(
            MockHttpClient, MockBlockchainClient, MockConfig)
        proof = Proof(leaves, nodes, depth, bitmap)
        with self.assertRaises(ProofVerificationException):
            proof_repo.verifyProof(proof)

    ''' #TESTS IN BLAKE2B

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.infrastructure.blockchain.web3.Web3Client')
    @mock.patch('enchaintesdk.infrastructure.http.http_client.HttpClient')
    def test_verify_proof_1(self, MockHttpClient, MockBlockchainClient, MockConfig):
        leaves = [
            '72aae7e86eb51f61a620831320475d9d61cbd52749dbf18fa942b1b97f50aee9']
        nodes = ['359b5206452a4ca5058129727fb48f0860a36c0afee0ec62baa874927e9d4b99',
                 '707cb86e449cd3990c85fb3ae9ec967ee12b82f21eae9e6ea35180e6c331c3e8',
                 '23950edeb3ca719e814d8b04d63d90d39327b49b7df5baf2f72305c1f2b260b7',
                 '72aae7e86eb50f61a620831320475d9d61cbd52749dbf18fa942b1b97f50aee9',
                 '517e320992fb35553575750153992d6360268d04a1e4d9e2cae7e5c3736ac627',
                 ]
        depth = '000200030004000500050001'
        bitmap = 'f4'
        root = '6608fd2c5d9c28124b41d6e441d552ad811a51fc6fdae0f33aa64bf3f43ca699'
        proof_repo = ProofRepository(
            MockHttpClient, MockBlockchainClient, MockConfig)
        proof = Proof(leaves, nodes, depth, bitmap)
        self.assertEqual(proof_repo.verifyProof(proof).getHash(), root,
                         'Proof not verifying correctly.')

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.infrastructure.blockchain.web3.Web3Client')
    @mock.patch('enchaintesdk.infrastructure.http.http_client.HttpClient')
    def test_verify_proof_2(self, MockHttpClient, MockBlockchainClient, MockConfig):
        leaves = [
            '82aae7e86eb51f61a620831320475d9d61cbd52749dbf18fa942b1b97f50aee9',
            '92aae7e86eb51f61a620831320475d9d61cbd52749dbf18fa942b1b97f50aee9']
        nodes = ['285f570a90100fb94d5608b25d9e2b74bb58f068d495190f469aac5ef7ecf3c5',
                 '8f0194b0986e0ea2d6e24df52f1fb3d44e421bce224383f7805f38dc772b3489',
                 ]
        depth = '0001000300030002'
        bitmap = 'a0'
        root = '264248bf767509da977f61d42d5723511b7af2781613b9119edcebb25a226976'
        proof_repo = ProofRepository(
            MockHttpClient, MockBlockchainClient, MockConfig)
        proof = Proof(leaves, nodes, depth, bitmap)
        self.assertEqual(proof_repo.verifyProof(proof).getHash(), root,
                         'Proof not verifying correctly.')

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.infrastructure.blockchain.web3.Web3Client')
    @mock.patch('enchaintesdk.infrastructure.http.http_client.HttpClient')
    def test_verify_proof_3(self, MockHttpClient, MockBlockchainClient, MockConfig):
        leaves = [
            '3b7a824a1572e5c64bc280d97cc658bebbd7f85032bda98d478012335637e34c']
        nodes = ['9bb9c0392509dbbb6cf8fecdff94c1c2175ceb2bbf1e4b8b527ff6ee8ec07908',
                 '69a6183ca72fc154d589527a5eae58038497818c4e48c8496ee0093448a227d8',
                 '4a11b9a8bcb62a6fa4104b0a01b5333e6636741c9683c0550365f06049f8f4ee',
                 '3809cc631ac9ae3184784edf104c195716d1e0e2738c8390fdd0f290b3ea6487',
                 'f22d28a9ae7db36bfe632939c0a6428edd4b109f1b616afb9c1ea31c8fd80a03',
                 '6932c94926edabb0f95e0f26fec8b75863b6fd8d882e44629d6d3f449b3b1a83',
                 '8af97658047a196a345f14aaedce43a7025b09481607511e31118ee718e2354a']
        depth = '00010002000300040006000700070005'
        bitmap = 'fb00'
        root = '482353335a663158a869de9b3d46987caedec00d7581c3a0eb75054ba4eb04b3'
        proof_repo = ProofRepository(
            MockHttpClient, MockBlockchainClient, MockConfig)
        proof = Proof(leaves, nodes, depth, bitmap)
        self.assertEqual(proof_repo.verifyProof(proof).getHash(), root,
                         'Proof not verifying correctly.')

    @mock.patch('enchaintesdk.config.service.config_service.ConfigService')
    @mock.patch('enchaintesdk.infrastructure.blockchain.web3.Web3Client')
    @mock.patch('enchaintesdk.infrastructure.http.http_client.HttpClient')
    def test_verify_proof_4(self, MockHttpClient, MockBlockchainClient, MockConfig):
        leaves = [
            '72aae3286eb51f61a620831320475d9d61cbd52749dbf18fa942b1b97f50aee9']
        nodes = []
        depth = '0000'
        bitmap = '00'
        root = '72aae3286eb51f61a620831320475d9d61cbd52749dbf18fa942b1b97f50aee9'
        proof_repo = ProofRepository(
            MockHttpClient, MockBlockchainClient, MockConfig)
        proof = Proof(leaves, nodes, depth, bitmap)
        self.assertEqual(proof_repo.verifyProof(proof).getHash(), root,
                         'Proof not verifying correctly.')
    '''
