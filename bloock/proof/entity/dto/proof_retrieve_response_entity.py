class ProofRetrieveResponse:
    def __init__(self, data):
        self.nodes = data.nodes
        self.depth = data.depth
        self.bitmap = data.bitmap
