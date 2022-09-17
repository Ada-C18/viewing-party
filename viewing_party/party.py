# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    dict_movie={
        "title": title,
        "genre": genre,
        "rating": rating
    }
    for key in dict_movie:
        if not dict_movie[key]:
            return None
    return dict_movie
def add_to_watched(the_user_data, movie_watched):
    the_user_data["watched"].append(movie_watched)
    return the_user_data

def add_to_watchlist(the_user_d, movie_to_watch):
    the_user_d["watchlist"].append(movie_to_watch)
    return the_user_d
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

