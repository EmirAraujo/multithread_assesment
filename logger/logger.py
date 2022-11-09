import threading
import time

from service.repository.repository import Repository
from utils.network import Network


class Logging():
    """ Logging class, monitors network mesages and stores values to repository
    """
    def __init__(self, repository: Repository, network: Network):
        self.lock = threading.Lock()
        self.num_of_workers = 5
        self.workers = [Logger_worker(repository,network,self.lock,'logger_'+str(i)) for i in range(self.num_of_workers) ]
        [worker.start() for worker in self.workers]

    def stop_workers(self) -> None:
        [worker.stop() for worker in self.workers]

class Logger_worker(threading.Thread):
    """ Logger worker, get the las message in the network and save it in the repository
    """
    def __init__(self, repository: Repository, network: Network, lock:threading.Lock, name:str='1' ):
        super(Logger_worker, self).__init__(name = name)
        self.lock = lock
        self.repository: Repository = repository
        self.network: Network = network
        self.stop = False
    
    def stop(self) -> None:
        self.stop = True

    def run(self) -> None:
        while not self.stop:
             #You most save data present on network here, keep on mind that network could have at maximum 5 messages
            #at the time.
            self.lock.acquire()

            messages = self.network.pop_message()
            if messages != None and messages != 0:
                self.repository.save(messages)
            
            self.lock.release()                        
            time.sleep(1)


