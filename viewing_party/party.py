# ------------- WAVE 1 --------------------

from distutils.file_util import move_file


def create_movie(title, genre, rating):

    movie = {"title" : title,
    "genre" : genre, 
    "rating" : rating}

# if three attributes are truthy, i.e. we have all any truthy values for all attribues
    if title and genre and rating:
        return movie
# otherwise, it's not movie. return none
    else:
        return None 

def add_to_watched(user_data, movie):

# insert movie (in dict) in the watched (in list) in user_data (in dict)
# exception: if no watched list (poor baby), create an empty one.

    if not user_data["watched"]:
        user_data["watched"] = [] 

    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):

# insert movie (in dict) in the watchlist (in list) in user_data (in dict)
# exception: if no watchlist (poor baby), create an empty one.

    if not user_data["watchlist"]:
        user_data["watchlist"] = [] 

    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    
    movies_watchlist = user_data["watchlist"] # in list

    for movie in movies_watchlist:
        if title in movie["title"]:
            # a removed & added list is reflected to user_data dict because dict is mutable
            movies_watchlist.remove(movie) 
            add_to_watched(user_data, movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    pass

def get_most_watched_genre(user_data):
    pass

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    pass

def get_friends_unique_watched(user_data):
    pass
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    pass

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    pass

