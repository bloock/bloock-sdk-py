class ApiResponse:
    def __init__(self, data):
        self.success = data['success']
        self.data = data['data']
