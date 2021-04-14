class AnchorNotFoundException(Exception):
    """ Attributes:
        -----------
        id -- anchor id
    """

    def __init__(self, id):
        self.id = id
        self.message = 'Anchor not found'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}. Anchord identifier: {self.id}.'
