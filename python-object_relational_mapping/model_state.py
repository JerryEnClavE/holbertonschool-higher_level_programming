#!/usr/bin/python3
"""task 6"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """class defining starte"""
    __tablename__ = "states"
    id = Column("id", Integer, autoincrement=True, primary_key=True)
    name = Column("name", String(128), nullable=False)
    cities = relationship("City", back_populates="state")
