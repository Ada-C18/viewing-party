# ------------- WAVE 1 --------------------
import statistics
from statistics import mode


def create_movie(title, genre, rating):
    movies = {
        'title':title,
        'genre':genre,
        'rating':rating,
    }   
    if not title or not genre or not rating:
        return None
    else:
        return movies


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    
    return user_data


def add_to_watchlist(user_data,movie):    
    user_data["watchlist"].append(movie)

    return user_data


def watch_movie(user_data, title):
    movie_to_watch = user_data["watchlist"]
    for movie in movie_to_watch:
        if title == movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0
    for i in range (len(user_data['watched'])):   
        movie = user_data['watched'][i]
        movie_r = movie['rating']
        sum += movie_r

    if (len(user_data['watched'])) == 0:
        return 0.0
    else:
        return sum / len(user_data['watched']) 

def get_most_watched_genre(user_data):
    movie_g_list = []
    for i in range (len(user_data['watched'])):   
        movie = user_data['watched'][i]
        movie_g = movie['genre'] 
        movie_g_list.append(movie_g)
    if user_data['watched'] == []:
        return None    
    else: 
        return(mode(movie_g_list))       

    # -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    friends = user_data['friends']
    friends_mediocre_movies = []
    my_watched = user_data['watched']
    cool_movies_watched = []
    unique_movies = []
    for my_movies in my_watched:
        cool_movies_watched.append(my_movies)

    for friends_watched in friends:
        for friends_movies in friends_watched['watched']:
            friends_mediocre_movies.append(friends_movies)
        
    for movie in cool_movies_watched:
        if not movie in friends_mediocre_movies and movie not in unique_movies:
            unique_movies.append(movie)
    return unique_movies        
    

def get_friends_unique_watched(user_data):
    friends = user_data['friends']
    friends_mediocre_movies = []
    my_watched = user_data['watched']
    cool_movies_watched = []
    unique_movies = []
    for my_movies in my_watched:
        cool_movies_watched.append(my_movies)

    for friends_watched in friends:
        for friends_movies in friends_watched['watched']:
            friends_mediocre_movies.append(friends_movies)
        
    for movie in friends_mediocre_movies:
        if not movie in cool_movies_watched and movie not in unique_movies: 
            unique_movies.append(movie)
    return unique_movies

    

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------