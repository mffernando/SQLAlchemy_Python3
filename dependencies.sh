#!/bin/bash

#pipenv is a global Python package
pip3 install pipenv

#the first dependency referes to SQLAlchemy (sqlalchemy) and the second one (psycopg2)
#is the PostgreSQL driver that SQLAlchemy will use to communicate with the database.

pipenv install sqlalchemy psycopg2