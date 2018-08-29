# coding=utf-8
#Queries Class

from actor import Actor
from base import Session
from contact_details import ContactDetails
from movie import Movie
from datetime import date

#session
session = Session()

#all movies
movies = session.query(Movie).all()
# print movies details
print('\n################### ALL MOVIES ###################')
for movie in movies:
	print(f'{movie.title} was released on {movie.release_date}')
print('##################################################')

#get movies after 2015-01-01
movies = session.query(Movie).filter(Movie.release_date > date(2015, 1, 1)).all()
#print recent movies
print('\n################# RECENT MOVIES ##################')
for movie in movies:
	print(f'{movie.title} was released after 2015-01-01')
print('##################################################')

#movies that specific actor participated
actor_1_movies = session.query(Movie).join(Actor, Movie.actors).filter(Actor.name == "Actor 1 Name").all()
#print specific movies from that actor
print('\n################# ACTOR 1 MOVIES #################')
for movie in actor_1_movies:
	print(f'Actor 1 starred in {movie.title}')
print('##################################################')

#actors that have Addres 1
address1_actors = session.query(Actor).join(ContactDetails).filter(ContactDetails.address.ilike('%Address 1%')).all()
#print actors that have Address 1
print('\n######### ACTOR THAT LIVES IN ADDRESS 1 ##########')
for actor in address1_actors:
	print(f'{actor.name} lives in Address 1')
print('##################################################')