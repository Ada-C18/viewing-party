# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating

        return new_movie

def add_to_watched(user_data, movie):
    '''
    user data is a dictionary containing a key "watched" with value []
    "watched" will be a list of dictionaries the user has watched
    '''
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    user data is dictionary containing value "watchlist with value []
    '''
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, MOVIE_TITLE_1):
    '''
    moves movie from user data dictionary w/ watchlist list using movie title -->
    watched list key in same dictionary (an empty list) 
    '''
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == MOVIE_TITLE_1:
            user_data["watched"].append(user_data["watchlist"].pop(i))

        
    return user_data
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

