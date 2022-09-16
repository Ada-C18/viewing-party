# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    if title == None or genre == None or rating == None:
        return None
    else:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    avg_rating = 0
    for i in range(len(user_data["watched"])):
        avg_rating += user_data["watched"][i]["rating"]
    if len(user_data["watched"]) == 0:
        return avg_rating
    avg_rating /= len(user_data["watched"])
    return avg_rating

def get_most_watched_genre(user_data):
    fav_genre = ""
    genre_dict = {}
    i = 0
    if len(user_data["watched"]) == 0:
        return None
    for key, value in user_data["watched"][i].items():
        if key == "genre":
            if value in genre_dict:
                genre_dict[value] += 1
            else:
                genre_dict[value] = 1
        i += 1
    for key, value in genre_dict.items():
        if value > 0:
            fav_genre = key
    return fav_genre





# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

