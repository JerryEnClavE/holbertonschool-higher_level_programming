#!/usr/bin/python3
"""Defines the State class and an instance of declarative_base for ORM"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
import sys

# Create instance of declarative base
Base = declarative_base()

class State(Base):
    """State class that links to the MySQL table `states`"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Connect to MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True
    )
    # Create all tables in the engine
    Base.metadata.create_all(engine)
