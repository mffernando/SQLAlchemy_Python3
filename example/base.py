# coding=utf-8

#Main Class

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#SQLAlchemy engine interact with dockerized PostgreSQL database
engine = create_engine('postgresql://postgres:password@localhost:5432/sqlalchemy')
#SQLAlchemy ORM session factory engine
Session = sessionmaker(bind=engine)
#base class for classes definitions
Base = declarative_base()