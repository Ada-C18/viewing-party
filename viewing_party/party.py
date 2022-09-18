# ------------- WAVE 1 --------------------

# user_data is a dict with a str key and a list value consisting of dicts
# HOW to access the values that are in the dicts in the list in the dict???? ahhhhh

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {
            "title" : title,
            "genre" : genre,
            "rating" : rating
        }
        return movie
    else:
        return None

# takes a movie dict and adds it to watched
def add_to_watched(user_data, movie):
    user_data["watched"] = [movie]
    return user_data

# takes a movie dict and adds it to watchlist
def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]
    return user_data

# finds the title of a movie in watchlist, then removes and transfers it to watched

def watch_movie(user_data, title):
    counter = 0
    for movie in user_data["watchlist"]:
        if title in movie["title"]:
            user_data["watched"].append(movie)
            del(user_data["watchlist"][counter])
        # if title in user_data["watchlist"]:
            # how to remove the title from the watchlist
            # movie_seen = user_data["watchlist"].pop(title)
            # movie_seen = user_data.pop("watchlist")
            # user_data["watched"][movie] = [movie_seen]
            return user_data
        counter += 1  
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

