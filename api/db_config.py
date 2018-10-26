
import os
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import Session
from sqlalchemy import create_engine
from api.dbmodels import Base
# SECRET_KEY = os.environ['SECRET_KEY']
SQLALCHEMY_DATABASE_URI = os.environ['SQLALCHEMY_URI']
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=False)
Base.metadata.create_all(bind=engine)


class Config:
    '''Database config'''
    def __init__(self):
        self.db_session = self.session

    @property
    def session(self):

        session_maker = sessionmaker()
        session_maker.configure(bind=engine)
        session = session_maker()
        return session
