# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {"title":title, 
                    "genre": genre, 
                    "rating": rating
                    }
        return movie_dict
    else:
        return None
    
def add_to_watched(user_data, movie):    
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if title in user_data["watchlist"][i]["title"]:
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].remove(user_data["watchlist"][i])
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) > 0:
        sum_watched_rating = 0.0
        for i in range(len(user_data["watched"])):
            sum_watched_rating += user_data["watched"][i]["rating"]
        watched_avg_rating = sum_watched_rating / len(user_data["watched"])
    else:
        watched_avg_rating = 0.0
    return watched_avg_rating


def get_most_watched_genre(user_data):
    pass

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    pass

def get_friends_unique_watched(user_data):
    pass

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    pass

# -----------------------------------------
# ------------- WAVE 5 --------------------
# ----------------------------------------- 
def get_new_rec_by_genre(user_data):
    pass

def get_rec_from_favorites(user_data):
    pass