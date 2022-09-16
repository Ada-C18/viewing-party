# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    '''
    Create a dict containing info about one movie, with "title", "genre", and "rating", as keys, mapped to values passed in as arguments.
    '''
    if not title or not genre or not rating:
        return None

    movie = {}
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating

    return movie

def add_to_watched(user_data, movie):
    '''
    Add a movie to a user's list of watched movies
    '''
    # user_data = {"watched" : []}
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    Add a movie to a user's watchlist
    '''
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    '''
    Move a movie from watchlist to watched
    '''
    
    #I want to find the correct dict entry in watchlist given the value of "title", how do I do that?
    #Iterate over watchlist until watchlist["title"] == movie_title
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            watched_movie = movie
    user_data["watched"].append(watched_movie)
    user_data["watchlist"].remove(watched_movie)
    
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

