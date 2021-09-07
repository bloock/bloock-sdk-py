from bloock.shared.utils import Utils
from typing import List

class Proof:
    ''' Proof is the object in charge of storing all data necessary to compute
        a data integrity check.
    '''

    def __init__(self, leaves: List[str], nodes: List[str], depth: str, bitmap: str):
        self.leaves = leaves
        self.nodes = nodes
        self.depth = depth
        self.bitmap = bitmap

    @staticmethod
    def isValid(proof) -> bool:
        ''' Checks whether the Proof was build with valid parameters or not.

            Parameters
            ----------
            proof: Proof
                Proof to validate.

            Returns
            -------
            bool
                A Boolean that returns True if the proof is valid, False if not.
        '''
        if isinstance(proof, Proof):
            try:
                for l in proof.leaves:
                    if not Utils.isHex(l) or len(l) != 64:
                        return False
                for n in proof.nodes:
                    if not Utils.isHex(n) or len(n) != 64:
                        return False
                if (len(proof.depth) != (len(proof.leaves)+len(proof.nodes))*4) \
                        and Utils.isHex(proof.depth):
                    return False

                n_elements = len(proof.leaves)+len(proof.nodes)
                if len(proof.depth) != (n_elements)*4:
                    return False
                offset = 1
                if n_elements % 8 == 0:
                    offset = 0
                if len(proof.bitmap)//2 < ((n_elements + 8*offset - n_elements % 8)//8):
                    return False

                return True
            except Exception:
                return False
        return False
