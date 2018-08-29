# coding=utf-8
#Inserts Class

#instances to persist to the database
from datetime import date
from actor import Actor
from base import Session, engine, Base
from contact_details import ContactDetails
from movie import Movie
from stuntman import Stuntman

#generate database schema
Base.metadata.create_all(engine)

#create new session

session = Session()

#create movies
movie_1 = Movie("Movie 1 Name", date(2018, 8, 28))
movie_2 = Movie("Movie 2 Name", date(2006, 8, 22))
movie_3 = Movie("Movie 3 Name", date(2008, 1, 12))
movie_4 = Movie("Movie 4 Name", date(2014, 8, 8))
movie_5 = Movie("Movie 5 Name", date(2010, 12, 1))

#create actors
actor_1 = Actor("Actor 1 Name", date(1950, 8, 28))
actor_2 = Actor("Actor 2 Name", date(1960, 8, 22))
actor_3 = Actor("Actor 3 Name", date(1970, 1, 12))
actor_4 = Actor("Actor 4 Name", date(1980, 8, 8))
actor_5 = Actor("Actor 5 Name", date(1990, 12, 1))

#add actors to movies
movie_1.actors = [actor_1]
movie_2.actors = [actor_2]
movie_3.actors = [actor_3]
movie_4.actors = [actor_4]
movie_5.actors = [actor_5, actor_1]

#add contact details to actors
actor_1_contact = ContactDetails("12 1234 1234", "Address 1", actor_1)
actor_2_contact = ContactDetails("12 1234 1234", "Address 2", actor_2)
actor_3_contact = ContactDetails("12 1234 1234", "Address 3", actor_3)
actor_4_contact = ContactDetails("12 1234 1234", "Address 4", actor_4)
actor_5_contact = ContactDetails("12 1234 1234", "Address 5", actor_5)

#create stuntmen
actor_1_stuntman = Stuntman("Stuntman 1", True, actor_1)
actor_2_stuntman = Stuntman("Stuntman 2", True, actor_2)
actor_3_stuntman = Stuntman("Stuntman 3", True, actor_3)
actor_4_stuntman = Stuntman("Stuntman 4", True, actor_4)
actor_5_stuntman = Stuntman("Stuntman 5", True, actor_5)

#persist data
#SQLAlchemy uses the save-update cascade strategy
#movie
session.add(movie_1)
session.add(movie_2)
session.add(movie_3)
session.add(movie_4)
session.add(movie_5)
#contact
session.add(actor_1_contact)
session.add(actor_2_contact)
session.add(actor_3_contact)
session.add(actor_4_contact)
session.add(actor_5_contact)
#stuntman
session.add(actor_1_stuntman)
session.add(actor_2_stuntman)
session.add(actor_3_stuntman)
session.add(actor_4_stuntman)
session.add(actor_5_stuntman)

#commit and close session
session.commit()
session.close()