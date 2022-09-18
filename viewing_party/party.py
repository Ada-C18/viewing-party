# ------------- WAVE 1 --------------------

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(title, genre, rating):
    new_movie = {"title": [], "genre": [], "rating": []}

    new_movie["title"] = MOVIE_TITLE_1
    new_movie["genre"] = GENRE_1
    new_movie["rating"] = RATING_1

    if title and genre and rating:
        return new_movie
    else: 
        return None

    
def add_to_watched(user_data, movie):
    user_data = {"watched": []}
    
    movie = {
        "title": MOVIE_TITLE_1,
        "genre": GENRE_1,
        "rating": RATING_1
    }

    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {"watchlist": []}
    movie = {
    "title": MOVIE_TITLE_1,
    "genre": GENRE_1,
    "rating": RATING_1
    }
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):

    
    for key, value in user_data.items():
        if key == "watchlist":
            for i in value:
                for key, value in i.items():
                    if value == title:
                        user_data["watched"].append(title)
                        user_data["watchlist"].remove(i)
        else:
            return user_data
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_total = []
    for value in user_data.values():
        for i in value:
            for key, value in i.items():
                if key == "rating":
                    rating_total.append(value)
    if len(rating_total) != 0:
        return sum(rating_total)/len(rating_total)
    else: 
        return 0.0

def get_most_watched_genre(user_data):
    popular_genre = []
    for value in user_data.values():
        for i in value:
            for key, value in i.items():
                if key == "genre":
                    popular_genre.append(value)
    if len(popular_genre) != 0:
        return max(set(popular_genre), key = popular_genre.count)
    else: 
        return None
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friends_movie_list = []
    my_movie_list = []
    third_list = []

    for key, value in user_data.items():
        if key == "friends":
            for i in value:
                for key, value in i.items():
                    for i in value: 
                        friends_movie_list.append(i)
        if key == "watched":
            for i in value:
                my_movie_list.append(i)

    for movie in my_movie_list:
        if movie not in friends_movie_list:
            third_list.append(movie)

    return third_list


def get_friends_unique_watched(user_data):
    friends_movie_list = []
    my_movie_list = []
    third_list = []

    for key, value in user_data.items():
        if key == "watched":
            for i in value:
                my_movie_list.append(i)
        if key == "friends":
            for i in value:
                for key, value in i.items():
                    for i in value: 
                        friends_movie_list.append(i)

    for movie in friends_movie_list:
        if movie not in my_movie_list:
            if movie not in third_list:
                third_list.append(movie)

    return third_list
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
