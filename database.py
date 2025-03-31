from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:sashaank@localhost/TodoApplicationDatabase'

engine = create_engine(SQLALCHEMY_DATABASE_URL) # To prevent accidental sharing of same connection for different requests

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()




