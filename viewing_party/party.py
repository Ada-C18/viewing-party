# ------------- WAVE 1 --------------------

from re import M
from turtle import title


def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {"title": title, "genre": genre, "rating": rating}
        return movie_dict
    else:
        return None


def add_to_watched(user_data, movie):
    user_data = {"watched": []}
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data = {"watchlist": []}
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    watched_movie = None
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            watched_movie = movie
            break
    if watched_movie:
        user_data["watchlist"].remove(watched_movie)
        user_data["watched"].append(watched_movie)
    return user_data


# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    movies = user_data["watched"]
    average_rating = 0.0
    sum = 0
    for movie in movies:
        sum += movie["rating"]
        average_rating = sum/len(movies)

    return average_rating


def get_most_watched_genre(user_data):
    movies = user_data["watched"]
    if len(movies) < 1:
        return None
    genre_count = {}
    for movie in movies:
        genre = movie["genre"]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1
    popular_genre = max(genre_count, key=genre_count.get)
    return popular_genre

# ------------- WAVE 3 --------------------


def get_unique_watched(user_data):
    unique_watched = []
    movies = user_data["watched"]
    friends = user_data["friends"]

    friend_watched_list = []
    for friend in friends:
        friend_watched = friend["watched"]
        friend_watched_list += friend_watched

    for movie in movies:
        if movie not in friend_watched_list:
            unique_watched.append(movie)

    return unique_watched


def get_friends_unique_watched(user_data):
    friend_unique_watched = []
    movies = user_data["watched"]
    friends = user_data["friends"]
    friend_watched_list = []

    for friend in friends:
        friend_watched = friend["watched"]
        friend_watched_list += friend_watched

    for friend_watched_movie in friend_watched_list:
        if friend_watched_movie not in movies:
            if friend_watched_movie not in friend_unique_watched:
                friend_unique_watched.append(friend_watched_movie)
    return friend_unique_watched

# ------------- WAVE 4 --------------------


def get_available_recs(user_data):
    recommended_movies = []
    friends_unique_watched = get_friends_unique_watched(user_data)
    for movie in friends_unique_watched:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies

# ------------- WAVE 5 --------------------


def get_new_rec_by_genre(user_data):
    genre_recommended_movies = []
    popular_genre = get_most_watched_genre(user_data)
    friend_unique_watched = get_friends_unique_watched(user_data)

    for movie in friend_unique_watched:
        if movie["genre"] == popular_genre:
            genre_recommended_movies.append(movie)
    return genre_recommended_movies


def get_rec_from_favorites(user_data):
    user_favorite_list = []
    user_watched = get_unique_watched(user_data)
    for movie in user_watched:
        if movie in user_data["favorites"]:
            user_favorite_list.append(movie)
    return user_favorite_list
