from bloock.shared.bloock_client_exception import BloockException


class HttpRequestException(BloockException):
    """ Attributes:
        -----------
        record -- record retrieved from Http response
    """

    def __init__(self, record):
        self.record = record
        super().__init__(self.record)

    def __str__(self):
        return f'HttpClient response was not successful: {self.record}.'
