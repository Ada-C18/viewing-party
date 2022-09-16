# ------------- WAVE 1 --------------------

from operator import length_hint


def create_movie(title, genre, rating):
    movie = {}
    # check if the parameters are truthy
    if title and genre and rating :
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie
    else :
        return None


def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data  


def add_to_watchlist(user_data, movie) :
    user_data["watchlist"].append(movie)     
    return user_data


def watch_movie(user_data, title):

    for movie in user_data["watchlist"]:
        if movie["title"] == title :
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            
    return user_data
        






# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0
    average = 0
    length = len(user_data["watched"])
    for i in range(length):
        sum += user_data["watched"][i]["rating"]
        average = sum / length

    return average    



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


