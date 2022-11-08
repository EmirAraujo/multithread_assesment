from threading import Thread
import time
from random import randint
from datetime import datetime

from utils.network import Network
from service.model.message import Message

class BaseSensor():
    """ Sensort manager, handle sensors creations and stops
    """
    def __init__(self, network: Network):
        self.num_of_sensors = 5
        self.network : Network = network   
        self.sensors = [Sensor(f'sensor_{i}',self.network,i) for i in range(self.num_of_sensors)]
        [sensor.start() for sensor in self.sensors]
        
    def stop(self):
        [sensor.stop() for sensor in self.sensors]

    
class Sensor(Thread):
    """ Sensor class, send message every 5 second to the network 
    """
    def __init__(self, sensor_name:str, network: Network,id:int =0):
        super(Sensor, self).__init__( name = sensor_name)
        self.network : Network = network   
        self.stop = False
        self.id = id

    def stop(self):
        self.stop = True

    def __get_value(self):
        return randint(-100,100)

    def run(self) -> None:
        while not self.stop:
            time.sleep(5)
            print(f"sending info from {self.name}")
            message = Message(datetime.now(), self.id, self.name, self.__get_value())
            self.network.send(message)

