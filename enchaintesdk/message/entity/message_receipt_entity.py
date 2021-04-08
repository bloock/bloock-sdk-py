class MessageReceipt:
    def __init__(self, anchor: int, client: str, message: str, status: str):
        self.anchor = anchor
        self.client = client
        self.message = message
        self.status = status
