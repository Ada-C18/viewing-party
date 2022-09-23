# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    new_movie = {}
    if len(title) > 0:
        new_movie["title"] = title
        if len(genre) > 0:
            new_movie["genre"] = genre
            if rating:
                new_movie["rating"] = rating
                return new_movie
            else:
                return None
    else:
        return None

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

