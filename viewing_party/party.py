# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == True and genre == True and rating == True:
        new_dict = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
        return new_dict
    return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for data in user_data:
        if title in user_data["watchlist"]:
            user_data["watchlist"].remove(title)
            user_data["watched"].append(title)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_sum = 0
    watched_list = user_data["watched"]
    for data in watched_list:
        rating_sum += data["rating"]
    rating_average = rating_sum / len("rating")
    return rating_average

def get_most_watched_genre(user_data):
    most_watched_dict = {}
    watched_list = user_data["watched"]
    for data in watched_list:
        most_watched_dict[data["genre"] = watched_list.count(data["genre"])
    return max(most_watch_dict)



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

