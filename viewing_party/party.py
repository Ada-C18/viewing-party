# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {"title": title, "genre": genre, "rating": rating}
        return movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    '''
    Takes two arguments, user_data and movie, where user_data 
    is a dictionary that stores all of the movies the user has watched 
    and movie is a dictionary which contains the information for a movie
    
    Adds the value of movie to the "watched" list inside of user_data

    Returns user_data
    '''
    user_data["watched"].append(movie)
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

