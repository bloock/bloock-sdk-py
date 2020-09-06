from .utils.deferred import Deferred
from .entity.hash import Hash
from .comms.apiService import ApiService
from weakref import WeakValueDictionary


class Writer:
    """ Writer is a Singleton in charge of storing all hashes before been sent through
        Enchainte's API."""

    __instance = WeakValueDictionary()

    def __new__(cls, *args, **kwargs):
        if cls not in cls.__instance:
            instance = super(Writer, cls).__new__(cls, *args, **kwargs)
            cls.__tasks = {}
            cls.__instance[cls] = instance
        return cls.__instance[cls]

    def push(self, value, resolve, reject):
        ''' Adds a sigle new Hash ("value") to the dictionary "tasks" and returns its
            related Deferred object with "resolve"/"reject" as callbacks.'''

        deferred = Deferred(resolve, reject)
        self.__tasks[value] = deferred
        return deferred

    @staticmethod
    def send():
        ''' Sends to Enchainte API all Hashes stored inside "tasks", cleans the dictionary
            and updates the Deferred promise depending in if the related Hash was
            succesfully recived by the API or not.'''

        if not Writer.__tasks:
            return
        currentTasks = Writer.__tasks
        Writer.__tasks = {}

        dataToSend = []
        for key in currentTasks:
            dataToSend.append(key)

        try:
            writenTask = ApiService.write(dataToSend)
            for task in dataToSend:
                if task.getHash() in writenTask:
                    currentTasks[task].promise = True
                else:
                    currentTasks[task].promise = False
        except BaseException as e:
            for task in currentTasks:
                currentTasks[task].promise = False
                currentTasks[task].reject = e

    @staticmethod
    def getInstance():
        ''' Returns the singleton Writer instance.'''

        return Writer()
