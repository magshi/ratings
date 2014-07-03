from model import User, Movie, Rating, connect
import csv
from datetime import datetime

def load_users(session):
    user_file = open('seed_data/u.user').read().split('\n')
    for line in user_file:
        split_line = line.split('|')
        if len(split_line) == 5:
            user_id = split_line[0]
            age = split_line[1]
            gender = split_line[2]
            occupation = split_line[3]
            zipcode = split_line[4]

            new_user = User(id=user_id, 
                            age=age, 
                            gender=gender, 
                            occupation=occupation, 
                            zipcode=zipcode)
            session.add(new_user)
    session.commit()

def load_movies(session):
    user_file = open('seed_data/u.item').read().split('\n')
    for line in user_file:
        u_line = line.decode('latin1')
        split_line = u_line.split('|')
        if len(split_line) >= 4:
            movie_id = split_line[0]
            title = split_line[1]
            date_raw = split_line[2]
            if date_raw != '':
                date_format = "%d-%b-%Y"
                date = datetime.strptime(date_raw, date_format)
            imdb = split_line[4]
            new_movie = Movie(id=movie_id,
                              title=title,
                              date=date,
                              imdb=imdb)
            session.add(new_movie)
    session.commit()

def load_ratings(session):
    user_file = open('seed_data/u.data').read().split('\n')
    for line in user_file:
        split_line = line.split('\t')
        if len(split_line) == 4:
            user_id = split_line[0]
            movie_id = split_line[1]
            rating = split_line[2]
            new_rating = Rating(movie_id = movie_id,
                                user_id = user_id,
                                rating = rating)
            session.add(new_rating)
    session.commit()

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    pass

if __name__ == "__main__":
    s = connect()
    main(s)