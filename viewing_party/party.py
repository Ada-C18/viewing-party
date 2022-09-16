# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    dict = {}
    if title and genre and rating:
        dict['title'] = title
        dict['genre'] = genre
        dict['rating'] = rating
        return dict
    else:
        return None

def add_to_watched(user_data, movie):
    #user_data = {'watched': []}
    #movie = {'title': "Title A", "genre": "Horror", "rating": 3.5}
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    #user_data = {'watchlist': []}
    #movie = {"title": "Title A", "genre": "Horror", "rating": 3.5}
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    #user_data = {"watchlist": [], "watched": []}
    #title = ""
    watchlist = user_data['watchlist']
    for watchlist_movie in watchlist:
        if title == watchlist_movie['title']:
            movie = watchlist_movie
            result = add_to_watched(user_data, movie)
            print('Result:', result)
            user_data['watchlist'].remove(watchlist_movie)
            
            return result
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

