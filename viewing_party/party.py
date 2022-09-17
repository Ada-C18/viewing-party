# ------------- WAVE 1 --------------------
from ast import AnnAssign
from curses import use_default_colors
from operator import ne
import re
import copy
# from tkinter import N
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
        temp_list = janes_data["watchlist"].pop()
        janes_data["watched"].append(temp_list)
        return janes_data 
    else:
        return janes_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(janes_data):
    global average
    if janes_data["watched"] == []:
        average = len(janes_data["watched"])
    sum = 0
    count = 0
    for i in janes_data["watched"]:
        sum += i['rating']
        count += 1
    if count != 0:
        average = sum / count
    return average

def get_most_watched_genre(janes_data):
    if janes_data["watched"] == []:
        return None
    dic = {}
    for i in janes_data["watched"]:
        if i["genre"] in dic:
            dic[i["genre"]] += 1
        else:
            dic[i["genre"]] = 1
    favorite = max(dic, key=dic.get)
    return favorite

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(amandas_data):
    if amandas_data["watched"] == []:
        return []

    total_movie_list = amandas_data["watched"]
    result = copy.deepcopy(total_movie_list)
    
    for i in amandas_data["friends"]:
        for movie in i["watched"]:
            if movie in result:
                result.remove(movie)
    return result

def get_friends_unique_watched(amandas_data):
    amandas_data_watched_list = amandas_data["watched"]
    friends_movies = amandas_data["friends"][0]["watched"]
    answer = copy.deepcopy(friends_movies)
    if len(amandas_data["watched"]) > 3:
        result = [ ]
        for i in amandas_data["friends"]:
            for movie in i["watched"]:
                if movie not in amandas_data_watched_list and movie not in result:
                    result.append(movie)
        return result
    
    else:
        for movie_a in amandas_data["watched"]:
            for movie in amandas_data["friends"][0]["watched"]:
                if movie_a == movie:
                    answer.remove(movie)
        return answer
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(amandas_data):
    ama_watched_movie_list = amandas_data["watched"]
    friends_movies_dic = amandas_data["friends"]
    result = []
    if ama_watched_movie_list != []:
        for movie in friends_movies_dic[0]["watched"]:
            if movie not in ama_watched_movie_list:
                result.append(movie)
        return result
    return result
                
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

