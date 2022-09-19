# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    pass
    #make a dictionary with these keys: "title","genre","rating"
    movie_dict = {}
    movie_dict["title"]= title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating
    
    information = [title,genre,rating]
    if None in information:
        return None
    else:
        return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"] = [movie]
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]
    return user_data 

def watch_movie(user_data,title):
    watched_movie = title
    for movie in user_data["watchlist"]:
        for value in movie.values():
            if value == watched_movie:
                user_data["watchlist"].remove(movie)
                user_data["watched"].append(movie)

    return(user_data)

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

