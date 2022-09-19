from re import M
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

def add_to_watched(user_data, movie):
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

def get_unique_watched(user_data):
    unique_watched = []
    unique_watched.extend(user_data["watched"])
    for list in user_data["friends"]:
        for movie in list["watched"]:
            if movie in unique_watched:
                unique_watched.remove(movie)
    return unique_watched


def get_friends_unique_watched(user_data):
    friends_watched = []
    for list in user_data["friends"]:
        for movie in list["watched"]:
            if movie not in friends_watched and movie not in user_data["watched"]:
                friends_watched.append(movie)
    return friends_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    friend_unique = get_friends_unique_watched(user_data)
    for movie in friend_unique:
        if movie not in recommended_movies and movie["host"] in user_data["subscriptions"]:
                recommended_movies.append(movie)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommended_movies = []
    friends_watched = get_friends_unique_watched(user_data)
    fav_genre = get_most_watched_genre(user_data)

    for movie in friends_watched:
        if movie not in recommended_movies and movie["genre"] is fav_genre:
            recommended_movies.append(movie)
    return recommended_movies


def get_rec_from_favorites(user_data):
    recommended_movies = []
    user_uniques = get_unique_watched(user_data)
    for movie in user_data["favorites"]:
            if movie in user_uniques and movie not in recommended_movies:
                recommended_movies.append(movie)
    return recommended_movies