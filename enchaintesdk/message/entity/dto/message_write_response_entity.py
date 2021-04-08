class MessageWriteResponse:
    def __init__(self, data):
        self.anchor = data.anchor
        self.client = data.client
        self.message = data.message
        self.status = data.status
