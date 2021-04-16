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

    def __init__(self, api_key: str, environment: ConfigEnv = ConfigEnv.TEST, timeout: int = 120000):
        ''' Constructor with API Key that enables accessing to Enchainté's functionalities

            Parameters
            ----------
            api_key : str
                client API Key
            environment: ConfigEnv (optional)
                defines the Enchainté's environment to use. By default: production
        '''
        config_repo = ConfigRepository(ConfigData())
        self.__config_service = ConfigService(config_repo)
        self.__config_service.setupEnvironment(environment)

        self.__http_client = HttpClient(HttpData(api_key))

        anchor_repo = AnchorRepository(
            self.__http_client, self.__config_service)
        self.__anchor_service = AnchorService(
            anchor_repo, self.__config_service, timeout)

        message_repo = MessageRepository(
            self.__http_client, self.__config_service)
        self.__message_service = MessageService(message_repo)

        proof_repo = ProofRepository(
            self.__http_client, Web3Client(self.__config_service), self.__config_service)
        self.__proof_service = ProofService(proof_repo)

    def sendMessages(self, messages: [Message]) -> [MessageReceipt]:
        ''' Sends a list of Message to Enchainté

            Parameters
            ----------
            messages : [Message]
                list of Message to send

            Returns
            -------
            [MessageReceipt]
                list of MessageReceipt of each Message sent.
        '''
        return self.__message_service.sendMessages(messages)

    def getMessages(self, messages: [Message]) -> [MessageReceipt]:
        ''' Retrieves all MessageReceipt for the specified Anchor

            Parameters
            ----------
            messages : [Message]
                list of Message to fetch

            Returns
            -------
            [MessageReceipt]
        '''
        return self.__message_service.getMessages(messages)

    def getAnchor(self, anchor: int) -> Anchor:
        ''' Gets an specific anchor id details

            Parameters
            ----------
            anchor : int
                id of the Anchor to look for

            Returns
            -------
            Anchor
                Anchor object matching the id
        '''
        return self.__anchor_service.getAnchor(anchor)

    def waitAnchor(self, anchor: int) -> Anchor:
        ''' Waits until the anchor specified is confirmed in Enchainté

            Parameters
            ----------
            anchor : int
                id of the Anchor to wait for

            Returns
            -------
            Anchor
                Anchor object matching the id
        '''
        return self.__anchor_service.waitAnchor(anchor)

    def getProof(self, messages: [Message]) -> Proof:
        ''' Retrieves an integrity Proof for the specified list of Anchor

            Parameters
            ----------
            messages: [Message]
                list of messages to validate

            Returns
            -------
            Proof
        '''
        return self.__proof_service.retrieveProof(messages)

    # TODO: descorbir si realment és un int o no
    def verifyProof(self, proof: Proof) -> bool:
        ''' Verifies if the specified integrity [Proof] is valid and checks if 
            it's currently included in the blockchain.

            Parameters
            ----------
            proof: Proof
                Proof to validate

            Returns
            -------
            bool
                a [Boolean] that returns True if valid, False if not
        '''
        return self.__proof_service.verifyProof(proof)

    def verifyMessages(self, messages: [Message]) -> bool:
        ''' It retrieves a proof for the specified list of Anchor using getProof and
            verifies it using verifyProof.

            Parameters
            ----------
            messages: [Message]
                list of messages to validate

            Returns
            -------
            bool
                a [Boolean] that returns True if valid, False if not
        '''
        return self.__proof_service.verifyMessages(messages)
