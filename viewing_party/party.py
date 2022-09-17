# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {"title": title, "genre": genre, "rating": rating}
    if title is None or genre is None or rating is None:
        new_movie = None
    return new_movie

def add_to_watched(user_data, movie):
    updated_data = user_data
    updated_data["watched"].append(movie)
    return updated_data 

def add_to_watchlist(user_data, movie):
    updated_data = user_data
    updated_data["watchlist"].append(movie)
    return updated_data 

def watch_movie(user_data, movie):
    # updated_data = user_data
    # I want to go into the dict user_data
    # I want to go into the key user_data["watchlist"] --- the value is a list of movies to watch
    # I want to go through the all the movies in that list, if the movie_title = movie param, remove that movie
    for item in user_data["watchlist"]:
        if item["title"] == movie:
            watched_movie = item
            user_data["watched"].append(watched_movie)
            user_data["watchlist"].remove(watched_movie)
            updated_data = user_data
    return updated_data


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

