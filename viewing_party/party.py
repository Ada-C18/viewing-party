# ------------- WAVE 1 --------------------
# -----------------------------------------

from viewing_party.party import *
from dataclasses import dataclass
#from symbol import subscript
from xml.dom import UserDataHandler


def create_movie(title, genre, rating):
    movie_dictionary = {}
    if title and genre and rating:
        movie_dictionary["title"] = title
        movie_dictionary["genre"] = genre
        movie_dictionary["rating"] = rating
        return movie_dictionary

    else:
        return None

def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data
#"watched": [{"title": "{movie} "genre": "Horror", "rating": 3.5},
          #  {"title": "Title A", "genre": "Horror", "rating": 3.5},
           # {"title": "Title A", "genre": "Horror", "rating": 3.5}]

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            del user_data["watchlist"][i]
            user_data["watched"].append(title)
            return user_data

        else:
            return user_data



# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    average = 0.0
    sum = 0.0
    if len(user_data["watched"]) != 0:
        for num in user_data["watched"]:
            sum += num["rating"] 
        average = sum /len(user_data["watched"])
        return average
    else: 
        average = 0.0
        return average

def get_most_watched_genre(user_data):
    genremostwatched = {}
    if len(user_data["watched"]) < 1:
        return None
    else:
        for movie in user_data["watched"]:
            if movie["genre"] in genremostwatched.keys():
                genremostwatched[movie["genre"]] += 1
            else:
                genremostwatched[movie["genre"]] = 1
    max_genre = max(genremostwatched)
    return max_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
    
def get_unique_watched(user_data):
    friends_movies = []
    unique_movies_watched = []
    user_movie = user_data["watched"]

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_movies:
                friends_movies.append(movie)

    for movie in user_movie:
        if movie not in friends_movies:
            unique_movies_watched.append(movie)
    return unique_movies_watched

def get_friends_unique_watched(user_data):
    unique_movies_watched = []
    friends_movies = []
    user_movie_list = user_data["watched"]

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_movies:
                friends_movies.append(movie)

    for movie in friends_movies:
        if movie not in user_movie_list:
            unique_movies_watched.append(movie)
    return unique_movies_watched

   
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies= []
    friends_movies = get_friends_unique_watched(user_data)
    
    for movie in friends_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommended= []
    friends_movies = get_friends_unique_watched(user_data)
    user_most_watched= get_most_watched_genre(user_data)

    for movie in friends_movies:
        if movie["genre"] == user_most_watched:
            recommended.append(movie)    
    return recommended

def get_rec_from_favorites(user_data):
    recommended= []
    user_favorites = user_data["favorites"]
    user_unique = get_unique_watched(user_data)
    for movie in user_favorites:
        if movie in user_unique:
            recommended.append(movie)
    return recommended