class Message:

    def __init__(self, root, message, txHash, status, error):
        self.root = root
        self.message = message
        self.txHash = txHash
        self.status = status
        self.error = error
