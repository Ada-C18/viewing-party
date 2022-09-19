# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    else:
        movie = {}
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
    return movie

def add_to_watched(data, movie):
    data["watched"].append(movie)
    return data

def add_to_watchlist(data, movie):
    data["watchlist"].append(movie)
    return data

def watch_movie(data, movie_title):
    movie = next((item for item in data["watchlist"] if item["title"] == movie_title), None)
    if movie:
        add_to_watched(data, movie)
        data["watchlist"].remove(movie)
    return data
    
    


    

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

