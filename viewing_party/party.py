# ------------- WAVE 1 --------------------

from enum import unique
from types import NoneType


def create_movie(title, genre, rating):
    # step 1

    new_movie = {}
    

    if bool(title) != True or bool(genre) != True or bool(rating) != True:
        return None
    else:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    return new_movie
# step 2
def add_to_watched(user_data, movie):

    if len(user_data) == 1:
        user_data["watched"].append(movie)

    return user_data
# step 3
def add_to_watchlist(user_data, movie):

    if not user_data["watchlist"]:
        user_data["watchlist"].append(movie)
    return user_data

# step 4

def watch_movie(user_data, title):

    
    for movie in user_data["watchlist"]:
        if movie["title"] is title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            print(user_data)
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
    

    unique = [users for users in user_data["watched"]]
    
    for film in user_data["friends"]:
        for name in film["watched"]:
            if name in unique:
                unique.remove(name)
    return unique
    
def get_friends_unique_watched(user_data):

    friend_unique = []
    
    for film in user_data["friends"]:
        for movie in film["watched"]:
            if movie not in friend_unique:
                friend_unique.append(movie)
    
    for users in user_data["watched"]:
        if users in friend_unique:
            friend_unique.remove(users)
    return friend_unique

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

