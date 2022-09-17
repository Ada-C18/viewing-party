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

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

