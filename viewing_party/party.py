# ------------- WAVE 1 --------------------

from hashlib import new
from re import M
from collections import Counter
from viewing_party.helper_functions import *

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1, USER_DATA_3

def create_movie(title, genre, rating):
    if title and genre and rating:
        new_movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return new_movie
    else:
        return None

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
    new_watchlist = []
    # iterates over watchlist. moves value in arg title from watchlist to 
    # watched if found. generates a new watchlist comprised of unwatched movies 
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
        else:
            new_watchlist.append(movie)
    user_data["watchlist"] = new_watchlist
    return user_data

# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    total_of_all_ratings = 0
    movies_watched = len(user_data["watched"])
    average = 0.0
    if movies_watched > 0:
        for movie in user_data["watched"]:
            total_of_all_ratings += movie["rating"]
        average = total_of_all_ratings / movies_watched
    return average

# imported Counter() from collections to use in this function
def get_most_watched_genre(user_data):
    dict_of_genres = Counter()
    popular_genre = ""
    if len(user_data["watched"]) > 0:
        #iterates over "watched" list and counts all instances of each genre
        for movie in user_data["watched"]:
            if movie["genre"] not in dict_of_genres:
                dict_of_genres[movie["genre"]] = 0
            else:
                dict_of_genres[movie["genre"]] +=1
        popular_genre = dict_of_genres.most_common(1)[0][0]
        return popular_genre
    else:
        return None

# ------------- WAVE 3 --------------------

def get_unique_watched(user_data):
    user_movie_list = build_user_movie_list(user_data)
    friends_movie_list = build_friend_movie_list(user_data)
    unique_movie_list = []    
    for movie in user_movie_list:
        if movie not in friends_movie_list:
            unique_movie_list.append(movie)
    return unique_movie_list 

def get_friends_unique_watched(user_data): 
    user_movie_list = build_user_movie_list(user_data)
    friends_movie_list = build_friend_movie_list(user_data)    
    unique_movie_list = []
    for movie in friends_movie_list:
        if movie not in user_movie_list and movie not in unique_movie_list:
            unique_movie_list.append(movie)
    return unique_movie_list

# ------------- WAVE 4 --------------------

def get_available_recs(user_data):
    user_movie_list = build_user_movie_list(user_data)
    friends_movie_list = build_friend_movie_list(user_data)    
    recommendations_list = []
    for movie in friends_movie_list:
        if movie not in user_movie_list and movie not in recommendations_list:
            if movie["host"] in user_data["subscriptions"]:
                recommendations_list.append(movie)
    return recommendations_list

# ------------- WAVE 5 --------------------

def get_new_rec_by_genre(user_data):
    user_movie_list = build_user_movie_list(user_data)
    friends_movie_list = build_friend_movie_list(user_data)    
    popular_genre = get_most_watched_genre(user_data)
    recs_by_genre = []
    for movie in friends_movie_list:
        if movie not in user_movie_list and movie["genre"] == popular_genre:
            recs_by_genre.append(movie)
    return recs_by_genre

def get_rec_from_favorites(user_data):
    friends_movie_list = build_friend_movie_list(user_data)    
    recs_from_favorites = []
    for movie in user_data["favorites"]:
        if movie not in friends_movie_list:
            recs_from_favorites.append(movie)
    return recs_from_favorites