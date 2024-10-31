#!/usr/bin/python3
"""task 14"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import Base


class City(Base):
    """class defining starte"""
    __tablename__ = "cities"
    id = Column("id", Integer, autoincrement=True, primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column(
        "state_id", Integer, ForeignKey("states.id"), nullable=False)
    state = relationship("State", back_populates="cities")
