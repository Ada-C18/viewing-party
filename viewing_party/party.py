# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {
        "title" : title,
        "genre" : genre,
        "rating": rating
    }

    if new_movie["title"] and new_movie["genre"] and new_movie["rating"]:
         return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data = {
        "watched" : [movie]
    }
    return user_data
    
def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist" : [movie]
    }
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

