# ------------- WAVE 1 --------------------

# from imp import new_module
# from turtle import title


from os import remove


def create_movie(title, genre, rating):
    new_movie = {"title": title,
            "genre": genre,
            "rating": rating}
    
    if new_movie["genre"] == None:
        return None
    if new_movie["rating"] == None:
        return None
    if new_movie["title"] == None:
        return None
    return new_movie

def add_to_watched(user_data, movie):
    user_data = {}
    user_data["watched"] = [movie]
    return user_data

def add_to_watchlist(user_data, movie):
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
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating = []
    sum = 0

    for i in user_data["watched"]:
        rating.append(i["rating"])
        sum += i["rating"]
    return sum/len(rating)

def get_watched_avg_rating(user_data):
    rating = []
    sum = 0

    for i in user_data["watched"]:
        if i["rating"] == None:
            return 0.0
        else:
            rating.append(i["rating"])
    return sum 





# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------