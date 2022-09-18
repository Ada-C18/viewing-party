# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    if not title or not genre or not rating:
        new_movie = None

    return new_movie

def add_to_watched(user_data, movie):
    
    updated_user_data = user_data.copy()
    updated_user_data["watched"].append(movie)

    return updated_user_data

def add_to_watchlist(user_data, movie):

    updated_user_data = user_data.copy()
    updated_user_data["watchlist"].append(movie)

    return updated_user_data

def watch_movie(user_data, title):
    
    title_list = []

    for dicts in user_data["watchlist"]:
        title_list.append(dicts["title"])

    for dicts in user_data["watched"]:
        title_list.append(dicts["title"])
        
    if title in title_list:
        updated_user_data = user_data.copy()
        updated_user_data["watched"].append(updated_user_data["watchlist"].copy())
        updated_user_data["watchlist"].pop()
        
        return updated_user_data
    
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

