# ------------- WAVE 1 --------------------

from collections import Counter
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
    for watched_list in user_data.values():
        watched_list.append(movie)

    updated_data = user_data
    return updated_data

def add_to_watchlist(user_data, movie):
    for watched_list in user_data.values():
        watched_list.append(movie)

    updated_data = user_data
    return updated_data

def watch_movie(janes_data, title):
    watched = {}
    for watchlist_list in janes_data.values():
        if not watchlist_list:
            pass
        else:
            for i in range(len(watchlist_list)):
                if watchlist_list[i]['title'] == title:
                    watched = watchlist_list.pop(i)
    if watched: 
        janes_data["watched"].append(watched)
    updated_data = janes_data
    return updated_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(janes_data):
# input: users data dict with list {[watched]}
# janes_data = {
#   "watched" : [{movie: blah, rating: blah}]
# }
# calculate average of movies in watched list
    sum_of_ratings = 0
    for watched_list in janes_data.values():
        if not watched_list:
            return 0
        else:
            for i in range(len(watched_list)):
                sum_of_ratings += watched_list[i]['rating']
    return sum_of_ratings/len(watched_list)    

def get_most_watched_genre(janes_data):
    watched_genres = []
    for watched_list in janes_data.values():
        if not watched_list:
            return None
        else:
            for i in range(len(watched_list)):
                watched_genres.append(watched_list[i]['genre'])
    popular_genre = Counter(watched_genres).most_common(1)[0][0]
    return popular_genre
    
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
# return what their friends have watched but not user
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

# input
# user data = {"watched":[]
# "friends": ["watched":{movie:movie, genre:}, "watched:{movie:move, genre:genere"]
# "subscriptions": ["hulu", "disney"]
# }
# use get unique watched which is movies friend has seen but not user
# movies_from_friends = get_friends_unique_watched(user_data)
# Determine a list of recommended movies. A movie should be added to this list if and only if:
# The user has not watched it
# At least one of the user's friends has watched
# The "host" of the movie is a service that is in the user's "subscriptions"
# Return the list of recommended movies
# recommended_movies = []
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

