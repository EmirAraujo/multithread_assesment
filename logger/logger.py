import threading
import time

from service.repository.repository import Repository
from utils.network import Network


class Logging(threading.Thread):
    """ Logging class, monitors network mesages and stores values to repository
    """
    def __init__(self, repository: Repository, network: Network):
        super(Logging, self).__init__()
        self.repository: Repository = repository
        self.network: Network = network
    #def

    def run(self) -> None:
        while True:
             #You most save data present on network here, keep on mind that network could have at maximum 5 messages
            #at the time.
            messages = self.network.get_mesages()

            self.repository.save(messages)
            
            self.network.reset_buffer()
            
            time.sleep(1)

