# ------------- WAVE 1 --------------------
from multiprocessing.sharedctypes import Value
import re
from turtle import update


def create_movie(title, genre, rating):
    movie ={}
    if title and genre and rating:
        movie.update({"title" :title ,"genre":genre, "rating":rating})
        return movie
    else:
        return None

def add_to_watched(user_data, movie):

    user_data ={}
    user_data["watched"] = [movie]
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {}
    user_data["watchlist"] = [movie]
    return user_data

def watch_movie(user_data, title):
    for item in user_data["watchlist"]:
        if item["title"] == title:
            user_data["watchlist"].remove(item)
            user_data["watched"].append(item)
    return user_data
        
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    avg_rating = 0
    sum_of_rating = 0
    for item in user_data["watched"]:
        for movie in item:
            if movie == "rating":
                sum_of_rating  += item[movie]
                avg_rating = sum_of_rating /len(user_data["watched"])
    return avg_rating
    #

def get_most_watched_genre(user_data):
    genre_list =[]
    temp = 0
    for item in user_data["watched"]:
        for movie in item:
            if movie == "genre":
                genre_list.append(item[movie])
    for i in range(len(genre_list)):
        temp = genre_list.count(genre_list[i])
        most_watched_genre = genre_list[i]
        return most_watched_genre
    else:
        return None
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_list =[]
    friends_movie_list=[]
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_movie_list:
                friends_movie_list.append(movie)
    for movie in user_data["watched"]:
        if movie not in friends_movie_list:
            unique_list.append(movie)
    return unique_list
    # for user_movie in user_data["watched"]:
    #     for friends_movie in user_data["friends"]:
    #         if user_movie not in friends_movie["watched"]:
    #             unique_list.append(user_movie)
    # return unique_list

    


def get_friends_unique_watched(user_data):
    unique_friends_list =[]
    user_movie_list=[]
    for movie in user_data["watched"]:
        if movie not in user_movie_list:
            user_movie_list.append(movie)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_movie_list and movie not in unique_friends_list:
                unique_friends_list.append(movie)
    return unique_friends_list
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movie_list=[]
    subscriptions_list=[]
    unique_watched = get_friends_unique_watched(user_data)
    
    for user in user_data["subscriptions"]:
            subscriptions_list.append(user)
    for movie in unique_watched:
        if movie["host"]in subscriptions_list:
            recommended_movie_list.append(movie)
    return recommended_movie_list
        
    

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommended_list = []
    most_watched_genre = get_most_watched_genre(user_data)
    unique_watched = get_friends_unique_watched(user_data)
    
    for watch in user_data["watched"]:
        if watch is None:
            return recommended_list
    for movie in unique_watched:
        if movie["genre"] == most_watched_genre:
            recommended_list.append(movie)
    return recommended_list
    
def get_rec_from_favorites(user_data):
    recommended_movie_list = []
    user_unique_movie = get_unique_watched(user_data)
    for u_movie in user_unique_movie:
        if u_movie in user_data["favorites"]:
            recommended_movie_list.append(u_movie)
    return recommended_movie_list