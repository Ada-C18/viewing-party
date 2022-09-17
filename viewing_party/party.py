import json
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    '''Add new movie if title, genre and rating are truthy'''
    new_movie = {}

    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    else:
        return None

    return new_movie


def add_to_watched(user_data, movie):
    '''Add movie to watched movies list in user data dict'''
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    '''Add movies to watchlist in user data dict'''
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    '''Move watched movies from watchlist to watched in user_data'''
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]['title'] == title:
            user_data['watched'].append(user_data['watchlist'][i])
            user_data["watchlist"].remove(user_data["watchlist"][i])

    return user_data

# Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify `user_data`.

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    '''Calculate avg rating of watched movies in user data'''
    print(user_data)
    average = 0.0
    rating_total = 0.0
    for i in range(len(user_data["watched"])):
        print(user_data["watched"][i]["rating"])
        rating_total += user_data["watched"][i]["rating"]
    
    if len(user_data['watched']) == 0:
        average == 0.0
    else:
        average = rating_total / len(user_data["watched"])
    
    return average


def get_most_watched_genre(user_data):
    '''Returning the genre watched the most times'''
    genres = []
    genre_count = {}
    for i in range(len(user_data["watched"])):
        genres.append(user_data['watched'][i]['genre'])
        genres.sort()
    print(f"genres: {genres}")

    for item in genres:
        if item not in genre_count:
            genre_count[item] = 0
        genre_count[item] += 1

    if len(genre_count) > 0:
        max_genre = max(genre_count, key=genre_count.get)       
        return max_genre
    else:
        return None

# max(stats, key=stats.get)
        

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

from copy import copy
def get_unique_watched(user_data):
    '''Returning list of unique movies watched by user'''
    unique_movies = copy(user_data["watched"])
    # print(json.dumps(user_data,indent=2)

    for my_movie in user_data["watched"]: #access list in user watched
        for friend in user_data["friends"]: #access list in each friend
            for friend_movie in friend["watched"]: #access list in friend
                if my_movie["title"] == friend_movie["title"] and my_movie in unique_movies:
                    unique_movies.remove(my_movie)

    return unique_movies

# 2. Create a function named `get_friends_unique_watched`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
#     - This represents that the user has a list of watched movies and a list of friends
#     - The value of `"friends"` is a list
#     - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
#     - Each movie dictionary has a `"title"`.
# - Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies at least one of the user's friends have watched, but the user has not watched.
# - Return a list of dictionaries, that represents a list of movies
 
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

