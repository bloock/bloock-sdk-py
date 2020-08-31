from enchaintesdk.writer import Writer
import threading
import time


class WriterTimer:
    ''' This class requieres a "Writer" object in its initialization, and 
        executes its writer.send() in intervals of "seconds" seconds. It
        can be stopped though calling the cancel function,'''

    def __init__(self, seconds):
        self.interval = seconds
        self.__writer = Writer.getInstance()
        self.stopEvent = threading.Event()
        thread = threading.Thread(target=self.__setInterval)
        thread.start()

    def __setInterval(self):
        nextTime = time.time()+self.interval
        while not self.stopEvent.wait(nextTime-time.time()):
            nextTime += self.interval
            self.__writer.send()

    def cancel(self):
        self.stopEvent.set()
