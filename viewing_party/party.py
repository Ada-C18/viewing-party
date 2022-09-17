# ------------- WAVE 1 --------------------
# 1. Create a function named  `create_movie`. This function and all subsequent functions should be in `party.py`. 

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {}
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    return None

# 2. Create a function named `add_to_watched`. This function should...
# test: test_adds_movie_to_user_watched
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

# 3. Create a function named add_to_watchlist.def 
# test: test_adds_movie_to_user_watchlist()
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
# Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify user_data.



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

