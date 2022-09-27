# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    new_movie = {}
    if title != None:
        new_movie["title"] = title
        if genre != None:
            new_movie["genre"] = genre
            if rating != None:
                new_movie["rating"] = rating
                return new_movie
            else:
                return None
        else:
            return None
    else:
        return None
            

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if title == user_data["watchlist"][i]["title"]: 
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].pop(i)
            
            return user_data
        # else:
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