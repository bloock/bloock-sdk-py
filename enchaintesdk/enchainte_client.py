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
from .message.entity.message_receipt_entity import MessageReceipt
from .message.entity.message_entity import Message
from .message.repository.message_repository import MessageRepository
from .message.service.message_service import MessageService
from .proof.entity.proof_entity import Proof
from .proof.repository.proof_repository import ProofRepository
from .proof.service.proof_service import ProofService


class EnchainteClient:
    ''' Entry-point to the Enchainté SDK

        This SDK offers all the features available in the Enchainté Toolset:
            * Write messages
            * Get messages proof
            * Validate proof
            * Get messages details
    '''

    def __init__(self, api_key: str, environment: ConfigEnv = ConfigEnv.PROD):
        ''' Constructor with API Key that enables accessing to 
            Enchainté's functionalities.

            Parameters
            ----------
            api_key : str
                Client API Key.
            environment: ConfigEnv (optional)
                Defines the Enchainté's environment to use. By default: production.
        '''
        config_repo = ConfigRepository(ConfigData())
        self.__config_service = ConfigService(config_repo)
        self.__config_service.setupEnvironment(environment)

        self.__http_client = HttpClient(HttpData(api_key))

        anchor_repo = AnchorRepository(
            self.__http_client, self.__config_service)
        self.__anchor_service = AnchorService(
            anchor_repo, self.__config_service)

        message_repo = MessageRepository(
            self.__http_client, self.__config_service)
        self.__message_service = MessageService(message_repo)

        proof_repo = ProofRepository(
            self.__http_client, Web3Client(self.__config_service), self.__config_service)
        self.__proof_service = ProofService(proof_repo)

    def sendMessages(self, messages: List[Message]) -> List[MessageReceipt]:
        ''' Sends a list of Message to Enchainté.

            Parameters
            ----------
            messages : [Message]
                List of Message to send.

            Returns
            -------
            [MessageReceipt]
                List of MessageReceipt of each Message sent.

            Exceptions
            ----------
            InvalidMessageException
                At least one of the messages sent was not well formed.
            HttpRequestException
                Error return by Enchainté's API.
        '''
        return self.__message_service.sendMessages(messages)

    def getMessages(self, messages: List[Message]) -> List[MessageReceipt]:
        ''' Retrieves all MessageReceipt for the specified Anchor.

            Parameters
            ----------
            messages : [Message]
                List of Message to fetch.

            Returns
            -------
            [MessageReceipt]
                List with the MessageReceipt of each message requested.

            Exceptions
            ----------
            InvalidMessageException
                At least one of the messages sent was not well formed.
            HttpRequestException
                Error return by Enchainté's API.
        '''
        return self.__message_service.getMessages(messages)

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
                Error return by Enchainté's API.
        '''
        return self.__anchor_service.getAnchor(anchor)

    def waitAnchor(self, anchor: int,  timeout: int = 120000) -> Anchor:
        ''' Waits until the anchor specified is confirmed in Enchainté.

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
                Error return by Enchainté's API.
        '''
        return self.__anchor_service.waitAnchor(anchor, timeout)

    def getProof(self, messages: List[Message]) -> Proof:
        ''' Retrieves an integrity Proof for the specified list of Message.

            Parameters
            ----------
            messages: [Message]
                List of messages to validate.

            Returns
            -------
            Proof/None 
                The Proof object containing the elements necessary to verify
                the integrity of the messages in the input list. If no
                message was requested, then returns None.

            Exceptions
            ----------
            InvalidMessageException
                At least one of the messages sent was not well formed.
            HttpRequestException
                Error return by Enchainté's API.
        '''
        return self.__proof_service.retrieveProof(messages)

    def verifyProof(self, proof: Proof) -> int:
        ''' Verifies if the specified integrity Proof is valid and checks if 
            it's currently included in the blockchain.

            Parameters
            ----------
            proof: Proof
                Proof to validate.

            Returns
            -------
            int
                A int contining the timestamp from when the messages where sent to blockchain.
                Its value is 0 not found.

            Exceptions
            ----------
            ProofVerificationException
                Error informing that at least one of the parameters of the Proof
                has not a valid value.
            Web3Exception
                Error connecting to blockchain.
        '''
        return self.__proof_service.verifyProof(proof)

    def verifyMessages(self, messages: List[Message]) -> int:
        ''' It retrieves a proof for the specified list of Anchor using getProof and
            verifies it using verifyProof.

            Parameters
            ----------
            messages: [Message]
                list of messages to validate

            Returns
            -------
            int
                A int contining the timestamp from when the messages where sent to blockchain.
                Its value is 0 not found.

            Exceptions
            ----------
            InvalidMessageException
                At least one of the messages sent was not well formed.
            HttpRequestException
                Error return by Enchainté's API.
            ProofVerificationException
                Error informing that at least one of the parameters of the Proof
                has not a valid value.
            Web3Exception
                Error connecting to blockchain.
        '''
        return self.__proof_service.verifyMessages(messages)
