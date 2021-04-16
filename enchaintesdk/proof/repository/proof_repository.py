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

        leaves = proof.leaves
        for l in leaves:
            if not Utils.isHex(l) or len(l) != 64:
                raise ProofVerificationException(
                    'Proof leaves does contain the following value: "'+l +
                    'which is not a valid Message.')
        hashes = proof.nodes
        for h in hashes:
            if not Utils.isHex(h) or len(h) != 64:
                raise ProofVerificationException(
                    'Proof hashes does contain the following value: "'+h +
                    '"; which is not a valid Message.')
        n_elements = len(leaves)+len(hashes)

        if len(proof.depth) != (n_elements)*4:
            raise ProofVerificationException(
                'Proof depth does contain "'+str(len(proof.depth)) +
                ' elements, but were expected'+str(n_elements*4) +
                '. Depth values: '+proof.depth)
        depth_bytes = bytes.fromhex(proof.depth)
        depth = []
        for i in range(0, len(depth_bytes)//2):
            depth.append(int.from_bytes(depth_bytes[i*2:i*2+2], "big"))

        if len(proof.bitmap) < ((n_elements + n_elements % 8)//8):
            raise ProofVerificationException(
                'Proof bitmap requires at least ' +
                str(((n_elements + n_elements % 8)//8)) +
                ', but only contains ' + str(len(proof.bitmap)) +
                '. Proof bitmap value in hex: ' + proof.bitmap)
        bitmap = Utils.hexToUint8Array(proof.bitmap)

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
