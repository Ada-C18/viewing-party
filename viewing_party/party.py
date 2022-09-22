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


"""
Create a function named get_most_watched_genre. This function should...
take one parameter: user_data
the value of user_data will be a dictionary with a "watched" list of movie dictionaries. 
Each movie dictionary has a key "genre".
This represents that the user has a list of watched movies. Each watched movie has a genre.
The values of "genre" is a string.
Determine which genre is most frequently occurring in the watched list
return the genre that is the most frequently watched
If the value of "watched" is an empty list, get_most_watched_genre should return None.
"""
def get_most_watched_genre(user_data):
    genres_map = {}
    for movie in user_data["watched"]:
        if movie["genre"] not in genres_map:
            genres_map[movie["genre"]] = 1
        else:
            genres_map[movie["genre"]] += 1
    
    # iterate over the genre_map 
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

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------





