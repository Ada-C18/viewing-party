# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {"title":title, 
                    "genre": genre, 
                    "rating": rating
                    }
        return movie_dict
    else:
        return None
    
def add_to_watched(user_data, movie):    
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# create funct "watch_movie"
# take in 2 parameters:
# user_data: dict of dictionaries "watchlist" and "watched"
# title: string as title of movie
def watch_movie(user_data, title):
    
    pass
# if title in watchlist
# remove movie from watchlist
# add to watched
# return user_data

# if title not in watchlist 
# return user_data 

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