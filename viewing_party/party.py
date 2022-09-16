# ------------- WAVE 1 --------------------

from curses import use_default_colors
from operator import ne
import re


def create_movie(title, genre, rating):
    dic = {}
    dic["title"] = title
    dic["genre"] = genre
    dic["rating"] = rating
    if dic["title"] == None or dic["genre"] == None or dic["rating"] == None:
        return None
    return dic

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(janes_data, MOVIE_TITLE_1):

    if len(janes_data["watched"]) == 0:
        temp_list = janes_data["watchlist"].pop()
        janes_data["watched"].append(temp_list)
        return janes_data
    elif len(janes_data["watchlist"]) > 1:
        temp_list = janes_data["watchlist"][0]
        janes_data["watched"].append(temp_list)
        del janes_data["watchlist"][0]
        return janes_data
    else:
        return janes_data



        

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

