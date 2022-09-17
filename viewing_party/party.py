# ------------- WAVE 1 --------------------

from multiprocessing.sharedctypes import Value

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(title, genre, rating):
    
    new_movie = {}
    if title and genre and rating:
        new_movie = {
            "title" : title,
            "genre" : genre,
            "rating" : rating
        }
        return new_movie
    return None

def add_to_watched(user_data, movie):
    user_data = {"watched" : [movie]}
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {"watchlist" :[movie]}
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            return user_data
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    average_rating = 0 
    sum_list = []
    for i in user_data["watched"]:
        if i["rating"]:
            sum_list.append(i["rating"])
        average_rating = sum(sum_list)/len(user_data["watched"])
    return average_rating

    
def get_most_watched_genre(user_data):
    genre_list =[]
    for i in user_data["watched"]:
        if i["genre"]:
            genre_list.append(i["genre"])
            most_popular = max(set(genre_list), key = genre_list.count)
        return most_popular
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

