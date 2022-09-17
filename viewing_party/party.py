# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    if title == None or genre == None or rating == None:
        return None
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating

    user_data = {
        "watched": [],
        "watchlist": [],
    }

    add_to_watched(user_data, new_movie)
    add_to_watchlist(user_data, new_movie)

    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie):
    for movie_dict in user_data["watchlist"]:
        if movie_dict["title"] == movie:
            user_data["watchlist"].remove(movie_dict)
            user_data["watched"].append(movie_dict)
    return user_data

    # for movie in user_data["watchlist"]:
    #     if movie["title"] == title:
    #         user_data["watchlist"].remove(movie)
    #         user_data["watched"].append(movie)

    #         return user_data
    # return user_data

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

