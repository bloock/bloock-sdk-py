class RecordWriteResponse:
    def __init__(self, data):
        self.anchor = data.get('anchor', 0) or 0
        self.client = data.get('client', '') or ''
        self.records = data.get('messages', []) or []
        self.status = data.get('status', '') or ''
