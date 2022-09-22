# ------------- WAVE 1 --------------------

from sys import breakpointhook


def create_movie(title, genre, rating):
    
    movie = {}
    
    if not title or not genre or not rating:
        return None
    else:    
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
    
    return movie

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data['watchlist']
    watched = user_data['watched']

    for movie in watchlist:        
        if movie['title'] == title:
            watchlist.remove(movie)
            watched.append(movie)
            

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total_rating = 0.0
    avg_rating = 0.0
    watched = user_data['watched']

# I originally had this as an if clause but I figured why not practice?
# 'if watched' would avoid a ZeroDivisionError when len(watched) == 0

    try:
        for movie in watched:
            total_rating += movie['rating']
        
        avg_rating = total_rating / len(watched)
    
    except ZeroDivisionError:
        avg_rating = 0.0

    return avg_rating

def get_most_watched_genre(user_data):
    watched = user_data['watched']
    genre_dict = {}

    # because we don't know the genres that the user has watched,
    # we have to determine what these are and initialize each dictionary key
    # before we can increment the genres.

    # Didn't bother to do exception handling here because the if statement
    # seems cleaner in terms of the function's logic. Calling max on an empty
    # dictionary would produce a ValueError.

    if watched:        
        for movie in watched:
            if movie['genre'] not in genre_dict:
                genre_dict[movie['genre']] = 1
            else:
                genre_dict[movie['genre']] += 1
        return max(genre_dict, key = genre_dict.get)

    else:
        return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# we want to ensure uniqueness by grabbing/comparing both title and genre.
# we want to have a clean comparison by not grabbing rating.

def create_user_watched_set(user_data):

    # I was on the fence about creating the 'watched' variable here.
    # The function's pretty clear without it and we only have to use it once
    # but might it be cleaner to use it since I assign this variable in almost all
    # of my earlier functions? I found having the variable there helpful for the debugging
    # watch list, for example, because it was always already set up. Thoughts appreciated.

    user_watched = set()

    for movie in user_data['watched']:
        user_watched.add((movie['title'], movie['genre']))

    return user_watched

def create_friends_watched_set(user_data):
    friends_watched = set()

    for friend in user_data['friends']:
        for movie in friend['watched']:
            friends_watched.add((movie['title'], movie['genre']))
    
    return friends_watched

def get_unique_watched(user_data):
    watched = user_data['watched']
    unique_movies = []

    user_unique_watched = (create_user_watched_set(user_data)
        - create_friends_watched_set(user_data))

    for movie in watched:
        for entry in user_unique_watched:
            if entry == (movie['title'], movie['genre']):
                unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):
    friends = user_data['friends']
    friends_unique_movies = []

    friends_unique_watched = (create_friends_watched_set(user_data) - 
        create_user_watched_set(user_data))
    
    for friend in friends:
        for movie in friend['watched']:
            for entry in friends_unique_watched:
                if entry == (movie['title'], movie['genre']):
                    if movie in friends_unique_movies:
                        continue
                    else:
                        friends_unique_movies.append(movie)

    return friends_unique_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    
    # making sure that this is robust to subscriptions not existing because
    # it's not in the Arrange section of the test where Sonya has no friends.
    
    subscriptions = user_data.get('subscriptions', [])
    available_recs = []

    friends_unique = get_friends_unique_watched(user_data)

    for movie in friends_unique:
        if movie['host'] in subscriptions:
            available_recs.append(movie)

    return available_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    rec_genre = get_most_watched_genre(user_data)
    available_recs = get_available_recs(user_data)
    movie_recs_by_genre = []

    for movie in available_recs:
        if movie['genre'] == rec_genre:
            movie_recs_by_genre.append(movie)
    
    return movie_recs_by_genre

def get_rec_from_favorites(user_data):
    available_recs = get_unique_watched(user_data)
    recs_in_favorites = []

    for movie in available_recs:
        if movie in user_data['favorites']:
            recs_in_favorites.append(movie)
    
    return recs_in_favorites