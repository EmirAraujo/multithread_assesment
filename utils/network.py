import threading
from datetime import datetime

from service.model.message import Message

class Network:
    """ Network class, message handling with a cicular buffer
    """
    def __init__(self,buffer_size=5):
        self.lock = threading.Lock()
        self.buffer = [ 0 for _ in range(5) ]
        self.index = 0
        self.buffer_size: int = buffer_size

    def send(self, message:Message):
        self.lock.acquire()

        self.buffer[self.index] = message
        self.index += 1
        if self.index > self.buffer_size-1:
            self.index = 0

        self.lock.release()

    def get_mesages(self):
        return [data for data in self.buffer if data != 0]

    def reset_buffer(self):
        self.lock.acquire()

        self.index = 0
        [ 0 for _ in range(5) ]

        self.lock.release()