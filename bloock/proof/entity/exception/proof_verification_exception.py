from bloock.shared.bloock_client_exception import BloockException


class ProofVerificationException(BloockException):
    def __init__(self, record: str):
        self.record = record
        super().__init__(self.record)

    def __str__(self):
        return f'{self.record}'
