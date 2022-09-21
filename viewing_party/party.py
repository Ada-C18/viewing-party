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
                # max_count = v
    return res



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

