class InvalidMessageException(Exception):
    """ Attributes:
        -----------
        hash -- message hash
    """

    def __init__(self, hash):
        self.hash = hash
        self.message = 'Message not valid'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}. Message hash: {self.hash}.'
