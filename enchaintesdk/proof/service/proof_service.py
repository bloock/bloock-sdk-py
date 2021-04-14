from enchaintesdk.message.entity.message_entity import Message
from ..entity.proof_entity import Proof
from ..repository.proof_repository import ProofRepository


class ProofService:

    def __init__(self, proof_repo: ProofRepository):
        self.__proof_repository = proof_repo

    def retrieveProof(self, messages: [Message]) -> Proof:
        s = Message.sort(messages)
        return self.__proof_repository.retrieveProof(s)

    def verifyMessages(self, messages: [Message]) -> int:
        proof = self.retrieveProof(messages)
        if proof == None:
            raise Exception("Couldn't get proof for specified messages")
        return self.verifyProof(proof)

    def verifyProof(self, proof: Proof) -> int:
        root = self.__proof_repository.verifyProof(proof)
        if root == None:
            raise Exception("The provided proof is invalid")
        return self.__proof_repository.validateRoot(root)
