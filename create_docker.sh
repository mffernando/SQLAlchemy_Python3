#!/bin/bash

#create PostgreSQL instance
docker run --name sqlalchemy-orm-psql \
	-e POSTGRES_PASSWORD=password \
	-e POSTGRES_USER=root \
	-e POSTGRES_DB=sqlalchemy \
	-p 5432:5432 \
	-d postgres

#--name = Name of Docker instance
#-e POSTGRES_PASSWORD = PostgreSQL password
#-e POSTGRES_USER = PostgreSQL user
#-e POSTGRES_DB = PostgreSQL database name
#-p 5432:5432 = PostgreSQL port (default)
#-d postgres = Docker instance based on the official PostgreSQL repository