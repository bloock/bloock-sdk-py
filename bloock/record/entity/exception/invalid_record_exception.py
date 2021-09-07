from bloock.shared.bloock_client_exception import BloockException


class InvalidRecordException(BloockException):
    """ Attributes:
        -----------
        hash -- record hash
    """

    def __init__(self, hash):
        self.hash = hash
        self.record = 'Record not valid'
        super().__init__(self.record)

    def __str__(self):
        return f'{self.record}. Record hash: {self.hash}.'
