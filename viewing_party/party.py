# ------------- WAVE 1 --------------------
from hashlib import new
# from turtle import title
from tests.test_constants import MOVIE_TITLE_1, clean_wave_3_data
from collections import Counter


def create_movie(title, genre, rating):

    if title == None or genre == None or rating == None:
        return None
    else:
        movie = {
                        "title": title,
                        "genre": genre,
                        "rating": rating,
                        }
        return movie
    

def add_to_watched(user_data, movie):
   
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):

    to_watch_list = user_data["watchlist"]
    already_watched = user_data["watched"]

    for i in range(len(to_watch_list)):
        if to_watch_list[i]["title"] == title:
            already_watched.append(to_watch_list[i])
            to_watch_list.remove(to_watch_list[i])
    return user_data
    
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
   
    already_watched = user_data["watched"]
    ratings = 0
    for i in range(len(already_watched)):
        ratings += already_watched[i]["rating"]
        avr_rating = (ratings/(len(already_watched)))
    if already_watched == []:
        avr_rating = 0
        
    return avr_rating

def get_most_watched_genre(user_data):

     already_watched = user_data["watched"]
     all_genres = []

     for i in range(len(already_watched)):
        all_genres.append(already_watched[i]["genre"])
        top_genre = [word for word, word_count in Counter(all_genres).most_common(1)]
        top_genre = top_genre[0]
        return top_genre
     if already_watched == []:
        top_genre = None
     return top_genre
     
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    
    friends_not_watched = []
    friends_watched = []
    user_watched = user_data["watched"]

    for movie in user_watched:
        friends_not_watched.append(movie)

    for friend_list in user_data["friends"]:
        for friend in friend_list["watched"]:
            friends_watched.append(friend)
    for i in friends_watched:
        if i in friends_not_watched:
            friends_not_watched.remove(i)
    return friends_not_watched

def get_friends_unique_watched(user_data):
   
    only_friends_watched = []
    already_watched = []
    user_watched = user_data["watched"]

    for friend_list in user_data["friends"]:
        for friend in friend_list["watched"]:
            if friend not in only_friends_watched:
                only_friends_watched.append(friend)
   
    for movie in user_watched:
        already_watched.append(movie)
    
    for i in already_watched:
        if i in only_friends_watched:
            only_friends_watched.remove(i)
    
    return only_friends_watched
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    
    recommendations = []
    user_subscriptions = user_data["subscriptions"]
    friends_watch_list = get_friends_unique_watched(user_data)
    
    for m in range(len(friends_watch_list)):
        if friends_watch_list[m]["host"] in user_subscriptions:
            recommendations.append(friends_watch_list[m])

    return recommendations
# -----------------------------------------
# ------------- WAVE 5 --------------------
# ----------------------------------------
def get_new_rec_by_genre(user_data):
    
    recommendations_genre = []
    favorite_genre = get_most_watched_genre(user_data)
    friends_watch_list = get_friends_unique_watched(user_data)

    for m in range(len(friends_watch_list)):
        if friends_watch_list[m]["genre"] ==  favorite_genre:
            recommendations_genre.append(friends_watch_list[m])
    return recommendations_genre

def get_rec_from_favorites(user_data):

    recommendations_favs = []
    favorite_movies = user_data["favorites"]
    user_watch_list = get_unique_watched(user_data)

    for movie in user_watch_list:
        if movie in favorite_movies:
            recommendations_favs.append(movie)
    return recommendations_favs
