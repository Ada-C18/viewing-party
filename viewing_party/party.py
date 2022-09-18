# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {"title": title, "genre": genre, "rating": rating}
        return movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    '''
    Takes two arguments, user_data and movie, where user_data 
    is a dictionary that stores all of the movies the user has watched 
    and movie is a dictionary which contains the information for a movie
    
    Adds the value of movie to the "watched" list inside of user_data

    Returns user_data
    '''
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    adds movie to the watchlist list inside of user_data,
    where movie is a dictionary and user_data is a dictionary with a list of dictionaries 
    '''
    user_data["watchlist"].append(movie)
    print(user_data)
    return user_data

def watch_movie(user_data, title):
    '''
    moves title from a user's watchlist to their watched list
    '''
    # watchlist_list = user_data["watchlist"]
    # print(watchlist_list)
    for index in range(len(user_data["watchlist"])):
        if user_data["watchlist"][index]["title"] == title:
            user_data["watched"].append(user_data["watchlist"].pop(index))
            
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

