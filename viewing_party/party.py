import copy
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        new_movie = None
        return new_movie
    
    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
    return new_movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(janes_data, title):
    copied_data = copy.deepcopy(janes_data["watchlist"])
    for movie in copied_data:
        if movie["title"] == title:
            janes_data["watched"].append(movie)
            janes_data["watchlist"].remove(movie)
    return janes_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(janes_data):
    average_rating = 0
    if janes_data["watched"]:
        for movie in janes_data["watched"]:
            average_rating += movie["rating"]
    else:
        return average_rating
    return average_rating / len(janes_data["watched"])


def get_most_watched_genre(janes_data):
    genre_frequency = {}
    if not janes_data["watched"]:
        return None
    for movie in janes_data["watched"]:
        if movie["genre"] not in genre_frequency:
            genre_frequency[movie["genre"]] = 1
        else:
            genre_frequency[movie["genre"]] += 1
    max_value = max(genre_frequency.values())
    print(f"{genre_frequency=}")
    for genre, value in genre_frequency.items():
        if value == max_value:
            return genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

