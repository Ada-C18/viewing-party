# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {"title": title,
        "genre": genre,
        "rating": rating
        }
        return movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    watched_list = []
    watched_list.append(movie)
    user_data["watched"] = watched_list
    return user_data

def add_to_watchlist(user_data, movie):
    to_watch_list = []
    to_watch_list.append(movie)
    user_data["watchlist"] = to_watch_list
    return user_data

def watch_movie(user_data, title):
    index = 0
    for i in user_data["watchlist"]:
        if title == user_data["watchlist"][index]["title"]:
            movie = user_data["watchlist"][index]
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
        else:
            index += 1
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

