# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
    # return None for incorrect inputs
    if title == None or genre == None or rating == None:
        return None
    # create a dictionary with the given input
    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    # return the dictionary
    return new_movie

# add movie dict to watched list
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

# add movie dict to watchlist
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# move movie dict from watchlist to watched list
def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
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

