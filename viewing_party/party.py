# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    if title and genre and rating:
        movie_dict.update({"title": title})
        movie_dict.update({"genre": genre})
        movie_dict.update({"rating": rating})
        return movie_dict
    else:
        return None   

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

    # for data in user_data:
    #         data.append(movie)
    # print(user_data)
    # return user_data

def add_to_watchlist(user_data, movie):
    for watchlist in user_data:
        watchlist.append(movie)

def watch_movie(user_data, title):
    if title in user_data["watchlist"]:
        user_data["watchlist"].remove(title)
        user_data["watched"].append(title)
    else:
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

