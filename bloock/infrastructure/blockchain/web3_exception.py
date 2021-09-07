from bloock.shared.bloock_client_exception import BloockException


class Web3Exception(BloockException):
    """ Attributes:
        -----------
        record -- record retrieved from Web3 response
    """

    def __init__(self, record):
        self.record = record
        super().__init__(self.record)

    def __str__(self):
        return f'HttpClient response was not successful: {self.record}.'
