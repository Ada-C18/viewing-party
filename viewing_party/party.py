# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    '''Add new movie if title, genre and rating are truthy'''
    new_movie = {}

    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    else:
        return None

    return new_movie


def add_to_watched(user_data, movie):
    '''Add movie to watched movies list in user data dict'''
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    '''Add movies to watchlist in user data dict'''
    user_data["watchlist"].append(movie)
    return user_data

# 4. Create a function named `watch_movie`. This function should...

# - take two parameters: `user_data`, `title`
#   - the value of `user_data` will be a dictionary with a `"watchlist"` and a `"watched"`
#     - This represents that the user has a watchlist and a list of watched movies
#   - the value of `title` will be a string
#     - This represents the title of the movie the user has watched
# - If the title is in a movie in the user's watchlist:
#   - remove that movie from the watchlist
#   - add that movie to watched
#   - return the `user_data`
# - If the title is not a movie in the user's watchlist:
#   - return the `user_data`

def watch_movie(user_data, title):    
    user_data["watched"] += user_data["watchlist"]

    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]['title'] == title:
            user_data["watchlist"].remove(user_data["watchlist"][i])

    return user_data

# Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify `user_data`.

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

