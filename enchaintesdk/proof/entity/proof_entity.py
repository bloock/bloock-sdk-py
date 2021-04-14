class Proof:
    def __init__(self, leaves: [str], nodes: [str], depth: str, bitmap: str):
        self.leaves = leaves
        self.nodes = nodes
        self.depth = depth
        self.bitmap = bitmap

    # TODO: canviar perquè validi millor
    @staticmethod
    def isValid(proof) -> bool:
        if isinstance(proof, Proof):
            return True
        return False
