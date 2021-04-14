from ..network_entity import Network


class AnchorRetrieveResponse:
    def __init__(self, anchor_id: int, block_roots: str, networks: [Network], root: str, status: str):
        self.anchor_id = anchor_id
        self.block_roots = block_roots
        self.networks = [Network(n.name, n.state, n.tx_hash) for n in networks]
        self.root = root
        self.status = status
