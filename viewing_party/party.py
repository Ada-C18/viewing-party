# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
    
    if None in new_movie.values():
        return None
    else:
        return new_movie

def add_to_watched(user_data, movie):
     user_data["watched"].append(movie)
     return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    # loop through dict of watch list
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    average = 0
    num_movies_watched = len(user_data["watched"])
    for movie in user_data["watched"]:
        average += movie["rating"] / num_movies_watched
    return average

def get_most_watched_genre(user_data):
    store_and_count_watched_genre = {}
    for movie in user_data["watched"]:
        if movie["genre"] in store_and_count_watched_genre:
            store_and_count_watched_genre[movie["genre"]] += 1
        else:
            store_and_count_watched_genre[movie["genre"]] = 1
    popular_genre = max(store_and_count_watched_genre, default=None, key = store_and_count_watched_genre.get)
    return popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------

def get_unique_watched(user_data):
    friends_watched_list = []
    user_unique_movies = []

    friends = user_data["friends"] # variable for accessing list of dictionaries storing movies that friends have watched
    user_watched = user_data["watched"] # variable of a dictionary with its value as a list of movies user has watched

    for friend in friends:
        for movie in friend["watched"]:
            friends_watched_list.append(movie["title"])
    
    for movie in user_watched:
        if movie["title"] not in friends_watched_list:
            user_unique_movies.append(movie) # if a movie title in user watched list is not in friend's list, append entire dictionary to unique list
        
    return user_unique_movies

def get_friends_unique_watched(user_data):

    friends_watched_list = []
    unique_friends_movie = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched_list:
                friends_watched_list.append(movie)
    
    for movie in friends_watched_list:
        if movie not in user_data["watched"]:
            unique_friends_movie.append(movie)

    return unique_friends_movie
# -----------------------------------------

# ------------- WAVE 4 --------------------
#  return a recommended list of movies as dictionaries

def get_available_recs(user_data):
    user_not_watched__friend_has_list = []
    # friends_watched_list = []
    rec_list = []

    friends = user_data["friends"]
    user_watched = user_data["watched"]

    for friend in friends:
        for movie in friend["watched"]:
            if movie not in user_watched:
                user_not_watched__friend_has_list.append(movie)
    
    for movie in user_not_watched__friend_has_list:
        if movie["host"] in user_data["subscriptions"]:
            rec_list.append(movie)

    return rec_list


    
    

# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

