# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {
        "title" : title,
        "genre" : genre,
        "rating" : rating,
    }
    if all(movie.values()) == False:
        return None
    else:
        return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie):
    for movie_dict in user_data["watchlist"]:
        if movie_dict["title"] == movie:
            user_data["watched"].append(user_data["watchlist"].pop())
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

