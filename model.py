from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String, DateTime
import datetime
from sqlalchemy.orm import sessionmaker, relationship, backref, scoped_session

engine = create_engine("sqlite:///ratings.db", echo=False)
session = scoped_session(sessionmaker(bind=engine,
                                        autocommit = False,
                                        autoflush = False))

Base = declarative_base()

### Class declarations go here
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True)
    age = Column(Integer, nullable = True)
    gender = Column(String(1), nullable = True)
    occupation = Column(String(20), nullable = True)
    email = Column(String(64), nullable = True)
    password = Column(String(64), nullable = True)
    age = Column(Integer, nullable = True)
    zipcode = Column(String(15), nullable = True)

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key = True)
    title = Column(String(80), nullable = False)
    date = Column(DateTime, nullable = False)
    imdb = Column(String(140), nullable = False)

class Rating(Base):
    __tablename__ = "ratings"

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable = False)
    movie_id = Column(Integer, ForeignKey('movies.id'), nullable = False)
    rating = Column(Integer, nullable = False)

    user = relationship("User",
                        backref=backref("ratings", order_by=id))
    movie = relationship("Movie",
                        backref=backref("movies", order_by=movie_id))
### End class declarations

def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
