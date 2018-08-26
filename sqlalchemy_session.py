#import create_engine function from sqlalchemy
from sqlalechemy import create_engine
#import sessionmaker function from sqlalchemy.orm
from sqlalchemy.orm import sessionmaker

#create a  PostgreSQL engine
#on port '5432' (default one)
#defines that it will use, 'usr' and 'pass'
#credentials interact with the 'sqlalchemy' database
engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')

#create a configured 'Session' class
Session = sessionmaker(bind=engine)

#create a session
session = Session()
