import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Genre(Base):
    __tablename__ = 'genre'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_id = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'user_id': self.user_id,
        }



class Artist(Base):
    __tablename__ = 'artist'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    instrument = Column(String(250))
    labels = Column(String(250))
    associated_acts = Column(String(250))
    genre_id = Column(Integer, ForeignKey('genre.id'))
    user_id = Column(String(250), nullable=False)
    genre = relationship(Genre)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
            'description': self.description,
            'instrument': self.instrument,
            'labels': self.labels,
            'associated_acts': self.associated_acts,
            'user_id': self.user_id,
        }


engine = create_engine('sqlite:///music_catalog.db')


Base.metadata.create_all(engine)