# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    movie = {}

    if title == None or genre == None or rating == None:
        return None
    else:
        movie['title'] = title
        movie['genre'] = genre
        movie['rating'] = rating
        
    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)   

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

#def watch_movie()

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

