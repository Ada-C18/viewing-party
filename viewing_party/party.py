from contextlib import nullcontext
from logging import log
from re import U
from collections import Counter

# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    
    if None in (title, genre, rating):
    
        return None
    
    create_movie_dict= {'title': title, 'genre': genre, 'rating': rating}
        
    return create_movie_dict
    pass


def add_to_watched(user_data, movie):
    
    for watched_movie in user_data['watched']:
        if movie['title'] == watched_movie['title']:
            
            return None
        
    user_data['watched'].append(movie)
   
    return user_data

def add_to_watchlist(user_data, movie):
   
    while len(user_data['watchlist']) > 1: 
    
        for movie in user_data["watchlist"]:
            if movie['title'] == user_data["watchlist"]:
            
                return None
    
    user_data["watchlist"].append(movie)
    
    return user_data

def watch_movie(user_data, title):
    
    for movie in (user_data['watchlist']).copy():
        if movie['title'] == title:
            (user_data['watchlist']).remove(movie)
            user_data["watched"].append(movie)
            
    
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):

    ratings = []
    total = 0.0
   
    for movie in (user_data['watched']):
        ratings.append(float(movie['rating']))
    
    for rate in range(len(ratings)):
        movie_rating = ratings[rate]
        total += movie_rating
    
    total_movies = float(len(user_data['watched']))
    
    if total_movies > 0:
        avg_rating = total/total_movies 
        return avg_rating 
    else:
        return 0.0

def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]

def get_most_watched_genre(user_data):
    genres = []
    
    for movie in (user_data['watched']):
        genres.append(movie['genre'])
    
    if len(genres)> 1:
        return most_frequent(genres)
    else:
        return None
           
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
    
def get_unique_watched(user_data):
    
    users_watched_movies = user_data['watched']
    friends_watched_movies = []
    friends_movie_list = []
    users_movie_list =[]
    unique_list = []
    unique_list_dict = []
    
    
    for movie in user_data['friends']:
        movie_list = movie['watched']
        for dict in movie_list:
            friends_watched_movies.append(dict)
            
    if len(friends_watched_movies) > 1:      
        for movie in friends_watched_movies:
            movie_name = movie['title']
            friends_movie_list.append(movie_name)
            
    for movie in users_watched_movies:
        movie_name = movie['title']
        users_movie_list.append(movie_name)
            
    for movie in users_movie_list:
        if movie not in friends_movie_list:
            unique_list.append(movie)
                
    for movie in users_watched_movies:
        movie_name = movie['title']
    
        if movie_name in unique_list:
            unique_list_dict.append(movie)   
        
    return unique_list_dict    
      
def get_friends_unique_watched(user_data):
    users_watched_movies = user_data['watched']
    friends_watched_movies = []
    friends_movie_list = []
    users_movie_list =[]
    unique_list = []
    unique_list_dict = []
    
    for movie in user_data['friends']:
        movie_list = movie['watched']
        for dict in movie_list:
            if dict not in friends_watched_movies:
                friends_watched_movies.append(dict)
            
    if len(friends_watched_movies) > 1:      
        for movie in friends_watched_movies:
            movie_name = movie['title']
            friends_movie_list.append(movie_name)
            
        for movie in users_watched_movies:
            movie_name = movie['title']
            users_movie_list.append(movie_name)  
        
        for movie in friends_movie_list:
            if movie not in users_movie_list:
                unique_list.append(movie)
        
        for movie in friends_watched_movies:
            movie_name = movie['title']
    
            if movie_name in unique_list:
                unique_list_dict.append(movie)
               
    return unique_list_dict
              
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs (user_data):
    recommended_movies = []
    movie_user_not_watch = get_friends_unique_watched(user_data)
    user_subscriptions = user_data['subscriptions']
    
    for movie in movie_user_not_watch:
        if movie['host'] in user_subscriptions:
            recommended_movies.append(movie)
    
    return recommended_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):

    recommended_movies = []
    most_frequent_genre = get_most_watched_genre(user_data)
    movie_user_not_watch = get_friends_unique_watched(user_data)
    
    for movie in movie_user_not_watch:
        if movie['genre'] == most_frequent_genre:
            recommended_movies.append(movie)
            
    return recommended_movies


def get_rec_from_favorites(user_data):
    recommended_movies = []
    user_only_watched_movies = get_unique_watched(user_data)
    user_only_watched_movies_list =[]
    user_fav_movies = user_data['favorites']
    
    for movie in user_only_watched_movies:
        if movie['title'] not in user_only_watched_movies_list:
            user_only_watched_movies_list.append(movie['title'])
    
    for movie in user_fav_movies:
        if movie['title'] in user_only_watched_movies_list:
            recommended_movies.append(movie)
            
    return get_unique_watched(user_data)
    
