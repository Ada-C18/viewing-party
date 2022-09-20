# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {
        "title": title, "genre": genre, "rating": rating
    }
    movie_info = [title, genre, rating]
    
    if None in movie_info:
        return None
    else:
        return movie_dict
    
    
def add_to_watched(user_data, movie):
    user_data = {
        "watched": [movie]
    }
    return user_data


def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist": [movie]
    }
    return user_data 


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if len(user_data['watched']) == 0:
        return 0.0 
    
    rating = 0
    movie_rating_list = []
    
    for movie in user_data["watched"]:
        movie_rating = movie["rating"]
        rating += movie_rating 
        movie_rating_list.append(movie["rating"])
        average_rating = rating / len(movie_rating_list)
    return average_rating



# def get_most_watched_genre(user_data):
#     user_data = {
#         "watched": [movie]
#     }
    
    




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    friends_watched_list = []
    user_watched_list = []
    unique_list_of_dicts = []
    friends = user_data["friends"]
    user_watched = user_data["watched"]
    
    for friend in friends:
        for movie in friend["watched"]:
            friends_watched_list.append(movie["title"])
            
    # for movie in user_watched:
    #     unique_list_of_dicts.append(movie["title"])
    
    for movie in user_watched:
        if movie["title"] not in friends_watched_list:
            unique_list_of_dicts.append(movie)
    
    return unique_list_of_dicts 




        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

