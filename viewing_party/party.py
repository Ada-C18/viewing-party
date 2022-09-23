# ------------- WAVE 1 --------------------

from optparse import TitledHelpFormatter
from xmlrpc.client import NOT_WELLFORMED_ERROR


def create_movie(title, genre, rating):
    new_movie = {}

    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    else:
        return None
    
    return new_movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].pop(i)
            
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    average_rating = 0.0
    total_rating = 0.0

    for i in range(len(user_data["watched"])):
        total_rating += user_data["watched"][i]["rating"]
    
    if len(user_data["watched"]) > 0:
        average_rating = total_rating / len(user_data["watched"])
    
    return average_rating

def get_most_watched_genre(user_data):
    watched_genre = {}
    
    if len(user_data["watched"]) == 0:
        return None

    for movie in user_data["watched"]:
        if movie["genre"] in watched_genre:
            watched_genre[movie["genre"]] += 1
        else:
            watched_genre[movie["genre"]] = 1

    k = list(watched_genre.keys())
    v = list(watched_genre.values())
    most_watched_genre = k[v.index(max(v))]

    return most_watched_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique_watched = []

    watched_list = []
    friends_watched_list = []

    for movies in user_data["watched"]:
        watched_list.append(movies)
    for i in range(len(user_data["friends"])):
        for movie in user_data["friends"][i]["watched"]:
            friends_watched_list.append(movie)

    for movie in watched_list:
        if movie not in friends_watched_list:
            unique_watched.append(movie)

    return unique_watched


def get_friends_unique_watched(user_data):
    friends_unique_watched = []

    watched_list = []
    friends_watched_list = []

    for movies in user_data["watched"]:
        watched_list.append(movies)
    for i in range(len(user_data["friends"])):
        for movie in user_data["friends"][i]["watched"]:
            friends_watched_list.append(movie)

    for movie in friends_watched_list:
        if movie not in watched_list and movie not in friends_unique_watched:
            friends_unique_watched.append(movie)

    return friends_unique_watched
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    available_recs = []

    friends_unique_watched = get_friends_unique_watched(user_data)
    
    for movie in friends_unique_watched:
        if movie["host"] in user_data["subscriptions"]:
            available_recs.append(movie)

    return available_recs
            
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    new_rec_by_genre = []

    favorite_genre = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)

    for movie in friends_unique_watched:
        if movie["genre"] == favorite_genre:
            new_rec_by_genre.append(movie)
    
    return new_rec_by_genre


def get_rec_from_favorites(user_data):
    favorites = []

    unique_watched = get_unique_watched(user_data)

    for movie in unique_watched:
        if movie in user_data["favorites"]:
            favorites.append(movie)

    return favorites

