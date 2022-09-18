# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {
    "title" : title,
    "genre" : genre,
    "rating" : rating
    }
    for key in new_movie:
        if not new_movie[key]:
            return None
        
    return new_movie


def add_to_watched(user_data, movie):
    # this function returns a list of dicts of movies the user watched 
    user_data["watched"] = [movie]
    return user_data


def add_to_watchlist(user_data, movie):
    # This function returns a list of dicts of movies the user wants to watch
    user_data["watchlist"] = [movie]
    return user_data


def watch_movie(user_data, title):
    # This functions checks if the title in movie is the same as the title in user_data watchlist list, 
    # and if yes, it removes it and adds it to the user_data watched list
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
    return user_data    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    avg_rating = 0.0
    if not user_data["watched"]:
        return avg_rating
    for movie in user_data["watched"]:
        avg_rating += movie["rating"]
    return avg_rating / len(user_data["watched"])

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

