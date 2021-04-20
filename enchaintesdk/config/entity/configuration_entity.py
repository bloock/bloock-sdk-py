class Configuration:
    ''' Object holder of all information related to
        configuring the connection with Enchainte's
        API.
    '''

    def __init__(self):
        self.host = ""
        self.api_version = ""
        self.contract_address = ""
        self.contract_abi = ""
        self.http_provider = ""
        self.wait_message_interval_default = 1000
