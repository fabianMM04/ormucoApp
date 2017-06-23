from sqlalchemy import Column, ForeignKey, Integer, String, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    __tablename__ = 'person'

    name = db.Column(String(250), nullable=False, unique=True)
    id = db.Column(Integer, primary_key=True)
    favorite_color = db.Column(String(250))
    cats_or_dog = db.Column(String(250))


    def __init__(self, name, favorite_color, cats_or_dog):
       self.name = name
       self.favorite_color = favorite_color
       self.cats_or_dog = cats_or_dog
      







