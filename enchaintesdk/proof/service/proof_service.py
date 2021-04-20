from enchaintesdk.message.entity.message_entity import Message
from ..entity.proof_entity import Proof
from ..repository.proof_repository import ProofRepository
from enchaintesdk.message.entity.exception.invalid_message_exception import InvalidMessageException


class ProofService:

    def __init__(self, proof_repo: ProofRepository):
        self.__proof_repository = proof_repo

    def retrieveProof(self, messages: [Message]) -> Proof:
        if not messages:
            return None
        for m in messages:
            if not Message.isValid(m):
                raise InvalidMessageException(m.getHash())
        return self.__proof_repository.retrieveProof(messages)

    def verifyMessages(self, messages: [Message]) -> int:
        return self.verifyProof(self.retrieveProof(messages))

    def verifyProof(self, proof: Proof) -> int:
        if not proof:
            return None
        root = self.__proof_repository.verifyProof(proof)
        return self.__proof_repository.validateRoot(root)
