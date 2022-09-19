# ------------- WAVE 1 --------------------

from enum import unique
import copy
# from types import NoneType


def create_movie(title, genre, rating):

    new_movie = {}
    
    if not title or not genre or not rating:
        return None
    else:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    return new_movie

def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):

    for movie in user_data["watchlist"]:
        if movie["title"] is title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    
    if not user_data["watched"]:
        return 0.0

    ratings = []
    
    for rate in user_data["watched"]:
        ratings.append(rate["rating"])

    return sum(ratings)/len(ratings)

def get_most_watched_genre(user_data):

    freq = {}
    
    if not user_data["watched"]:
        return None

    for style in user_data["watched"]:
        if style["genre"] in freq:
            freq[style["genre"]] += 1
        else:
            freq[style["genre"]] = 1
    return max(freq, key = freq.get)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    
    unique = copy.copy(user_data["watched"])

    for film in user_data["friends"]:
        for name in film["watched"]:
            if name in unique:
                unique.remove(name)
    return unique
    
def get_friends_unique_watched(user_data):

    friend_unique = []

    for film in user_data["friends"]:
        for name in film["watched"]:
            if name not in user_data["watched"] and name not in friend_unique:
                friend_unique.append(name)
    return friend_unique

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    
    rec = []

    friend_unique = get_friends_unique_watched(user_data)

    for movies in friend_unique:
        if movies["host"] in user_data["subscriptions"]:
            rec.append(movies)
    return rec

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    rec_by_genre = []

    freq = get_most_watched_genre(user_data)

    friend_unique = get_friends_unique_watched(user_data)

    for movies in friend_unique:
        if freq == movies["genre"]:
            rec_by_genre.append(movies)
    return rec_by_genre

def get_rec_from_favorites(user_data):

    fav_rec = []
    
    user_only = get_unique_watched(user_data)

    for user in user_data["favorites"]:
        if user in user_only:
            fav_rec.append(user)
    return fav_rec




