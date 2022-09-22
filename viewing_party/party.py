# ------------- WAVE 1 --------------------

from enum import unique
from os import fpathconf
from typing import Concatenate, Counter
from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(movie_title, genre, rating):
    viewing_dict = {
        "title": movie_title,
        "genre": genre,
        "rating": rating
    }
    if movie_title is None or genre is None or rating is None:
        return None

    return viewing_dict

def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

#user_data = {'watched': [], 'watchlist': [{'genre': 'Horror', 'rating': 3.5, 'title': 'It Came from the Stack Trace'}]}, title = 'It Came from the Stack Trace'
def watch_movie(user_data, title):
    for movie in user_data["watchlist"]: #read the titles in my watchlist_dict
        if movie["title"] == title: #if watchlist_dict contains the entered title
            #watched_title = movie #creates a new variable for the watched title
            user_data["watchlist"].remove(movie) #delete the watched title in watchlist
            user_data["watched"].append(movie) #append the watched title in watchlist

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    average = []
    for movie in user_data["watched"]:
        average.append(movie["rating"])
    if len(user_data["watched"]) == 0:
        calc_average = 0.0
    else:
        calc_average = sum(average) / len(average)
    return calc_average

def get_most_watched_genre(user_data):
    genre_count = []
    if len(user_data["watched"]) == 0:
        return None
    else:
        for movie in user_data["watched"]:
            genre_count.append(movie["genre"])

            #counts.append(genre) # appending as characters and not string
        pop_genre = max(set(genre_count), key = genre_count.count)
    
        return pop_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    uniqued_watched = []
    all_friends_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            all_friends_movies.append(movie)
    for movie in user_data["watched"]:
        if movie not in all_friends_movies:
            uniqued_watched.append(movie)
    return uniqued_watched
            # for movie in friend
        # if movie not in user_data["friends"]:
def get_friends_unique_watched(user_data):
    unique_watched = []
    user_movies = []
    new_unique_list = []
    for movie in user_data["watched"]:
        user_movies.append(movie)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_movies: 
                unique_watched.append(movie)
    for i in range(len(unique_watched)):
        if unique_watched[i] not in unique_watched[i + 1:]:
            new_unique_list.append(unique_watched[i])

    return new_unique_list

    
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommendations_list = []
    unique_watched = []
    user_movies = []
    new_unique_list = []
    sub = user_data["subscriptions"]
    for movie in user_data["watched"]:
        user_movies.append(movie)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_movies: 
                unique_watched.append(movie)
    for i in range(len(unique_watched)):
        if unique_watched[i] not in unique_watched[i + 1:]:
            new_unique_list.append(unique_watched[i])
    for movie in new_unique_list:
        if movie["host"] in sub:
            recommendations_list.append(movie)

    return recommendations_list
    


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    new_recommendation_for_genre = []
    fave_genre = get_most_watched_genre(user_data)
    unique_movies = get_friends_unique_watched(user_data)
    for movie in unique_movies:
        if movie["genre"] == fave_genre:
            new_recommendation_for_genre.append(movie)
    return new_recommendation_for_genre

def get_rec_from_favorites(user_data):
    unique_movies = get_unique_watched(user_data)
    recommended_by_user = []
    for movie in unique_movies:
        if movie in user_data["favorites"]:
            recommended_by_user.append(movie)
    return recommended_by_user