class RecordReceipt:
    def __init__(self, anchor: int, client: str, record: str, status: str):
        self.anchor = anchor or 0
        self.client = client or ''
        self.record = record or ''
        self.status = status or 'Pending'
