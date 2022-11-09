from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.orm import validates
from sqlalchemy.orm import declarative_base
Base = declarative_base()

class Message(Base):
    """ Message ORM model, data declaration and data validation
    """
    __tablename__ = 'message'
    
    timestamp = Column(DateTime , primary_key=True)
    id = Column(Integer)
    sensor_name = Column(String, nullable=False)
    value = Column(Integer, nullable=False)

    def __init__(self, timestamp:datetime, id:int, sensor_name:str, value:int):
        super(Message, self).__init__()
        self.timestamp = timestamp
        self.id = id
        self.sensor_name = sensor_name
        self.value = self.validate_value('value',value)


    @validates('value')
    def validate_value(self, key, value) -> None:
        assert value >= -100 and value <= 100, f"ERROR: valor out of range :{value}"
        return value

        
