

'''database models in sql alchemy'''



from sqlalchemy import Column, Integer, String, ARRAY, Boolean
from sqlalchemy.types import TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from .dictalchemy import DictAlchemy
Base = declarative_base()

class CustomElementTable(Base):
    __tablename__ = 'custom_element'
    id = Column(Integer, primary_key=True)
    el_id = Column(String, unique=True)
    el_complete = Column(Boolean, default=False)
    attributes = Column(DictAlchemy())
    text = Column(String)
    parent_id =Column(String)
    file_path = Column( String)
    file_type = Column( String)