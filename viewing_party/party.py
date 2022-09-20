# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
    
    if None in new_movie.values():
        return None
    else:
        return new_movie

def add_to_watched(user_data, movie):
     user_data["watched"].append(movie)
     return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    # loop through dict of watch list
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    average = 0
    num_movies_watched = len(user_data["watched"])
    for movie in user_data["watched"]:
        average += movie["rating"] / num_movies_watched
    return average

def get_most_watched_genre(user_data):
    store_and_count_watched_genre = {}
    for movie in user_data["watched"]:
        if movie["genre"] in store_and_count_watched_genre:
            store_and_count_watched_genre[movie["genre"]] += 1
        else:
            store_and_count_watched_genre[movie["genre"]] = 1
    popular_genre = max(store_and_count_watched_genre, default=None, key = store_and_count_watched_genre.get)
    return popular_genre

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

