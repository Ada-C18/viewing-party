# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {}
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    else:
        return None

#user data is a dictionary with a key "watched" and value is list of dictionaries 
#movie is a dictionary with title, genre,rating as keys (like create movie)
#add movie to user_data & return user_data 
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

#user_data is same as above exept key is "watchlist"
#movie follows create_movie format
#add movie to user_data & return user_data 
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

#if title is in watchlist, move to watched
#else return user_data 

def watch_movie(user_data, title):

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            
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

