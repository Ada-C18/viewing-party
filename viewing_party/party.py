# ------------- WAVE 1 --------------------
# this is my first commit 

from operator import ge


def create_movie(title, genre, rating):
    
    if title and genre and rating:
        movie = {}
        
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie

    else:
        return None

def add_to_watched(user_data, movie):
    prev = user_data["watched"] 
    curr = prev.append(movie) 
    
    return user_data

def add_to_watchlist(user_data, movie):
    prev = user_data["watchlist"]
    curr = prev.append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
    return user_data

# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    sum = 0
    average = 0
    
    for i in range(len(user_data["watched"])):
        sum += user_data["watched"][i]["rating"]
    if sum > 0:
        average = sum / len(user_data["watched"])

    return average
#
def get_most_watched_genre(user_data): 
    genre_count = {}
    current_top = 0
    current_genre = " "

    for i in range(len(user_data["watched"])): 
        genre = user_data["watched"][i]["genre"]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1
    
    genres = genre_count.keys()
    for genre in genres:
        if genre_count[genre] > current_top:
            current_top = genre_count[genre]
            current_genre = genre
    
    if user_data["watched"] == []:
        return None
    
    return current_genre

# ------------- WAVE 3 --------------------

def get_unique_watched(user_data):


    # input is the dict of movies
    # output is the unique_movies = [] (empty list) or unique_movies = list of the objects 
    # need to know titles from user_data then titles from friends
    # loop through titles and see if any titles existed in the friends list
    # is title in friends user_data


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
