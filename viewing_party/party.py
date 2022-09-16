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
    list_of_movies = user_data["watched"]
    list_of_movies.append(movie)
    user_data["watched"] = list_of_movies
    return user_data

# def add_to_watchlist(user_data, movie):


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

