# coding=utf-8
#Movie Class

from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import relationship
#extend the Base Class (base.py)
from base import Base

#many to many, connect rows of actors and movies
movies_actors_association = Table(
	'movies_actors', Base.metadata,
	Column('movie_id', Integer, ForeignKey('movies.id')),
	Column('actor_id', Integer, ForeignKey('actors.id'))
)

class Movie(Base):	
	__tablename__ = 'movies' #name of table

	id = Column(Integer, primary_key=True) #id Integer type primary key
	title = Column(String) #title String type
	release_date = Column(Date) #release_date Date type
	actors = relationship("Actor", secondary=movies_actors_association) #relationship

	def __init__(self, title, release_date):
		self.title = title
		self.release_date = release_date