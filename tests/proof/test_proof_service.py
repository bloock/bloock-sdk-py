from datetime import time
from bloock.config.entity.networks_entity import Network
from unittest import TestCase, mock
from unittest.mock import call 
from bloock.shared.utils import Utils
from bloock.proof.service.proof_service import ProofService
from bloock.proof.entity.proof_entity import Proof, ProofAnchor
from bloock.infrastructure.http.dto.api_response_entity import ApiResponse
from bloock.record.entity.record_entity import Record
from bloock.proof.entity.exception.proof_verification_exception import ProofVerificationException


class testProofService(TestCase):

    @mock.patch('bloock.proof.repository.proof_repository.ProofRepository')
    def test_verify_proof_okay(self, MockProofRepo):
        MockProofRepo.verifyProof.return_value = Record('root')
        proof = Proof(
                bitmap = "bfdf7000",
                depth = "000400060006000500030002000400060007000800090009",
                leaves = [
                    "02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5",
                ],
                nodes = [
                    "bb6986853646d083929d1d92638f3d4741a3b7149bd2b63c6bfedd32e3c684d3",
                    "0616067c793ac533815ae2d48d785d339e0330ce5bb5345b5e6217dd9d1dbeab",
                    "68b8f6b25cc700e64ed3e3d33f2f246e24801f93d29786589fbbab3b11f5bcee"
                ],
                anchor= {
                    "anchor_id": 387,
                    "root": "c6372dab6a48637173a457e3ae0c54a500bb50346e847eccf2b818ade94d8ccf",
                    "networks": [
                        {
                            "name": "bloock_chain",
                            "tx_hash": "0xc087797b9700245c8e3f678874e9c419297f2302cb822d798ca94cce8c27aea9",
                            "state": "Confirmed",
                            "created_at": 0
                        },{
                            "name": "ethereum_rinkeby",
                            "tx_hash": "0xc087797b9700245c8e3f678874e9c419297f2302cb822d798ca94cce8c27aea9",
                            "state": "Confirmed",
                            "created_at": 1
                        },{
                            "name": "ethereum_mainnet",
                            "tx_hash": "0xc087797b9700245c8e3f678874e9c419297f2302cb822d798ca94cce8c27aea9",
                            "state": "Confirmed",
                            "created_at": 1
                        }
                    ],
                    "status": "Success"
                }
            )
        root = Record('root')
        calls = [
            call(Network.BLOOCK_CHAIN, root),
            call(Network.ETHEREUM_RINKEBY, root),
            call(Network.ETHEREUM_MAINNET, root)
            ]
        MockProofRepo.validateRoot.has_calls(calls)
        MockProofRepo.validateRoot.side_effect = [0,1,2]

        service = ProofService(MockProofRepo)
        timestamp = service.verifyProof(proof)
        self.assertEqual(timestamp, 2, 'wrong timestamp recieved')

    @mock.patch('bloock.proof.repository.proof_repository.ProofRepository')
    def test_verify_proof_wrong_network_name(self, MockProofRepo):
        MockProofRepo.verifyProof.return_value = Record('root')
        proof = Proof(
                bitmap = "bfdf7000",
                depth = "000400060006000500030002000400060007000800090009",
                leaves = [
                    "02aae7e86eb50f61a62083a320475d9d60cbd52749dbf08fa942b1b97f50aee5",
                ],
                nodes = [
                    "bb6986853646d083929d1d92638f3d4741a3b7149bd2b63c6bfedd32e3c684d3",
                    "0616067c793ac533815ae2d48d785d339e0330ce5bb5345b5e6217dd9d1dbeab",
                    "68b8f6b25cc700e64ed3e3d33f2f246e24801f93d29786589fbbab3b11f5bcee"
                ],
                anchor = {
                    "anchor_id": 387,
                    "root": "c6372dab6a48637173a457e3ae0c54a500bb50346e847eccf2b818ade94d8ccf",
                    "networks": [
                        {
                            "name": "bloock_chain",
                            "tx_hash": "0xc087797b9700245c8e3f678874e9c419297f2302cb822d798ca94cce8c27aea9",
                            "state": "Confirmed",
                            "created_at": 0
                        },{
                            "name": "ethereum_secret_master_network",
                            "tx_hash": "0xc087797b9700245c8e3f678874e9c419297f2302cb822d798ca94cce8c27aea9",
                            "state": "Confirmed",
                            "created_at": 1
                        },{
                            "name": "ethereum_mainnet",
                            "tx_hash": "0xc087797b9700245c8e3f678874e9c419297f2302cb822d798ca94cce8c27aea9",
                            "state": "Confirmed",
                            "created_at": 1
                        }
                    ],
                    "status": "Success"
                }
            )
        service = ProofService(MockProofRepo)
        with self.assertRaises(Exception) as context:
            service.verifyProof(proof)
        self.assertTrue("'ethereum_secret_master_network' is not a valid Network" in str(context.exception))