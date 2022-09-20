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

# 4. Create a function named watch_movie.
# TODO: move dict from watchlist to watched list -- if movie in user's watchlist
# OUTPUT: user_data (modified user_data if title in watchlist)
# test_moves_movie_from_watchlist_to_watched
def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    for i in range(len(watchlist)):
        movie = watchlist[i]
        if title == movie["title"]:
            # will remove it from same list in location in memory
            watchlist.remove(movie)
            user_data["watched"].append(movie)
            break
    # return outside for loop to ensure we iterate entire list
    return user_data
# TODO: Add assertions here to test that the correct movie was added to "watched"

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
# Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify user_data.
# 1. Calculate the average rating of all movies in the watched list
# The average rating of an empty watched list is 0.0
# return the average rating
def get_watched_avg_rating(user_data):
    sum_rating = 0
    watched_lst = user_data["watched"]
    watched_lst_length = len(watched_lst)

    if watched_lst_length == 0:
        return 0.0

    for movie in watched_lst:
        sum_rating += movie["rating"]
    return sum_rating / watched_lst_length

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

