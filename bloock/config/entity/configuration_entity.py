class Configuration:
    ''' Object holder of all information related to
        configuring the connection with Bloock's
        API.
    '''

    def __init__(self):
        self.host = ""
        self.api_version = ""

        self.wait_record_interval_default = 1000

class NetworkConfiguration:
    ''' Object holder of all information related to
        configuring the connection with blockchain
        networks.
    '''
    
    def __init__(self):
        self.contract_address = ""
        self.contract_abi = ""
        self.http_provider = ""