from typing import List
from .anchor.entity.anchor_entity import Anchor
from .anchor.repository.anchor_repository import AnchorRepository
from .anchor.service.anchor_service import AnchorService
from .config.entity.config_env_entity import ConfigEnv
from .config.repository.config_data import ConfigData
from .config.repository.config_repository import ConfigRepository
from .config.service.config_service import ConfigService
from .infrastructure.blockchain.web3 import Web3Client
from .infrastructure.http.http_data import HttpData
from .infrastructure.http.http_client import HttpClient
from .record.entity.record_receipt_entity import RecordReceipt
from .record.entity.record_entity import Record
from .record.repository.record_repository import RecordRepository
from .record.service.record_service import RecordService
from .proof.entity.proof_entity import Proof
from .proof.repository.proof_repository import ProofRepository
from .proof.service.proof_service import ProofService
from .config.entity.configuration_entity import NetworkConfiguration
from .config.entity.networks_entity import Network

class BloockClient:
    ''' Entry-point to the Bloock SDK

        This SDK offers all the features available in the Bloock Toolset:
            * Write records
            * Get records proof
            * Validate proof
            * Get records details
    '''

    def __init__(self, api_key: str):
        ''' Constructor with API Key that enables accessing to 
            Bloock's functionalities.

            Parameters
            ----------
            api_key : str
                Client API Key.
        '''
        config_repo = ConfigRepository(ConfigData())
        self.__config_service = ConfigService(config_repo)

        self.__http_client = HttpClient(HttpData(api_key))

        anchor_repo = AnchorRepository(
            self.__http_client, self.__config_service)
        self.__anchor_service = AnchorService(
            anchor_repo, self.__config_service)

        record_repo = RecordRepository(
            self.__http_client, self.__config_service)
        self.__record_service = RecordService(record_repo)

        proof_repo = ProofRepository(
            self.__http_client, Web3Client(self.__config_service), self.__config_service)
        self.__proof_service = ProofService(proof_repo)

    def setApiHost(self, host: str):
        ''' Replaces the default Bloock api host for the specified one.
            
            Parameters
            ----------
            host : str
                New host URL.
        '''
        self.__config_service.setApiHost(host)

    def setNetworkConfiguration(self, network: Network, configuration: NetworkConfiguration):
        ''' Overrides the default Network configuration.
            
            Parameters
            ----------
            network : Network
                .
            configuration: networkConfiguration
                .
            
        '''
        return self.__config_service.setNetworkConfiguration(network, configuration)

    def sendRecords(self, records: List[Record]) -> List[RecordReceipt]:
        ''' Sends a list of Record to Bloock.

            Parameters
            ----------
            records : List[Record]
                List of Record to send.

            Returns
            -------
            [RecordReceipt]
                List of RecordReceipt of each Record sent.

            Exceptions
            ----------
            InvalidRecordException
                At least one of the records sent was not well formed.
            HttpRequestException
                Error return by Bloock's API.
        '''
        return self.__record_service.sendRecords(records)

    def getRecords(self, records: List[Record]) -> List[RecordReceipt]:
        ''' Retrieves all RecordReceipt for the specified Anchor.

            Parameters
            ----------
            records : List[Record]
                List of Record to fetch.

            Returns
            -------
            List[RecordReceipt]
                List with the RecordReceipt of each record requested.

            Exceptions
            ----------
            InvalidRecordException
                At least one of the records sent was not well formed.
            HttpRequestException
                Error return by Bloock's API.
        '''
        return self.__record_service.getRecords(records)

    def getAnchor(self, anchor: int) -> Anchor:
        ''' Gets an specific anchor id details.

            Parameters
            ----------
            anchor : int
                Id of the Anchor to look for.

            Returns
            -------
            Anchor
                Anchor object matching the id.

            Exceptions
            ----------
            TypeError
                Informs that the input is not an int.
            HttpRequestException
                Error return by Bloock's API.
        '''
        return self.__anchor_service.getAnchor(anchor)

    def waitAnchor(self, anchor: int,  timeout: int = 120000) -> Anchor:
        ''' Waits until the anchor specified is confirmed in Bloock.

            Parameters
            ----------
            anchor : int
                Id of the Anchor to wait for.
            timeout (optional): int 
                Timeout time in miliseconds. After exceeding this time 
                returns a None.

            Returns
            -------
            Anchor
                Anchor object matching the id.

            Exceptions
            ----------
            TypeError
                Informs that the input is not an int.
            HttpRequestException
                Error return by Bloock's API.
        '''
        return self.__anchor_service.waitAnchor(anchor, timeout)

    def getProof(self, records: List[Record]) -> Proof:
        ''' Retrieves an integrity Proof for the specified list of Record.

            Parameters
            ----------
            records: List[Record]
                List of records to validate.

            Returns
            -------
            Proof/None 
                The Proof object containing the elements necessary to verify
                the integrity of the records in the input list. If no
                record was requested, then returns None.

            Exceptions
            ----------
            InvalidRecordException
                At least one of the records sent was not well formed.
            HttpRequestException
                Error return by Bloock's API.
        '''
        return self.__proof_service.retrieveProof(records)

    def verifyProof(self, proof: Proof, network: Network = Network.ETHEREUM_MAINNET) -> int:
        ''' Verifies if the specified integrity Proof is valid and checks if 
            it's currently included in the blockchain.

            Parameters
            ----------
            proof: Proof
                Proof to validate.
            network: Network
                Blockchain network where the proof will be validated.
            
            Returns
            -------
            int
                A int contining the timestamp from when the records where sent to blockchain.
                Its value is 0 not found.

            Exceptions
            ----------
            ProofVerificationException
                Error informing that at least one of the parameters of the Proof
                has not a valid value.
            Web3Exception
                Error connecting to blockchain.
        '''
        return self.__proof_service.verifyProof(proof, network)

    def verifyRecords(self, records: List[Record], network: Network = Network.ETHEREUM_MAINNET) -> int:
        ''' It retrieves a proof for the specified list of Anchor using getProof and
            verifies it using verifyProof.

            Parameters
            ----------
            records: List[Record]
                List of records to validate
            network: Network
                Blockchain network where the proof will be validated.
            
            Returns
            -------
            int
                A int contining the timestamp from when the records where sent to blockchain.
                Its value is 0 not found.

            Exceptions
            ----------
            InvalidRecordException
                At least one of the records sent was not well formed.
            HttpRequestException
                Error return by Bloock's API.
            ProofVerificationException
                Error informing that at least one of the parameters of the Proof
                has not a valid value.
            Web3Exception
                Error connecting to blockchain.
        '''
        return self.__proof_service.verifyRecords(records, network)
