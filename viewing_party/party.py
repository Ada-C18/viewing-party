# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {"title": title,"genre":genre,"rating":rating}
        return movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    user_data = {"watched":[]}
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {"watchlist":[]}
    user_data["watchlist"].append(movie)
    return user_data
    

def watch_movie(user_data,title):
    watched_movie = None
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            watched_movie = movie
            break
    if watched_movie:
        user_data["watchlist"].remove(watched_movie)
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

