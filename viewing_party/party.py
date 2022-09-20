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
    # print(f"genres: {genres}")

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
        for friend in user_data["friends"]: #access lists in each friend
            for friend_movie in friend["watched"]: #access list in friend
                if my_movie["title"] == friend_movie["title"] and my_movie in unique_movies:
                    unique_movies.remove(my_movie)

    return unique_movies
    
 
def get_friends_unique_watched(user_data):
    '''Returning list of unique movies watched by friends'''
    friend_movies = []
    # print(json.dumps(user_data,indent=2))
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
    # print("json at get_available_recs")
    # print(json.dumps(user_data,indent=2))
    pass
    '''Creating friend movie recommendation list for user. User must have subscription
    service where movie is streamed and not seen the movies yet'''
    # list to return
    recommended_movies = []
    
    # get list of friend movies not in user watched list
    friend_movies = get_friends_unique_watched(user_data)
    print(f"{friend_movies=}")

    # check if user subscriptions includes friend movie host
    for movie in friend_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# 1. Create a function named  `get_new_rec_by_genre`. This function should...

# - take one parameter: `user_data`
# - Consider the user's most frequently watched genre. Then, determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"genre"` of the movie is the same as the user's most frequent genre
# - Return the list of recommended movies

def get_new_rec_by_genre(user_data):
    '''Creating friend recommended movie list if user has not seen it and
    genre matches user most frequently watched genre'''
    # print("json at get_new_rec_by_genre")
    # print(json.dumps(user_data,indent=2))
    recommended_movies = []
    user_most_watched_genre = get_most_watched_genre(user_data)
    friend_unique_movies = get_friends_unique_watched(user_data)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie in friend_unique_movies and movie["genre"] == user_most_watched_genre:
                recommended_movies.append(movie)
        
    return recommended_movies

# 2. Create a function named  `get_rec_from_favorites`. This function should...

# - take one parameter: `user_data`
#   - `user_data` will have a field `"favorites"`. The value of `"favorites"` is a list of movie dictionaries
#     - This represents the user's favorite movies
# - Determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The movie is in the user's `"favorites"`
#   - None of the user's friends have watched it
# - Return the list of recommended movies

def get_rec_from_favorites(user_data):
    print("json at get_rec_from_favorites")
    print(json.dumps(user_data,indent=2))
    recommended_movies =[]
    
    friend_watched_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched_movies.append(movie)


    for movie in user_data["favorites"]:
        if movie not in friend_watched_movies:
            recommended_movies.append(movie)
    
    return recommended_movies

