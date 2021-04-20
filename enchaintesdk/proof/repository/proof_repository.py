from enchaintesdk.config.service.config_service import ConfigService
from enchaintesdk.infrastructure.blockchain.web3 import Web3Client
from enchaintesdk.infrastructure.http.http_client import HttpClient
from enchaintesdk.message.entity.message_entity import Message
from enchaintesdk.shared.utils import Utils
from ..entity.dto.proof_retrieve_request_entity import ProofRetrieveRequest
from ..entity.proof_entity import Proof
from ..entity.exception.proof_verification_exception import ProofVerificationException


class ProofRepository:

    def __init__(self, http_client: HttpClient, blockchain_client, config_service: ConfigService):
        self.__http_client = http_client
        self.__blockchain_client = blockchain_client
        self.__config_service = config_service

    def retrieveProof(self, messages: [Message]) -> Proof:
        url = f'{self.__config_service.getApiBaseUrl()}/messages/proof'
        body = {'messages': [m.getHash() for m in messages]}
        response = self.__http_client.post(url, body)
        return Proof(response.data['leaves'], response.data['nodes'], response.data['depth'], response.data['bitmap'])

    def verifyProof(self, proof: Proof) -> Message:

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
                act_hash = (Message.fromHex(last_hash[0] + act_hash).getHash())
                act_depth -= 1

            stack.append((act_hash, act_depth))
        return Message.fromHash(stack[0][0])

    def validateRoot(self, root: Message) -> int:
        return self.__blockchain_client.validateRoot(root.getHash())
