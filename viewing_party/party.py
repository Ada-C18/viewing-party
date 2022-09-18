# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {
        "title" : title,
        "genre" : genre,
        "rating": rating
    }

    if new_movie["title"] and new_movie["genre"] and new_movie["rating"]:
         return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data = {
        "watched" : [movie]
    }
    return user_data
    
def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist" : [movie]
    }
    return user_data

def watch_movie(user_data, title):
    pass
    watchlist = user_data["watchlist"]
    for movie in watchlist:
    # if the title is in a movie in the user's watchlist:
        if title  == movie["title"]:
            # print(f"debug: title in movie dict")
            watchlist.remove(movie)
        else:
            # print(f"debug: title no in movie dict")
            return user_data
        user_data["watched"].append(movie)
        # return the user_data
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
