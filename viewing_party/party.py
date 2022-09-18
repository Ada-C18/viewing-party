# ------------- WAVE 1 --------------------

# I feel like there's a better way to test if title, genre, & rating are truthy 
# but not sure how

from multiprocessing.sharedctypes import Value


def create_movie(title, genre, rating):
    new_movie = {"title": title, "genre": genre, "rating": rating}
    if title and genre and rating:
        return new_movie
    else:
        return None


def add_to_watched(user_data, movie):
    has_watched = [movie] 
    user_data = {"watched" : has_watched }
    return user_data


def add_to_watchlist(user_data, movie):
    wants_to_watch = [] 
    user_data = {"watchlist" : wants_to_watch }
    wants_to_watch.append(movie)

    return user_data

def watch_movie(user_data, title):
    for movies in user_data["watchlist"]:
        if movies["title"] == title:
            user_data["watchlist"].remove(movies)
            user_data["watched"].append(movies)
    return user_data
        
        
# -----------------------------------------
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------        

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