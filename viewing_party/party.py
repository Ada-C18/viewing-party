# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # make a dictionary with these keys: "title":title, "genre": genre, "rating": rating
    movie_dict = {}

    if title and genre and rating:
        movie_dict['title'] = title
        movie_dict['genre'] = genre
        movie_dict['rating'] = rating

        return movie_dict
    
    return None
def add_to_watched(user_data, movie):
    # user data is a dictionary with a key watched that has the value of an empty list which will be later a list of dictionaries with the movies the user has watched
    # the value of movie is a dictionary like the one from the first function
    # add the value of movie to the list in watched
    # return user_data
    user_data['watched'].append(movie)
    return user_data
def add_to_watchlist(user_data, movie):
    # add movie to list in 'watchlist' key in user_data dictionary
    user_data['watchlist'].append(movie)
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

