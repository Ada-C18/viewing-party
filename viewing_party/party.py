# ------------- WAVE 1 --------------------

def create_movie(movie_title, genre, rating):
    new_movie = {
        "title" : movie_title,
        "genre" : genre,
        "rating" : rating,
    }

    return new_movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data    

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(janes_data, movie):
    janes_data["watched"].append(movie)
    janes_data["watchlist"] = []

    return janes_data

def watched_movie(janes_data, movie_to_watch):

    if movie_to_watch in janes_data["watchlist"]:
        janes_data["watched"].append(movie_to_watch)
        janes_data["watchlist"].remove(movie_to_watch)   

    return janes_data


        


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

