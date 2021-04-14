class EmptyProofStackException(Exception):

    def __init__(self):
        self.message = 'Verify: Stack got empty before capturing its value.'
        super().__init__(self.message)

    def __str__(self):
        return f'{self.message}'
