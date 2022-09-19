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

    user_data = {}
    user_data["watched"] = [movie]
    
    return user_data

def add_to_watchlist(user_data,movie):
    user_data = {}
    user_data["watchlist"] = [movie]

    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    
            return user_data    
    return user_data    
# -----------------------------------------

# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    average_rating = 0
    list_sum = []
    for i in user_data["watched"]:
        if i["rating"] == 0:
            return 0.0
        if i["rating"]:
            list_sum.append(i["rating"])
        average_rating = sum(list_sum) / len(user_data["watched"])
    return average_rating

def get_most_watched_genre(user_data):
    genre_dict = {}
    
    
    
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

