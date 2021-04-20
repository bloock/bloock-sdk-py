from enchaintesdk.infrastructure.hashing.keccak import Keccak
from enchaintesdk.shared.utils import Utils


class Message:
    ''' Message is the class in charge of computing and storing the
        value of the data sent to Enchainté.

        This class is intended to be used by calling "from" static
        methods to create instances of Message.
    '''
    __hashAlgorithm = Keccak()

    def __init__(self, hash: str):
        self.__hash = hash

    @staticmethod
    def fromDict(data: dict):
        ''' Given a dictionary returns a Message with its value hashed.

            Parameters
            ----------
            data : dict
                Dictionary to convert to Message.

            Returns
            -------
            Message
                Message object of the hashed input.
        '''
        return Message.fromString(Utils.stringify(data))

    @staticmethod
    def fromHash(hash: str):
        ''' Given a value already hashed creates a Message containing it.

            Parameters
            ----------
            hash : str
                Hexadecimal string without prefix and length 64.

            Returns
            -------
            Message
                Message object of the hashed input.
        '''
        return Message(hash)

    @staticmethod
    def fromHex(hex: str):
        ''' Given a hexadecimal string (with no 0x prefix) returns a 
            Message with its value hashed.

            Parameters
            ----------
            hex : str
                Hexadecimal string without prefix.

            Returns
            -------
            Message
                Message object of the hashed input.
        '''
        dataArray = bytes.fromhex(hex)
        return Message(Message.__hashAlgorithm.generateHash(dataArray))

    @staticmethod
    def fromString(string: str):
        ''' Given a string returns a Message with its value hashed.

            Parameters
            ----------
            string : str
                String object.

            Returns
            -------
            Message
                Message object of the hashed input.
        '''
        dataArray = Utils.stringToBytes(string)
        return Message(Message.__hashAlgorithm.generateHash(dataArray))

    @staticmethod
    def fromBytes(b: bytes):
        ''' Given a bytes object returns a Message with its value hashed.

            Parameters
            ----------
            b : bytes
                Bytes object.

            Returns
            -------
            Message
                Message object of the hashed input.
        '''
        return Message(Message.__hashAlgorithm.generateHash(b))

    @staticmethod
    def isValid(message) -> bool:
        ''' Given a Message returns True if its contents are valid to be
            sent to Enchainté's API or False otherwise.

            Parameters
            ----------
            message : Message
                Message object.

            Returns
            -------
            bool
                Boolean indicating if the Message is susceptible to be sent
                (True) or not (False).
        '''
        if isinstance(message, Message):
            _message = message.getHash()

            if (len(_message) == 64 and Utils.isHex(_message)):
                return True
        return False

    def getHash(self) -> str:
        ''' Returns the hashed representation of the Message string.

            Returns
            -------
            str
                String containing the Message hash as a hexadecimal 
                (with no "0x" prefix).
        '''
        return self.__hash
