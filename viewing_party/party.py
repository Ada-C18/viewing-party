# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    #pass
    if title and genre and rating:
        new_movie = {"title": title , "genre": genre, "rating": rating}
        return new_movie
    else: 
        return None 

def add_to_watched(user_data, movie):

    user_data.get("watched").append(movie)
    return user_data

def add_to_watchlist(user_data, movie):

    user_data.get("watchlist").append(movie)
    return user_data

def watch_movie(user_data, title):

    for movie in user_data.get("watchlist"):
        if movie["title"] == title:
            user_data.get("watchlist").remove(movie)
            user_data.get("watched").append(movie)
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

