from ..utils.utils import Utils
from ..entity.hash import Hash


class Proof:
    def __init__(self, leaves, nodes, depth, bitmap):
        self.leaves = leaves
        self.nodes = nodes
        self.depth = depth
        self.bitmap = bitmap
        self.root = None

    def isValid(self):
        # if self.root == None:
        #    return False
        for l in self.leaves:
            if not Hash(l).isValid():
                return False
        for n in self.nodes:
            if not (len(n) == 64 and Utils.is_hex(n)):
                return False
        # if not (len(self.root) == 64 and Utils.is_hex(self.root)):
        #    return False
        return len(self.depth)/2 == (len(self.leaves)+len(self.nodes))

    def setRoot(self, root):
        self.root = root
