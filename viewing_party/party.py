# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    return {
        "title": title,
        "genre": genre,
        "rating": rating,
    }

def add_to_watched(user_data, movie):
    updated_data = user_data.copy()
    updated_data["watched"].append(movie)
    return updated_data

def add_to_watchlist(user_data, movie):
    updated_data = user_data.copy()
    updated_data["watchlist"].append(movie)
    return updated_data

def watch_movie(user_data, movie):
    updated_data = user_data.copy()
    watchlist = updated_data["watchlist"]
    watched = updated_data["watched"]
    watchlist_titles = {
        watch_item["title"]: watch_item 
        for watch_item in watchlist
    }
    if movie in watchlist_titles:
        movie_details = watchlist_titles[movie]
        watchlist.remove(movie_details)
        watched.append(movie_details)
    return updated_data
        

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

