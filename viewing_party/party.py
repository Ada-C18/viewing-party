# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
    # return None for incorrect inputs
    if title == None or genre == None or rating == None:
        return None
    # create a dictionary with the given input
    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    # return the dictionary
    return new_movie

# add movie dict to watched list
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

# add movie dict to watchlist
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# move movie dict from watchlist to watched list
def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    # return 0 for an empty list
    if len(user_data["watched"]) == 0:
        return 0
    # set variables
    movie_count = 0
    sum_ratings = 0
    # take sum of all ratings
    for movie in user_data["watched"]:
        movie_count += 1
        rating = movie["rating"]
        sum_ratings += rating
    # calculate average rating
    average_rating = sum_ratings / movie_count
    return average_rating

    


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

