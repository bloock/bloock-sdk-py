from .utils.utils import SetInterval
from .utils.constants import SEND_INTERVAL
from .utils.deferred import Deferred
from .entity.hash import Hash
from .comms.apiService import ApiService


class Writer:
    __instance = None
    __tasks = {}

    def __init__(self):
        if self.__instance == None:
            SetInterval(SEND_INTERVAL, self)

    @staticmethod
    def getInstance():
        if Writer.__instance == None:
            return Writer()
        return Writer.__instance

    def push(self, value, resolve, reject):
        deferred = Deferred(resolve, reject)
        self.__tasks[value] = deferred
        return deferred

    @staticmethod
    def send():
        if not Writer.__tasks:
            return
        currentTasks = Writer.__tasks
        Writer.__tasks = {}

        dataToSend = []
        for key in currentTasks:
            dataToSend.append(key.getHash())

        try:
            ApiService.write(dataToSend)
            for task in currentTasks:
                task.promise = True
        except:
            for task in currentTasks:
                task.promise = False
