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
# def get_unique_watched(user_data):
    

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------