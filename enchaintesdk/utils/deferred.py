class Deferred:
    def __init__(self, resolve, reject):
        self.resolve = resolve
        self.reject = reject
