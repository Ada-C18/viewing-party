# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict ["rating"] = rating
    
    movie_info = [title,genre,rating]
    if None in movie_info:
        return None
    else:
        return movie_dict

def add_to_watched(user_data,movie):
    user_data = {}
    user_data["watched"] = [movie]

    return user_data

def add_to_watchlist(user_data,movie):
    user_data = {}
    user_data["watchlist"] = [movie]

    return user_data

def watch_movie(user_data,title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
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

