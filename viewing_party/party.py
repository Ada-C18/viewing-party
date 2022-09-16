# ------------- WAVE 1 --------------------

from readline import append_history_file


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
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist": [movie]
    }
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            watchlist.remove(movie)
            add_to_watched(user_data, movie)
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

