from typing import List
from bloock.record.entity.record_entity import Record
from ..entity.proof_entity import Proof
from ..repository.proof_repository import ProofRepository
from bloock.record.entity.exception.invalid_record_exception import InvalidRecordException
from bloock.config.entity.networks_entity import Network

class ProofService:

    def __init__(self, proof_repo: ProofRepository):
        self.__proof_repository = proof_repo

    def retrieveProof(self, records: List[Record]) -> Proof:
        if not records:
            return None
        for m in records:
            if not Record.isValid(m):
                raise InvalidRecordException(m.getHash())
        return self.__proof_repository.retrieveProof(records)

    def verifyRecords(self, records: List[Record], network: Network) -> int:
        return self.verifyProof(self.retrieveProof(records), network)

    def verifyProof(self, proof: Proof, network: Network) -> int:
        if not proof:
            return None
        root = self.__proof_repository.verifyProof(proof)
        return self.__proof_repository.validateRoot(network, root)
