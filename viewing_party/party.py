# ------------- WAVE 1 --------------------

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(title, genre, rating):
    new_movie = {}
    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie
    
    return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    if len(user_data.get("watched")) == 0:
        return 0.0

    rating_average = 0
    for movie in user_data.get("watched"):
        rating_average += movie["rating"]
    return rating_average / len(user_data.get("watched"))

def get_most_watched_genre(user_data):
    if len(user_data.get("watched")) == 0:
        return None

    popular_genre = {}
    for movie in user_data.get("watched"):
        genre = movie["genre"]
        if genre not in popular_genre:
            popular_genre[genre] = 1
        else:
            popular_genre[genre] += 1

    genre_count = 0
    most_popular_genre = ""
    for g, value in popular_genre.items():
        if value > genre_count:
            genre_count = value
            most_popular_genre = g
    return most_popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

