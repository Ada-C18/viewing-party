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
# 1. Create a function named `get_watched_avg_rating`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries
#     - This represents that the user has a list of watched movies
# - Calculate the average rating of all movies in the watched list
#   - The average rating of an empty watched list is `0.0`
# - return the average rating

def get_watched_avg_rating(user_data):
    # print(user_data)
    average = 0.0
    rating_total = 0.0
    for i in range(len(user_data["watched"])):
        print(user_data["watched"][i]["rating"])
        rating_total += user_data["watched"][i]["rating"]
    average = rating_total / len(user_data["watched"])
    return average

# 2. Create a function named `get_most_watched_genre`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries. Each movie dictionary has a key `"genre"`.
#     - This represents that the user has a list of watched movies. Each watched movie has a genre.
#     - The values of `"genre"` is a string.
# - Determine which genre is most frequently occurring in the watched list
# - return the genre that is the most frequently watched
# - If the value of "watched" is an empty list, `get_most_watched_genre` should return `None`.


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

