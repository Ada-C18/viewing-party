# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = None
    if title == None or genre == None or rating == None:
        movie == None
    else:
        movie = {
            "title" : title,
            "genre" : genre,
            "rating" : rating
        }
    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
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

