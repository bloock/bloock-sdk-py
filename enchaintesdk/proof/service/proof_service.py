from enchaintesdk.message.entity.message_entity import Message
from ..entity.proof_entity import Proof
from ..repository.proof_repository import ProofRepository


class ProofService:

    def __init__(self, proof_repo: ProofRepository):
        self.__proof_repository = proof_repo

    def retrieveProof(self, messages: [Message]) -> Proof:
        return self.__proof_repository.retrieveProof(messages)

    def verifyMessages(self, messages: [Message]) -> int:
        return self.verifyProof(self.retrieveProof(messages))

    def verifyProof(self, proof: Proof) -> int:
        root = self.__proof_repository.verifyProof(proof)
        return self.__proof_repository.validateRoot(root)
