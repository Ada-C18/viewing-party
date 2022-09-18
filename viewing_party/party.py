# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    # if title == True and genre == True and rating == True:
    if True: 
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
    else:
        return None 
    if title == None or genre == None or rating == None:
        return None
    return movie_dict

def add_to_watched(user_data, movie):
    # user_data is a dictionary with a key "watched" and value of list of dictionaries users have watched
        # An empty list value in user_data["watched"] means user has no movies in watched list
    # movie is a dictionary with title, genre, and rating keys
    user_data["watched"] = [movie]
    return user_data

def add_to_watchlist(user_data, movie):
    # user_data is a dictionary with key "watchlist" with value of list of dictionaries
    # movie is a dicitonary
    user_data["watchlist"] = [movie]
    return user_data

def watch_movie(user_data, title):
    # user_data is a dictionary with "watchlist" and "watched" keys
    # title is a string and reps the title of a movie the user has watched
    if user_data["watchlist"][0]["title"] == title:
        user_data["watched"] = [user_data["watchlist"][0]]
        user_data["watchlist"] = []
    # for i in user_data["watchlist"]: # looking at every item in list
    #     for key in i:
    #         if key["title"] == title:
    #             user_data["watched"].append(key)
    #             user_data["watchlist"].pop(key)
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

