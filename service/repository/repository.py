from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from service.model.message import Message

class Repository:
    """ db class, handle records to files o SQL databases
    """
    def __init__(self, db_type_str:str = 'sqlite:///sensors.sqlite'):
        self.engine = create_engine(db_type_str)#, echo=True, future=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        Message.metadata.create_all(self.engine)


    def save(self, message: Message):  
        if isinstance(message, list):
            for m in message:
                self.session.add(m)
        else:
            self.session.add(message)
        self.session.commit()
        