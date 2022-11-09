from datetime import datetime

from service.model.message import Message

class Network:
    """ Network class, message handling LIFO stack
    """
    def __init__(self, buffer_size:int = 5):
        self.buffer_size: int = buffer_size
        self.buffer = [ 0 for _ in range(self.buffer_size) ]
        self.index = 0

    def send(self, message:Message) -> None:
        """ Send message to the network, can only retain 5 messages
        """

        self.buffer[self.index] = message
        if self.index >= self.buffer_size-1:
            self.buffer = self.buffer[1:]
            self.buffer.append(message)
        else:
            self.index += 1


    
    def pop_message(self):

        if self.index == -1:
            return 0
        print(self.index)
        ans = self.buffer[self.index]
        self.buffer[self.index] = 0
        self.index -= 1

        return ans



