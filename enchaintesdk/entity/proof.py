from ..utils.utils import Utils
from ..entity.message import Message


class Proof:
    def __init__(self, leaves, nodes, depth, bitmap):
        self.leaves = leaves
        self.nodes = nodes
        self.depth = depth
        self.bitmap = bitmap

    def isValid(self):
        for l in self.leaves:
            if not Message(l).isValid():
                return False
        for n in self.nodes:
            if not (len(n) == 64 and Utils.is_hex(n)):
                return False
        return len(self.depth)/2 == (len(self.leaves)+len(self.nodes))
