# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating
    if movie_dict["title"] == None:
        return None
    if movie_dict["genre"] == None:
        return None
    if movie_dict["rating"]== None:
        return None
    return movie_dict

def add_to_watched(user_data, movie):

    user_data = {
        "watched": [movie] 
    }

    movie = {
        "title": "Title A",
        "genre": "Horror",
        "rating": 3.5
    }

    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist": [movie] 
    }

    movie = {
        "title": "Title A",
        "genre": "Horror",
        "rating": 3.5
    }

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

