# ------------- WAVE 1 --------------------

from enum import unique


def create_movie(title, genre, rating):
    if title and genre and rating:
        new_movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):

    for movie in user_data["watchlist"]:
        if title in movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            
    return user_data
            

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    total_ratings = 0
    number_of_movies = len(user_data["watched"])

    for movie_dict in user_data["watched"]:
        total_ratings += movie_dict["rating"]

    if number_of_movies == 0:
        average_rating = 0.0
    else:
        average_rating = total_ratings/number_of_movies

    return average_rating

# my_data = {"watched": [{"title": "scary movie", "genre": "horror", "rating": "3"}, {"title": "another scary movie", "genre": "horror", "rating": "2"}, {"title": "funny movie", "genre": "comedy", "rating": "5"}]}
def get_most_watched_genre(user_data):
    genre_freq_dict = {}
    
    for movie_dict in user_data["watched"]:

        if movie_dict["genre"] not in genre_freq_dict:
            genre_freq_dict[movie_dict["genre"]] = 1
        else:
            genre_freq_dict[movie_dict["genre"]] += 1
    
    if user_data["watched"] == []:
        max_genre = None
    else:
        max_genre = max(genre_freq_dict, key=genre_freq_dict.get)

    return max_genre
  

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    user_movies = user_data["watched"]
    friend_movies = []
    user_unique_movies = []

    for index in user_data["friends"]:
        for watched_list in index["watched"]:
                friend_movies.append(watched_list)

    for movie in user_movies:
        if movie not in friend_movies:
            user_unique_movies.append(movie)

    return user_unique_movies

def get_friends_unique_watched(user_data):
    user_movies = user_data["watched"]
    friend_movies = []
    friend_unique_movies = []

    for index in user_data["friends"]:
        for watched_list in index["watched"]:
                friend_movies.append(watched_list)

    for movie in friend_movies:
        if movie not in user_movies and movie not in friend_unique_movies:
            friend_unique_movies.append(movie)

    return friend_unique_movies
    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies_list = []

    potential_movies = get_friends_unique_watched(user_data)
# loop through the host of the friends unique movies and
# see which hosts are in the users movies hosts
    for movie in potential_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies_list.append(movie)

    return recommended_movies_list  
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):

#Find the most frequently watched genre in users movies
    freq_genre = get_most_watched_genre(user_data)
# Find movies the user hasn't watched but at least one of their friend's have watched
    unique_friends_movies = get_friends_unique_watched(user_data)

# find which movies in the unique_friends_movies list has the same genre as...
# the users most frequent watched genre
    rec_movies = []    

    for movie in unique_friends_movies:
        if freq_genre == None:
            break
        if freq_genre in movie["genre"]:
            rec_movies.append(movie)
    return rec_movies

def get_rec_from_favorites(user_data):
    rec_movies = []
    unique_movies = get_unique_watched(user_data)
    for movie in user_data["favorites"]:
        if movie in unique_movies:
            rec_movies.append(movie)

    return rec_movies