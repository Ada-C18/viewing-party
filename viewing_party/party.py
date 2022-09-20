# ------------- WAVE 1 --------------------

# from collections import Counter
from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    new_movie = {
        "title": MOVIE_TITLE_1,
        "genre": GENRE_1,
        "rating": RATING_1
    }
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    updated_data = user_data
    return updated_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    updated_data = user_data
    return updated_data

def watch_movie(user_data, title):
    watched = {}
    for i in range(len(user_data['watchlist'])):
        if (user_data["watchlist"][i]["title"]) == title:
            watched = user_data["watchlist"].pop(i)
    if watched: 
        user_data["watched"].append(watched)
    updated_data = user_data
    return updated_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum_of_ratings = 0
    if not user_data["watched"]:
        return 0
    else:
        for i in range(len(user_data["watched"])):
            sum_of_ratings += user_data["watched"][i]["rating"]
        average_rating = sum_of_ratings/len(user_data["watched"])
    return average_rating  

def get_most_watched_genre(user_data):
    genre_list = []
    genre_counter = {}
    if not user_data["watched"]:
        return None
    else:
        for i in range(len(user_data["watched"])):
            genre_list.append(user_data["watched"][i]["genre"])
        for genre in genre_list:
            if genre not in genre_counter:
                genre_counter[genre] = 1
            elif genre in genre_counter:
                genre_counter[genre] += 1
        max_value = max(genre_counter.values())
        for key, value in genre_counter.items():
            if max_value == value:
                return key
    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_unique_movies = []
    user_watched_list = []
    friend_watched_list = []

    for movie in user_data["watched"]:
        user_watched_list.append(movie)

    for friend_movie in user_data['friends']:
        for movie in friend_movie['watched']:
            friend_watched_list.append(movie)

    for i in user_watched_list:
        if i not in friend_watched_list:
            user_unique_movies.append(i)
    return user_unique_movies

def get_friends_unique_watched(user_data):
    user_watched_list = []
    friend_watched_list = []
    friend_unique_movies = []
    friend_unique_movies_no_duplicates = []

    for movie in user_data["watched"]:
        user_watched_list.append(movie)

    for friend_movie in user_data['friends']:
        for movie in friend_movie['watched']:
            friend_watched_list.append(movie)

    for i in friend_watched_list:
        if i not in user_watched_list:
            friend_unique_movies.append(i)
    
    for i in friend_unique_movies:
        if i not in friend_unique_movies_no_duplicates:
            friend_unique_movies_no_duplicates.append(i)
    return friend_unique_movies_no_duplicates
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recs = []
    movies_from_friends = get_friends_unique_watched(user_data)
    for i in range(len(movies_from_friends)):
        if (movies_from_friends[i]['host']) in user_data['subscriptions']:
            recs.append(movies_from_friends[i])
    return recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    user_most_frequent_genre = get_most_watched_genre(user_data)
    recs = []
    friend_has_watched = get_friends_unique_watched(user_data)
    for i in range(len(friend_has_watched)):
        if friend_has_watched[i]["genre"] == user_most_frequent_genre:
            recs.append(friend_has_watched[i])
    return recs

def get_rec_from_favorites(user_data):
    user_fav_movies = []
    friend_watched_list = []
    recs = []

    for movie in user_data["favorites"]:
        user_fav_movies.append(movie)

    for friend_movie in user_data['friends']:
        for movie in friend_movie['watched']:
            friend_watched_list.append(movie)

    for fav_movie in user_fav_movies:
        if fav_movie not in friend_watched_list:
            recs.append(fav_movie)
    return recs

