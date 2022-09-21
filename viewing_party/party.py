# import json
# print(json.dumps(user_data,indent=2))
# ------------- WAVE 1 --------------------
# 1. Create a function named  `create_movie`. This function and all subsequent functions should be in `party.py`. 

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {}
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    return None

# 2. Create a function named `add_to_watched`.
# test: test_adds_movie_to_user_watched
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

# 3. Create a function named add_to_watchlist.def 
# test: test_adds_movie_to_user_watchlist()
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# 4. Create a function named watch_movie.
# TODO: move dict from watchlist to watched list if movie in user's watchlist
# OUTPUT: user_data (modified user_data if title in watchlist)
# test_moves_movie_from_watchlist_to_watched
def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    for movie in watchlist:
        if title == movie["title"]:
            # will remove it from same list in location in memory
            watchlist.remove(movie)
            user_data["watched"].append(movie)
            break
    # return outside for loop to ensure we iterate entire list
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
# Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify user_data.
# 1. Calculate the average rating of all movies in the watched list
# The average rating of an empty watched list is 0.0
# return the average rating

def get_watched_avg_rating(user_data):
    sum_rating = 0
    watched_lst = user_data["watched"]
    watched_lst_length = len(watched_lst)

    if watched_lst_length == 0:
        return 0.0

    for movie in watched_lst:
        sum_rating += movie["rating"]
    return sum_rating / watched_lst_length


# 2. Determine which genre is most frequently occurring in the watched list
# return the genre that is the most frequently watched
# If the value of "watched" is an empty list, get_most_watched_genre should return None.

def get_most_watched_genre(user_data):
    watched_lst = user_data["watched"]
    # 1. create genre dict 
    genre_dict = {}
    # 2. return None if watched list empty
    if len(watched_lst) == 0:
        return None
    # 3. populate genre dict
    # -- iterate
    for movie in watched_lst:
        if movie["genre"] in genre_dict:
            genre_dict[movie["genre"]] += 1
        else:
            genre_dict[movie["genre"]] = 1
    
    # 4. compare values / num of occurrences
    # -- return highest
    current_highest = 0
    current_genre = 0
    for genre, num in genre_dict.items():
        if num > current_highest:
            current_highest = num
            current_genre = genre
    return current_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
# 1. Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies the user has watched, but none of their friends have watched.
# Return a list of dictionaries, that represents a list of movies


def get_unique_watched(user_data):
    # set
    # remove
    watched_lst = user_data["watched"]
    friends_lst = user_data["friends"]
    unique_watched_lst = watched_lst + friends_lst
    # print(unique_watched_lst)

    for movie in watched_lst:
        for friend in friends_lst:

    # TODO: add movie dict to unique lst => ONLY ONCE, FIX: remove duplicates
    # -- find same title in "watched" and "friends" lsts
            if movie in friend["watched"] :
                unique_watched_lst.append(movie)
            
            if movie in unique_watched_lst:
                unique_watched_lst.remove(movie)
    # 4. return lst output
    return unique_watched_lst

# 2. Create a function named get_friends_unique_watched.
# Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies at least one of the user's friends have watched, but the user has not watched.
# Return a list of dictionaries, that represents a list of movies
def get_friends_unique_watched(user_data):
    pass


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# 1. Create a function named get_available_recs. 
# Determine a list of recommended movies. A movie should be added to this list if and only if:
# The user has not watched it
# REQ 1: if movie not in user's watched list

# At least one of the user's friends has watched
# REQ 2: if movie in 1 friend's watched list

# The "host" of the movie is a service that is in the user's "subscriptions"
# REQ 3: if "host" str in user's subscriptions lst

# Return the list of recommended movies
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies_lst = []
    return recommended_movies_lst

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
# 1. Create a function named get_new_rec_by_genre(user_data) 

# Consider the user's most frequently watched genre. Then, determine a list of recommended movies. A movie should be added to this list if and only if:
# 1. The user has not watched it
# 2. At least one of the user's friends has watched
# 3. The "genre" of the movie is the same as the user's most frequent genre
# Return the list of recommended movies



# 2. Create a function named get_rec_from_favorites(user_data)

# user_data will have a field "favorites". The value of "favorites" is a list of movie dictionaries
# This represents the user's favorite movies
# Determine a list of recommended movies. A movie should be added to this list if and only if:
# 1. The movie is in the user's "favorites"
# 2. None of the user's friends have watched it
# Return the list of recommended movies
