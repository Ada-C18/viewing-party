# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if bool(title) == True and bool(genre) == True and bool(rating) == True:
        return {
            "title": title,
            "genre": genre,
            "rating": rating
            }
    else:
        return None

def add_to_watched(user_data, movie):
    user_data = {
        "watched": [movie]
        }
    return user_data

def add_to_watchlist(user_data, movie):
    pass

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

