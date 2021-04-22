from enchaintesdk.shared.enchainte_client_exception import EnchainteSDKException


class ProofVerificationException(EnchainteSDKException):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'
