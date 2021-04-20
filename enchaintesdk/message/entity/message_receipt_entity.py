class MessageReceipt:
    def __init__(self, anchor: int, client: str, message: str, status: str):
        self.anchor = anchor or 0
        self.client = client or ''
        self.message = message or ''
        self.status = status or 'Pending'
