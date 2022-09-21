# ------------- WAVE 1 --------------------

from distutils.file_util import move_file


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

"""
Create a function named watch_movie. This function should...
take two parameters: user_data, title
the value of user_data will be a dictionary with a "watchlist" and a "watched"
This represents that the user has a watchlist and a list of watched movies
the value of title will be a string
This represents the title of the movie the user has watched
If the title is in a movie in the user's watchlist:
remove that movie from the watchlist
add that movie to watched
return the user_data
If the title is not a movie in the user's watchlist:
return the user_data
Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify user_data.
"""

# watch_movie(janes_data, "Non-Existent Movie Title")

def watch_movie(user_data, title):
    movie_to_move = None
    # dict_movie name of each dictionary in "watchlist"
    for dict_movie in user_data["watchlist"]:
        # if the tittle in that dictionary evaluate to the same then do the following 
        if title == dict_movie["title"]:
            # create a new varaible 
            movie_to_move = dict_movie
        else:
            return user_data
    
# you can't remove a dict from a for loop 
    user_data["watchlist"].remove(movie_to_move)
    user_data["watched"].append(movie_to_move)
    return user_data
    
    


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
# def get_watched_avg_rating(user_data):
#     # user has a list of watched movies: to calculate all movies average
#     # user_data["watched"]["rating"] 
#     rating = 0 
#     # empty watched list == 0.0 
#     for movie_rating in user_data["watched"]:
#         if user_data["watched"]["rating"] == None:
#             user_data["watched"]["rating"] == 0.0 
#         rating += user_data["watched"]["rating"] 
    
#     average_rating = rating/len(user_data["watched"])
#     return average_rating
    
#     # return average_rating 

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------





