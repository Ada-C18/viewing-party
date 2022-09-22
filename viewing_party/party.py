# ------------- WAVE 1 --------------------

import math


def create_movie(title, genre, rating):
    movie = {}
    if title and genre and rating:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie    
    else:
        return None    

def add_to_watched(user_data, movie):
    if not "watched" in user_data:
        user_data["watched"] = []
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    if not "watchlist" in user_data:
        user_data["watchlist"] = []
    user_data["watchlist"].append(movie)
    return user_data
    
def watch_movie(user_data, title):
    for ele in user_data["watchlist"]:
        if title == ele["title"]:
            user_data["watched"].append(ele)
            user_data["watchlist"].remove(ele)
            return user_data
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum_rating = 0.0
    length = len(user_data["watched"])
    if "watched" in user_data and length > 0:
        for ele in user_data["watched"]:
            sum_rating += ele["rating"]
        avg_rating = sum_rating/length
    else:
        avg_rating = 0.0
    return avg_rating


def get_most_watched_genre(user_data):
    counter = {}
    res = None
    if "watched" in user_data:
        for ele in user_data["watched"]:
            if not ele["genre"] in counter:
                counter[ele["genre"]] = 1
            else:
                counter[ele["genre"]] += 1
        max_count = 0
        for k, v in counter.items():
            if v > max_count:
                res = k
                max_count = v
    return res



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    res = []
    friends_movie_set = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movie_set.add(movie["title"])
    for movie in user_data["watched"]:
        if not movie["title"] in friends_movie_set:
            res.append(movie)
    return res

def get_friends_unique_watched(user_data):
    res = []
    watched_moive_set = set()
    for movie in user_data["watched"]:
        watched_moive_set.add(movie["title"])
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if not movie["title"] in watched_moive_set and not movie in res:
                res.append(movie)
    return res


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movie = []
    movie = get_friends_unique_watched(user_data)
    for ele in movie:
        if ele["host"] in user_data["subscriptions"]:
            recommended_movie.append(ele)
    return recommended_movie



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    recommended_movie2 = []
    movie = get_friends_unique_watched(user_data)
    most_freq_movie = get_most_watched_genre(user_data)
    for ele in movie:
        if ele["genre"] == most_freq_movie:
            recommended_movie2.append(ele)
    return recommended_movie2

def get_rec_from_favorites(user_data):
    recommended_movie3 = []
    fav_movie = user_data["favorites"]
    friends_movie_set = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movie_set.add(movie["title"])
    for ele in fav_movie:
        if not ele["title"] in friends_movie_set:
            recommended_movie3.append(ele)
    return recommended_movie3