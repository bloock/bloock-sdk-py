class Deferred:
    def __init__(self, resolve, reject):
        self.promise = None
        self.resolve = resolve
        self.reject = reject

    def getPromise(self):
        if self.promise:
            return self.resolve
        return self.reject
