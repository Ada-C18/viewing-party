# ------------- WAVE 1 --------------------

from functools import total_ordering
from operator import length_hint
import re

# creating the movie dictionary
def create_movie(title, genre, rating):
    movie = {}
    # check if the parameters are truthy
    if title and genre and rating :
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie
    else :
        return None


# adding wathced movies to the user's watched list
def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data  


# adding movies to the users's watchlist
def add_to_watchlist(user_data, movie) :
    user_data["watchlist"].append(movie)     
    return user_data


# moving the moive from watchlist to watched
def watch_movie(user_data, title):

    for movie in user_data["watchlist"]:
        if movie["title"] == title :
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            
    return user_data

        
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum = 0
    average = 0
    length = len(user_data["watched"])

    for movie in user_data["watched"]:
        sum += movie["rating"]
        average = sum / length

    return average   


def get_most_watched_genre(user_data):
    genre_dict = {}
    length = len(user_data["watched"])
    
    if length > 0 :
        for i in range(length):
            genre = user_data["watched"][i]["genre"]
            if genre in genre_dict.keys():
                genre_dict[genre] +=1
            else :
                genre_dict[genre] = 1

        
        genre_list = []
        for k, v in genre_dict.items():
            genre_list.append((v, k))   
        genre_list.sort(reverse = True)
        return genre_list[0][1]
    else :
        return None
         

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_unique_watched = []
    friends_watched_list =[]
    user_list = user_data["watched"]
    friends= user_data["friends"]
    
    for friend in friends:
        friend_watched = friend["watched"]
        friends_watched_list += friend_watched

    for movie in user_list:
        if movie not in friends_watched_list:
            user_unique_watched.append(movie)   

    return user_unique_watched


def get_friends_unique_watched(user_data):
    friends_unique_watched = []
    friends_watch_list = []
    user_list = user_data["watched"]
    friends=user_data["friends"]

    for friend in friends:
        friend_watched = friend["watched"]
        friends_watch_list +=friend_watched

    for movie in friends_watch_list:
        if movie not in user_list and movie not in friends_unique_watched:
            friends_unique_watched.append(movie)

    return friends_unique_watched           

    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    friends_unique_movies = get_friends_unique_watched(user_data)

    for movie in friends_unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)

    return recommended_movies        


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommended_movies = []
    genre = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)

    for movie in friends_unique_watched :
        if movie["genre"] == genre :
            recommended_movies.append(movie)

    return recommended_movies        

def get_rec_from_favorites(user_data):
    recommended_movies = []
    friends_all_movies = []
    friends = user_data["friends"]

    for friend in friends:
        friend_movies = friend["watched"]
        friends_all_movies +=friend_movies

    for movie in user_data["favorites"] :
        if movie not in friends_all_movies:
            recommended_movies.append(movie)

    return recommended_movies        

