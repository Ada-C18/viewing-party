# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}
    if title and genre and rating: 
        movie["title"] = title
        movie["genre"] = genre 
        movie["rating"] = rating 
        return movie


def add_to_watched(user_data, movie):
    user_data = {}
    user_data["watched"] = [movie]
    return user_data


def add_to_watchlist(user_data, movie):
    user_data = {}
    user_data["watchlist"] = [movie]
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:    
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data['watched'].append(movie)
            # return user_data
        
    return user_data  
# # -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched_movies = user_data["watched"]
    rating_list = []
    for i in range(len(watched_movies)):
        rating_list.append(watched_movies[i]["rating"])
    if len(rating_list) != 0:
        average = sum(rating_list)/len(rating_list)
    else:
        average = 0.0
    return average 
        
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

