from .utils.deferred import Deferred
from .utils.utils import Utils
from .comms.configService import ConfigService
from .entity.message import Message
from .comms.apiService import ApiService
from weakref import WeakValueDictionary


class Writer:
    """ Writer is a Singleton in charge of storing all messages before been sent through
        Enchainte's API."""

    __instance = WeakValueDictionary()
    __config = [None]

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
    @Utils.periodic_task(2) #will need to be update to write interval
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
            writenTask = ApiService.write(dataToSend, Writer.__config[0])
            for task in dataToSend:
                if task.getMessage() in writenTask:
                    currentTasks[task].resolve()
                else:
                    currentTasks[task].reject(BaseException('Element with message "' + task + '" was not sent to Enchainte'))
        except BaseException as e:
            for task in currentTasks:
                currentTasks[task].reject(e)

    @staticmethod
    def getInstance():
        ''' Returns the singleton Writer instance.'''

        return Writer()

    
    def get_config(self):
        return self.__config[0]
    
    @staticmethod
    def set_config(c):
        Writer.__config = c 