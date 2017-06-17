import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    name = Column(String(250), nullable=False, unique=True)
    id = Column(Integer, primary_key=True)
    favorite_color = Column(String(250))
    cats_or_dog = Column(String(250))


engine = create_engine('sqlite:///lista_herramienta.db')


Base.metadata.create_all(engine)