from .network_entity import Network
from typing import List

class Anchor:
    def __init__(self, anchor_id: int, block_roots: str, networks: List[Network], root: str, status: str):
        self.id = anchor_id
        self.block_roots = block_roots
        self.networks = networks
        self.root = root
        self.status = status
