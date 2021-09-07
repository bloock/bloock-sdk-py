from bloock.infrastructure.hashing.keccak import Keccak
from bloock.shared.utils import Utils


class Record:
    ''' Record is the class in charge of computing and storing the
        value of the data sent to Bloock.

        This class is intended to be used by calling "from" static
        methods to create instances of Record.
    '''
    __hashAlgorithm = Keccak()

    def __init__(self, hash: str):
        self.__hash = hash

    @staticmethod
    def fromDict(data: dict):
        ''' Given a dictionary returns a Record with its value hashed.

            Parameters
            ----------
            data : dict
                Dictionary to convert to Record.

            Returns
            -------
            Record
                Record object of the hashed input.
        '''
        return Record.fromString(Utils.stringify(data))

    @staticmethod
    def fromHash(hash: str):
        ''' Given a value already hashed creates a Record containing it.

            Parameters
            ----------
            hash : str
                Hexadecimal string without prefix and length 64.

            Returns
            -------
            Record
                Record object of the hashed input.
        '''
        return Record(hash)

    @staticmethod
    def fromHex(hex: str):
        ''' Given a hexadecimal string (with no 0x prefix) returns a 
            Record with its value hashed.

            Parameters
            ----------
            hex : str
                Hexadecimal string without prefix.

            Returns
            -------
            Record
                Record object of the hashed input.
        '''
        dataArray = bytes.fromhex(hex)
        return Record(Record.__hashAlgorithm.generateHash(dataArray))

    @staticmethod
    def fromString(string: str):
        ''' Given a string returns a Record with its value hashed.

            Parameters
            ----------
            string : str
                String object.

            Returns
            -------
            Record
                Record object of the hashed input.
        '''
        dataArray = Utils.stringToBytes(string)
        return Record(Record.__hashAlgorithm.generateHash(dataArray))

    @staticmethod
    def fromBytes(b: bytes):
        ''' Given a bytes object returns a Record with its value hashed.

            Parameters
            ----------
            b : bytes
                Bytes object.

            Returns
            -------
            Record
                Record object of the hashed input.
        '''
        return Record(Record.__hashAlgorithm.generateHash(b))

    @staticmethod
    def isValid(record) -> bool:
        ''' Given a Record returns True if its contents are valid to be
            sent to Bloocks's API or False otherwise.

            Parameters
            ----------
            record : Record
                Record object.

            Returns
            -------
            bool
                Boolean indicating if the Record is susceptible to be sent
                (True) or not (False).
        '''
        if isinstance(record, Record):
            _record = record.getHash()

            if (len(_record) == 64 and Utils.isHex(_record)):
                return True
        return False

    def getHash(self) -> str:
        ''' Returns the hashed representation of the Record string.

            Returns
            -------
            str
                String containing the Record hash as a hexadecimal 
                (with no "0x" prefix).
        '''
        return self.__hash
