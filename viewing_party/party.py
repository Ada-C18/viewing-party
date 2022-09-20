# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):    
    if title and genre and (type(rating) == int or type(rating) == float):
        new_movie ={}  
        new_movie['title'] = title
        new_movie['genre'] = genre
        new_movie['rating'] = rating
        return new_movie
    return None

def add_to_watched(user_data, movie):
    # add movie to the "watched" list inside "user_data"
    # "watched" is a dictionary key but it's also the index
    # of the list "user_data"
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    # "watchlist" is a dictionary key but is also an index in "user_data"
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    
    # if title is in a movie in watchlist
    if user_data["watchlist"]["movie"]["title"] == title:
    # remove the movie from watchlist using .pop()
        user_data["watchlist"]["movie"]["title"].pop(title)
        #add movie to "watched"
        user_data["watched"].append(title)
        return user_data
    else:
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

