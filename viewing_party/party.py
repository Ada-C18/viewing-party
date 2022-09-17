# ------------- WAVE 1 --------------------

from pickle import FALSE


def create_movie(title, genre, rating):
    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
    information = [title, genre, rating]
    if None in information:
        return None
    else:
        return new_movie
def add_to_watched(user_data, movie):
    user_data ={}
    watched_list = []
    user_data["watched"]: watched_list
    if None in watched_list:
        return None
    elif movie not in watched_list:
        watched_list.append(movie)
        print(len(watched_list))
    return user_data
#  test_adds_movie_to_user_watched()

def add_to_watchlist(user_data,movie):
    user_data ={}
    watched_list = user_data["watched"]
    user_data["watched"]: watched_list
    if user_data["watched"] == None:
        # user_data["watched"] == None
        watched_list.append(None)
    user_data["watchlist"].append(movie)
    return user_data#- take two parameters: `user_data`, `title`
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
# Details = {"Destination": "China", 
#            "Nstionality": "Italian", "Age": []}
# Details["Age"] += [20, "Twenty"]
# print(Details)

def watch_movie(user_data, title):
    user_data ={}
    watched_list = []
    user_data["watched"]: watched_list
    
    user_data["watchlist"]: title
    if title in watched_list:
        user_data["watchlist"].pop(title)
        user_data["watched"] = title
        
        
    if user_data["watched"] == None:
        watched_list.append("None")
    return user_data        
   # Arrange
 
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

