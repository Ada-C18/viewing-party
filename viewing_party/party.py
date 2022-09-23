# ------------- WAVE 1 --------------------
# this is my first commit 

from operator import ge

from tests.test_constants import USER_DATA_4


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
    unique_movies = []

    for movie in user_data["watched"]:
        unique_movies.append(movie)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            
            if movie in unique_movies:
                unique_movies.remove(movie)
            
    return unique_movies

def get_friends_unique_watched(user_data):
    friends_unique_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_unique_movies:
                friends_unique_movies.append(movie)
    
    for movie in user_data["watched"]:
        if movie in friends_unique_movies:
            friends_unique_movies.remove(movie)
    
    return friends_unique_movies
    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recs = get_friends_unique_watched(user_data)
    if len(recs) == 0:
        return recs
    else:
        for movie in recs:
            if movie["host"] not in user_data["subscriptions"]:
                recs.remove(movie)

    return recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
