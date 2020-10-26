import interface


class api(interface.Interface):
    @staticmethod
    def write(dataH):
        pass

    @staticmethod
    def getProof(dataH):
        pass

    @staticmethod
    def getMessages(dataH):
        pass


class Web3(interface.Interface):

    @staticmethod
    def validateRoot(root):
        pass


class ConfigService(interface.Interface):

    def __init__(self):
        pass

    def fetchConfig(self):
        pass

    def setTestEnvironment(self, isTest):
        pass

    def getConfig(self):
        pass

    def __getAuthHeaders(self, url, body):
        pass
