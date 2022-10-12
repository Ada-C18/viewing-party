# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
    '''Add new movie to dict if title, genre and rating are truthy'''
    new_movie = {}

    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating

        return new_movie


def add_to_watched(user_data, movie):
    '''Add movie to watched movies list in user_data'''
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    '''Add movie to watchlist in user_data'''
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    '''Move movie from watchlist to watched in user_data'''
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data['watched'].append(movie)
            user_data["watchlist"].remove(movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    '''Calculate avg rating of watched movies in user data'''
    average = 0.0
    rating_total = 0.0
    
    for i in range(len(user_data["watched"])):
        rating_total += user_data["watched"][i]["rating"]
    
    if len(user_data['watched']) == 0:
        average == 0.0
    else:
        average = rating_total / len(user_data["watched"])
    
    return average


def get_most_watched_genre(user_data):
    '''Returning the genre watched the most times in user_data'''
    genres = []
    genre_count = {}

    for movie in user_data["watched"]:
        genres.append(movie["genre"])

    # create dict of genres and how many times they appear in genres list
    for genre in genres:
        if genre not in genre_count:
            genre_count[genre] = 1    
        else:
            genre_count[genre] += 1 

    # get max value of genre count
    if len(genre_count) > 0:
        max_genre = max(genre_count.values())     

    # dealing with ties of genre counts
    max_genres = []
    for genre in genre_count:
        if genre_count[genre] == max_genre:
            max_genres.append(genre)
    
    # returning single genre or list of genres depending on tie
    if len(max_genres) == 1:
        return max_genres[0]
    elif len(max_genres) > 1:
        return max_genres
    else:
        return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

from copy import copy
def get_unique_watched(user_data):
    '''Returning list of unique movies watched by user'''
    # make copy of user_data watched to use as list to remove movies also watched by friends
    unique_movies = copy(user_data["watched"])

    for my_movie in user_data["watched"]: #access list in user watched
        for friend in user_data["friends"]: #access friend lists in user friends
            for friend_movie in friend["watched"]: #access movie list in each friend watched
                if my_movie["title"] == friend_movie["title"] and my_movie in unique_movies:
                    unique_movies.remove(my_movie)

    return unique_movies
    
 
def get_friends_unique_watched(user_data):
    '''Returning list of unique movies watched by friends and not user'''
    friend_movies = []

    #create combined friend movie list
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friend_movies:
                friend_movies.append(movie)
    
    #compare user movies to friend movies    
    for my_movie in user_data["watched"]:
        for movie in friend_movies:
            if movie["title"] == my_movie["title"]:
                friend_movies.remove(movie)

    return friend_movies
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    '''Creating friend movie recommendation list for user. User must have subscription
    service where movie is streamed and not seen the movies yet'''

    recommended_movies = []
    
    # get list of friend movies not in user watched list
    friend_movies = get_friends_unique_watched(user_data)

    # check if user subscriptions includes friend movie host
    for movie in friend_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    '''Creating friend recommended movie list if user has not seen it and
    genre matches user most frequently watched genre'''
    recommended_movies = []
    user_most_watched_genre = get_most_watched_genre(user_data)
    friend_unique_movies = get_friends_unique_watched(user_data)

    for movie in friend_unique_movies:
        if movie["genre"] == user_most_watched_genre:
            recommended_movies.append(movie)
        
    return recommended_movies


def get_rec_from_favorites(user_data):
    '''Creating user recommended movie list for friends. User movies are favorites and have
    not been watched by friends'''
    recommended_movies =[]
    friend_watched_movies = []
    
    # Get list of movies watched by all friends
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched_movies.append(movie)

    for movie in user_data["favorites"]:
        if movie not in friend_watched_movies:
            recommended_movies.append(movie)
    
    return recommended_movies



# import json
# print(json.dumps(user_data,indent=2)
# max(stats, key=stats.get)