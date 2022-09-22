# ------------- WAVE 1 --------------------

from enum import unique


def create_movie(title, genre, rating):
    dict = {}
    if title and genre and rating:
        dict['title'] = title
        dict['genre'] = genre
        dict['rating'] = rating
        return dict
    else:
        return None

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data['watchlist']
    for watchlist_movie in watchlist:
        if title == watchlist_movie['title']:
            movie = watchlist_movie
            result = add_to_watched(user_data, movie)
            user_data['watchlist'].remove(watchlist_movie)
            return result
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    avg_rating = 0.0
    rating_sum = 0.0
    watched = user_data['watched']
    if len(watched) != 0:
        for movie in watched:
            rating_sum += movie['rating']
        avg_rating = rating_sum/len(watched)
    return avg_rating

def get_most_watched_genre(user_data):
    genre_counter = {}
    watched = user_data['watched']
    most = ''
    if len(watched) != 0:
        for movie in watched:
            if movie['genre'] in genre_counter.keys():
                genre_counter[movie['genre']] += 1
            else:
                genre_counter[movie['genre']] = 0
        most = max(genre_counter, key = genre_counter.get)
        return most

    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_friends_watched_list(user_data):
    friends_watched = []
    friends_movies = user_data['friends']
    for watched_list in friends_movies:
        for friend_movie in watched_list['watched']:
            friends_watched.append(friend_movie)
    return friends_watched

def get_user_watched_list(user_data):
    watched_movies = []
    for user_movie in user_data['watched']:
        watched_movies.append(user_movie)
    return watched_movies

def get_unique_watched(user_data):
    user_unique = []
    friends_watched = get_friends_watched_list(user_data)
    user_watched = get_user_watched_list(user_data)
    for user_movie in user_watched:
        if user_movie not in friends_watched:
            user_unique.append(user_movie)
    return user_unique


def get_friends_unique_watched(user_data):
    unique_movies = []
    friends_movies = get_friends_watched_list(user_data)
    user_movies = get_user_watched_list(user_data)
    for movie in friends_movies:
        if movie not in user_movies and movie not in unique_movies:
            unique_movies.append(movie)
    return unique_movies

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    movie_recs = []
    subscriptions = user_data['subscriptions']
    watched_movies = get_user_watched_list(user_data)
    friends_watched = get_friends_watched_list(user_data)
    for movie in friends_watched:
        if movie not in watched_movies and movie['host'] in subscriptions:
                movie_recs.append(movie)
    return movie_recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    fav_genre = get_most_watched_genre(user_data)
    movie_recs = []
    watched_movies = watched_movies = get_user_watched_list(user_data)
    friends_watched = get_friends_watched_list(user_data)
    for movie in friends_watched:
        if movie not in watched_movies and movie['genre'] == fav_genre:
            movie_recs.append(movie)
    return movie_recs

def get_rec_from_favorites(user_data):
    movie_recs = []
    watched_movies = watched_movies = get_user_watched_list(user_data)
    friends_watched = get_friends_watched_list(user_data)
    for movie in watched_movies:
        if movie in user_data['favorites'] and movie not in friends_watched:
            movie_recs.append(movie)
    return movie_recs

