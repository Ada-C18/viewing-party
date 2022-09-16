from statistics import mode

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movies = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movies
    return None

def add_to_watch(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

#user_data = {
# }
def get_watched_avg_rating(user_data):
    ratings = []
    ave_ratings = 0
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
    if len(ratings) > 0:
        ave_ratings = sum(ratings)/len(ratings)
    return ave_ratings

def get_most_watched_genre(user_data):
    genre_list = []
    for movie in user_data["watched"]:
        genre_list.append(movie["genre"])
    
    if len(genre_list) > 0:
        return mode(genre_list)
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