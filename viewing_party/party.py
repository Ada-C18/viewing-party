# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # check to see if parameters are true
    # conditional for each paramter 
    # add parameters to a dictionary if true
    # create a dictionary
    # append to dictionary if true, NONE if false
    # return dictionary

    movie = {}
    if title == None or genre == None or rating == None:
        return None
    else:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie

def add_to_watched(user_data, movie):
    watched =[]
    watched.append(movie)
    user_data["watched"] = watched

    return user_data

def add_to_watchlist(user_data, movie):
    watchlist = []
    watchlist.append(movie)
    user_data["watchlist"] = watchlist

    return user_data

def watch_movie(user_data, title):
# need to see if the title is in the usersdata
# if movie in WATCHLIST then remove the movie from watchlist and add to watched, return
# if movie not in watchlist, return
    # for i in user_data['watchlist'][i]:
    for i in range(len(user_data['watchlist'])):
        if user_data['watchlist'][i]['title'] == title:
            user_data['watched'].append(user_data['watchlist'][i])
            user_data['watchlist'].remove(user_data['watchlist'][i])
            # user_data['watched'].append(user_data['watchlist'][i])
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

