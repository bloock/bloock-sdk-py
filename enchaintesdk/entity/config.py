class Config:
    def __init__(self, host, write_endpoint, proof_endpoint, fetch_endpoint,
        http_provider, contract_address, contract_abi, provider, write_interval,
        config_interval, wait_message_interval_factor, wait_message_interval_default):

        self.host = host
        self.write_endpoint = write_endpoint
        self.proof_endpoint = proof_endpoint
        self.fetch_endpoint = fetch_endpoint
        self.http_provider = http_provider
        self.contract_address = contract_address
        self.contract_abi = contract_abi
        self.provider = provider
        self.write_interval = int(write_interval)/1000
        self.config_interval = int(config_interval)/1000
        self.wait_message_interval_factor = wait_message_interval_factor
        self.wait_message_interval_default = int(wait_message_interval_default)/1000