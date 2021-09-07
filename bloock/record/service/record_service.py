from typing import List
from ..entity.exception.invalid_record_exception import InvalidRecordException
from ..entity.record_receipt_entity import RecordReceipt
from ..entity.record_entity import Record
from ..repository.record_repository import RecordRepository


class RecordService:

    def __init__(self, record_repository: RecordRepository):
        self.__record_repo = record_repository

    def sendRecords(self, records: List[Record]) -> List[RecordReceipt]:
        if (len(records) == 0):
            return []

        for m in records:
            if not Record.isValid(m):
                raise InvalidRecordException(m.getHash())

        r = self.__record_repo.sendRecords(records)
        return [RecordReceipt(r.anchor, r.client, m, r.status) for m in r.records]

    def getRecords(self, records: List[Record]) -> List[RecordReceipt]:
        if (len(records) == 0):
            return []

        for m in records:
            if not Record.isValid(m):
                raise InvalidRecordException(m.getHash())
        return self.__record_repo.fetchRecords(records)
