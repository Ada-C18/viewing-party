import math
from queue import Empty
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    if not title or not genre or not rating:
        new_movie = None

    return new_movie

def add_to_watched(user_data, movie):
    
    updated_user_data = user_data.copy()
    updated_user_data["watched"].append(movie)

    return updated_user_data

def add_to_watchlist(user_data, movie):

    updated_user_data = user_data.copy()
    updated_user_data["watchlist"].append(movie)

    return updated_user_data

def watch_movie(user_data, title):
    
    title_list = []

    for dicts in user_data["watchlist"]:
        title_list.append(dicts["title"])

    for dicts in user_data["watched"]:
        title_list.append(dicts["title"])
        
    if title in title_list:
        updated_user_data = user_data.copy()
        updated_user_data["watched"].append(updated_user_data["watchlist"].copy())
        updated_user_data["watchlist"].pop()
        
        return updated_user_data
    
    else:
        return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    
    watched_list = list(user_data.values())
    
    try:
        ratings_list = [sub['rating'] for sub in watched_list[0]]
        ratings_sum = math.fsum(ratings_list)
        avg_rating = ratings_sum/len(ratings_list)
        
        return avg_rating
    
    except ZeroDivisionError:
        avg_rating = 0
        
        return avg_rating
        
def get_most_watched_genre(user_data):
    watched_list = list(user_data.values())
    genre_list = [sub['genre'] for sub in watched_list[0]]
    
    if not genre_list:
        return None
    else:
        most_frequent_genre = max(set(genre_list), key = genre_list.count)
        
        return most_frequent_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_watch_list = user_data["watched"]
    
    friends_list = user_data["friends"]
    
    friends_watch_list = []
    for dicts in friends_list:
        friends_watch_list.append(dicts["watched"])
        
    friends_watch_list = [val for sublist in friends_watch_list for val in sublist]

    unique_friend_watch = list({val["title"]:val for val in friends_watch_list}.values())
    
    for val in unique_friend_watch:
        if val in user_watch_list:
            user_watch_list.remove(val)
            
    return user_watch_list

def get_friends_unique_watched(user_data):
    
    user_watch_list = user_data["watched"]
    
    friends_list = user_data["friends"]
    
    friends_watch_list = []
    for dicts in friends_list:
        friends_watch_list.append(dicts["watched"])
        
    friends_watch_list = [val for sublist in friends_watch_list for val in sublist]
    
    unique_friend_watch = list({val["title"]: val for val in friends_watch_list}.values())
    
    for val in user_watch_list:
        if val in unique_friend_watch:
            unique_friend_watch.remove(val)
            
    return unique_friend_watch
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

