from enchaintesdk.shared.enchainte_client_exception import EnchainteSDKException


class HttpRequestException(EnchainteSDKException):
    """ Attributes:
        -----------
        message -- message retrieved from Http response
    """

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'HttpClient response was not successful: {self.message}.'
