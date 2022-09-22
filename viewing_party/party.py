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
# Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify user_data.?

# 1. Calculate the average rating of all movies in the watched list
# The average rating of an empty watched list is 0.0
# return the average rating

def get_watched_avg_rating(user_data):
    rating_total = 0
    watched_lst = user_data["watched"]
    watched_lst_length = len(watched_lst)

    if watched_lst_length == 0:
        return 0.0

    for movie in watched_lst:
        rating_total += movie["rating"]
    return rating_total / watched_lst_length


# 2. Determine which genre is most frequently occurring in the watched list
# return the genre that is the most frequently watched
# If the value of "watched" is an empty list, get_most_watched_genre should return None.

def get_most_watched_genre(user_data):
    watched_lst = user_data["watched"]
    genre_dict = {}

    if len(watched_lst) == 0:
        return None

    for movie in watched_lst:
        if movie["genre"] in genre_dict:
            genre_dict[movie["genre"]] += 1
        else:
            genre_dict[movie["genre"]] = 1
    
    current_highest = 0
    current_genre = None
    for genre, num in genre_dict.items():
        if num > current_highest:
            current_highest = num
            current_genre = genre
    return current_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    watched_lst = user_data["watched"]
    friends_lst = user_data["friends"]
    unique_watched_lst = []

    for movie in watched_lst:
        seen_movie = False
        for friend in friends_lst:
            if movie in friend["watched"]:
                seen_movie = True
        
        if seen_movie == False:
            unique_watched_lst.append(movie)

    return unique_watched_lst


def get_friends_unique_watched(user_data):
    user_watched_lst = user_data["watched"]
    friends_lst = user_data["friends"]

    user_not_watched = []

    for friend in friends_lst:
        for movie in friend["watched"]:
            if movie not in user_watched_lst and movie not in user_not_watched:
                user_not_watched.append(movie)

    return user_not_watched

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
# 1. Create a function named get_available_recs. 
# Determine a list of recommended movies. A movie should be added to this list if and only if:
# The user has not watched it
# At least one of the user's friends has watched
# The "host" of the movie is a service that is in the user's "subscriptions"

# REQ 1: if movie not in user's watched list
# REQ 2: if movie in at least 1 friend's watched list
# REQ 3: if "host" str is in user's subscriptions lst

# Return the list of recommended movies

def get_available_recs(user_data):
    user_watched_lst = user_data["watched"]
    friends_lst = user_data["friends"]
    subscriptions = user_data["subscriptions"]
    
    recommended_movies = []

    for friend in friends_lst:
        for movie in friend["watched"]:
            if movie not in user_watched_lst and movie["host"] in subscriptions and movie not in recommended_movies:
                recommended_movies.append(movie)

    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    user_watched_lst = user_data["watched"]
    friends_lst = user_data["friends"]

    recommended_movies = []
    most_freq_genre = get_most_freq_genre(user_data)

    for friend in friends_lst:
        for movie in friend["watched"]:
            if movie not in user_watched_lst and movie["genre"] == most_freq_genre and movie not in recommended_movies:
                recommended_movies.append(movie)

    return recommended_movies

# Helper for get_new_rec_by_genre
def get_most_freq_genre(user_data):
    user_watched_lst = user_data["watched"]
    genre_dict = {}

    for movie in user_watched_lst:
        genre = movie["genre"]
        if genre in genre_dict:
            genre_dict[genre] += 1
        else:
            genre_dict[genre] = 1
    
    most_freq_genre = (None, 0)
    for genre in genre_dict:
        genre_count = genre_dict[genre]
        if genre_count > most_freq_genre[1]:
            most_freq_genre = (genre, genre_count)

    return most_freq_genre[0]


def get_rec_from_favorites(user_data):
    friends_lst = user_data["friends"]
    users_favorites = user_data["favorites"]

    rec_from_favorites = list(users_favorites)

    for friend in friends_lst:
        for movie in friend["watched"]:
            if movie in rec_from_favorites:
                rec_from_favorites.remove(movie)

    return rec_from_favorites