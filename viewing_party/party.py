# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movies = {}
    if None in [title, genre, rating]: 
        return None
    movies["title"] = title
    movies["genre"] = genre
    movies["rating"] = rating
    return movies

def add_to_watched(user_data, movie):
    # user_data["watched"] = [list of dictionaries that holds movies the user has watched]
    # movie will be a dictionary 
    # add movie to this list 
    list_of_movies_watched = user_data["watched"]
    list_of_movies_watched.append(movie)
    user_data["watched"] = list_of_movies_watched
    return user_data

def add_to_watchlist(user_data, movie):
    list_of_movies_to_watch = user_data["watchlist"] 
    list_of_movies_to_watch.append(movie)
    user_data["watchlist"] = list_of_movies_to_watch
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"] #[{}]
    watched = user_data["watched"] #[{}]
    for i in range(0, len(watchlist)):
        if title == watchlist[i]["title"]:
            watched.append(watchlist[i])
            watchlist.remove(watchlist[i])
    user_data["watchlist"] = watchlist
    user_data["watched"] = watched
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

