# ------------- WAVE 1 --------------------

from distutils.file_util import move_file
from pickle import FALSE


def create_movie(title, genre, rating):
    new_movie = {}
    if title == None or genre == None or rating == None:
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

        if user_data["watchlist"] == None:
            return user_data
        else: 
            movie_to_move = None
            # dict_movie name of each dictionary in "watchlist"
            for dict_movie in user_data["watchlist"]:
                # if the tittle in that dictionary evaluate to the same then do the following 
                if title == dict_movie["title"]:
                    # create a new varaible it becomes none when user_data["watchlist"] is removed
                    movie_to_move = dict_movie
                    # need to add this to a diffrent dictionary 
            # error here because condition needs to be true
            if movie_to_move:
                user_data["watched"].append(movie_to_move)
                user_data["watchlist"].remove(movie_to_move)
            return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    all_ratings_added = 0
    if user_data["watched"] == []:
        return 0
    for movie in user_data["watched"]:
        rating = 0 
        rating = movie["rating"]
        all_ratings_added += rating

    average_rating = all_ratings_added/len(user_data["watched"])
    return average_rating

def get_most_watched_genre(user_data):
    genres_map = {}
    for movie in user_data["watched"]:
        if movie["genre"] not in genres_map:
            genres_map[movie["genre"]] = 1
        else:
            genres_map[movie["genre"]] += 1
    
    maximum_key = None
    maximum_value = 0 
    for genre, quanity in genres_map.items():
        if quanity > maximum_value:
            maximum_value = quanity
            maximum_key = genre
        return maximum_key
        

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    # # compare movies of friends with user
    # # create a list of dictionaries of the movies that have not been seen by the friends
    # # return the list of dictionaries that friends have not watched 

    friends_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.append(movie["title"])

    movie_list = []
    for movie in user_data["watched"]:
        if movie["title"] not in friends_movies:
            movie_list.append(movie)

    return movie_list

"""
Create a function named get_friends_unique_watched. This function should...
take one parameter: user_data
the value of user_data will be a dictionary with a "watched" list of movie dictionaries, and a "friends"
This represents that the user has a list of watched movies and a list of friends
The value of "friends" is a list
Each item in "friends" is a dictionary. This dictionary has a key "watched", which has a list of movie dictionaries.
Each movie dictionary has a "title".
Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies at least one of the user's friends have watched, but the user has not watched.
Return a list of dictionaries, that represents a list of movies
"""
def get_friends_unique_watched(user_data):
    # user 
    movie_list = []
    for movie in user_data["watched"]:
        movie_list.append(movie["title"])

    friends_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in movie_list:
                if movie not in friends_movies:
                    friends_movies.append(movie)
    return friends_movies
            
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------





