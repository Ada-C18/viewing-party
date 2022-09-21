# ------------- WAVE 1 --------------------
from ast import In


def create_movie(title, genre, rating):
    #pass
    if title and genre and rating:
        new_movie = {"title": title , "genre": genre, "rating": rating}
        return new_movie
    else: 
        return None 

def add_to_watched(user_data, movie):

    user_data.get("watched").append(movie)
    return user_data

def add_to_watchlist(user_data, movie):

    user_data.get("watchlist").append(movie)
    return user_data

def watch_movie(user_data, title):

    for movie in user_data.get("watchlist"):

        if movie["title"] == title:
            user_data.get("watchlist").remove(movie)
            user_data.get("watched").append(movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):

    if len(user_data.get("watched")) == 0:
        return 0.0

    rating_avergae = 0

    for movie in user_data.get("watched"):
        rating_avergae +=  movie["rating"]

    return rating_avergae / len(user_data.get("watched"))

def get_most_watched_genre(user_data):

    if len(user_data.get("watched")) == 0:
        return None

    popular_genre = {}
    for movie in user_data.get("watched"):
        genre = movie["genre"] 

        if genre not in popular_genre:
            popular_genre[genre] = 1
        else: 
            popular_genre[genre] += 1

    most_count = 0
    most_popular_genre = ""

    for g, value in popular_genre.items():

        if value > most_count:
            most_count = value 
            most_popular_genre = g
            
    return most_popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
# Added heleper function to make code dry
def get_friends_movie(user_data):

    friend_movies = []

    for friend in user_data.get("friends"):
        for f_movie in friend.get("watched"):

            if f_movie not in friend_movies:
                friend_movies.append(f_movie)
    return friend_movies

def get_unique_watched(user_data):

    friend_movies = get_friends_movie(user_data)

    unique_watched = []
    # trying list comprehension
    unique_watched = [movie
        for movie in user_data.get("watched")
            if movie not in friend_movies]

    return unique_watched

def get_friends_unique_watched(user_data):
    friend_movies = get_friends_movie(user_data)

    unique_watched = []

    for f_movie in friend_movies:

        if f_movie not in user_data.get("watched"):
            unique_watched.append(f_movie)

    return unique_watched
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):

    recs_movie = []

    friends_movie = get_friends_unique_watched(user_data)

    for movie in friends_movie:

        if movie.get("host") in user_data.get("subscriptions"):
            recs_movie.append(movie)

    return recs_movie

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):

    rec_movie = []

    fav_genre = get_most_watched_genre(user_data)
    friends_movie = get_friends_unique_watched(user_data)

    for movie in friends_movie:
        if movie["genre"] == fav_genre:
            rec_movie.append(movie)
    
    return rec_movie


def get_rec_from_favorites(user_data):

    rec_movie = []

    unique = get_unique_watched(user_data)

    for fav in user_data.get("favorites"):
        if fav in unique:
            rec_movie.append(fav)

    return rec_movie