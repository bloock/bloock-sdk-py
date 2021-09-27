from typing import List
from bloock.config.service.config_service import ConfigService
from bloock.infrastructure.blockchain.web3 import Web3Client
from bloock.infrastructure.http.http_client import HttpClient
from bloock.record.entity.record_entity import Record
from bloock.config.entity.networks_entity import Network
from bloock.shared.utils import Utils
from ..entity.dto.proof_retrieve_request_entity import ProofRetrieveRequest
from ..entity.proof_entity import Proof
from ..entity.exception.proof_verification_exception import ProofVerificationException


class ProofRepository:

    def __init__(self, http_client: HttpClient, blockchain_client, config_service: ConfigService):
        self.__http_client = http_client
        self.__blockchain_client = blockchain_client
        self.__config_service = config_service

    def retrieveProof(self, records: List[Record], network: Network, date: float) -> Proof:
        url = f'{self.__config_service.getApiBaseUrl()}/core/proof'
        body = {'messages': [m.getHash() for m in records]}
        if network is not None:
            body['network'] = network.value
        if date is not None:
            body['date'] = int(date //1)
        response = self.__http_client.post(url, body)
        return Proof(response['leaves'], response['nodes'], response['depth'], response['bitmap'], response['anchor'])

    def verifyProof(self, proof: Proof) -> Record:

        if not Proof.isValid(proof):
            raise ProofVerificationException(
                'Input Proof is not valid for a verification process.')
        leaves = proof.leaves
        hashes = proof.nodes
        depth_bytes = bytes.fromhex(proof.depth)
        depth = [int.from_bytes(depth_bytes[i*2:i*2+2], 'big')
                 for i in range(0, len(depth_bytes)//2)]
        bitmap = [b for b in bytes.fromhex(proof.bitmap)]

        it_leaves = 0
        it_hashes = 0
        stack = []

        while it_hashes < len(hashes) or it_leaves < len(leaves):
            act_depth = depth[it_hashes + it_leaves]

            if (bitmap[int((it_hashes + it_leaves) / 8)] & (1 << (7 - ((it_hashes + it_leaves) % 8)))) > 0:
                act_hash = hashes[it_hashes]
                it_hashes += 1
            else:
                act_hash = leaves[it_leaves]
                it_leaves += 1

            while len(stack) > 0 and stack[len(stack)-1][1] == act_depth:
                last_hash = stack.pop()
                act_hash = (Record.fromHex(last_hash[0] + act_hash).getHash())
                act_depth -= 1

            stack.append((act_hash, act_depth))
        return Record.fromHash(stack[0][0])

    def validateRoot(self, network: Network, root: Record) -> int:
        return self.__blockchain_client.validateRoot(network, root.getHash())
