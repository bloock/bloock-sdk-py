class Deferred:
    def __init__(self, resolve, reject):
        self.promise = None
        self.__resolve = resolve
        self.__reject = reject

    def getPromise(self):
        if self.promise:
            return self.__resolve
        return self.__reject
