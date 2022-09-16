# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    info = [title, genre, rating]
    for movie_info in info:
        if movie_info == None:
            return None
        
    new_movie = {"title": title , "genre": genre , "rating": rating}
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"] = [movie]
    return user_data 

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]
    return user_data 

def watch_movie(user_data, movie):
    for movies in user_data["watchlist"]:
        for label,info in movies.items():
            if label == "title":
                if movie == info:
                    watched_movie = user_data["watchlist"].pop(user_data["watchlist"].index(movies))
                    user_data["watched"].append(watched_movie)
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

