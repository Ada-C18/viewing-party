# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    my_dict = {}

    if not bool(title) or not bool(genre) or not bool(rating):
        return None
    else:
        my_dict["title"] = title
        my_dict["genre"] = genre
        my_dict["rating"] = rating
        
    return my_dict

def add_to_watched(user_data, movie):
    # user_data = {"watched": [
    # { "title": "Title A", "genre": "Horror", "rating": 3.5},
    # { "title": "Title B", "genre": "Horror", "rating": 3.5}, 
    # { "title": "Title C", "genre": "Horror", "rating": 3.5}
    # ]}
    watched_movies_list = user_data.get('watched')
    watched_movies_list.append(movie)
    user_data["watched"] = watched_movies_list
    
    return user_data
    
def add_to_watchlist(user_data, movie):
    # user_data = {"watchlist": [
    # { "title": "Title A", "genre": "Horror", "rating": 3.5},
    # { "title": "Title B", "genre": "Horror", "rating": 3.5}, 
    # { "title": "Title C", "genre": "Horror", "rating": 3.5}
    # ]}
    watchlist_movies_list = user_data.get('watchlist')
    watchlist_movies_list.append(movie)
    user_data["watchlist"] = watchlist_movies_list
    return user_data
    
def watch_movie(user_data, title):
    # user_data = {
        # "watchlist":[], 
        # "watched": []
        # }
    # find movie using the title from watchlist
    watchlist_movies = user_data.get('watchlist')
    # movie = {}
    for movie in watchlist_movies:
        if movie["title"] == title:
            watchlist_movies.remove(movie)
            updated_user_data = add_to_watched(user_data, movie)
            return updated_user_data
    return user_data
    # if it exists, remove it from the watchist
    
    # if it doesnt exist, do nothing
    # add it to watched
        # find movie using the title from watched
        # if it exists, do nothing
        # if it does not exist, add it watched

    


#  --------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched_list = user_data.get("watched")
    if not bool(watched_list):
        return 0.0
    rating_sum = 0.0
    for movie in watched_list:
        rating_sum += movie["rating"]
        
    average_rating = rating_sum/len(watched_list)
    return average_rating


def get_most_watched_genre(user_data):
    watched_list = user_data.get("watched")
    if not bool(watched_list):
        return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

