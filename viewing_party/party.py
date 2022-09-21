# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating
    if movie_dict["title"] == None:
        return None
    if movie_dict["genre"] == None:
        return None
    if movie_dict["rating"]== None:
        return None
    return movie_dict

def add_to_watched(user_data, movie):

    user_data = {
        "watched": [movie] 
    }

    movie = {
        "title": "Title A",
        "genre": "Horror",
        "rating": 3.5
    }

    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist": [movie] 
    }

    movie = {
        "title": "Title A",
        "genre": "Horror",
        "rating": 3.5
    }

    return user_data

def watch_movie(user_data, title):

    

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            movie_index = user_data["watchlist"].index(movie) 
            user_data["watchlist"].pop(movie_index) 
            user_data["watched"].append(movie["title"])
    
    return user_data 

    #pseudocode 
    # for movie in user_data["watchlist"]:
    # if movie["title"] == title:
    #     remove title from movie inside "watchlist" ---
    #     add it to movies in "watched" 







    # ******solution works only for test 7******** 

    # if title in user_data["watchlist"][0]["title"]:
    #     user_data["watched"].append(user_data["watchlist"][0])
    #     user_data["watchlist"]=[]
    # elif title != user_data["watchlist"][0]["title"]: 
    #     return user_data

    #*******solution works only for test 7*********



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

