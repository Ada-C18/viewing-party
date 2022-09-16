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

def get_most_watched_genre(user_data):
    # set empty dict
    genre_counts = {
        "Horror" : 0,
        "Fantasy" : 0,
        "Action" : 0,
        "Intrigue" : 0
    }
    # fill dict with genre counts
    for movie in user_data["watched"]:
        if movie["genre"] == "Horror":
            genre_counts["Horror"] += 1
        elif movie["genre"] == "Fantasy":
            genre_counts["Fantasy"] += 1
        elif movie["genre"] == "Action":
            genre_counts["Action"] += 1
        elif movie["genre"] == "Intrigue":
            genre_counts["Intrigue"] += 1
    # find most-watched genre
    # it will miss ties!
    highest_genre_count = max(genre_counts.values())
    for genre in genre_counts:
        if genre_counts[genre] == highest_genre_count:
            return genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

