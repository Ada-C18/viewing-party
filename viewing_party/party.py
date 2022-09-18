# ------------- WAVE 1 --------------------

from multiprocessing.sharedctypes import Value

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(title, genre, rating):
    
    new_movie = {}
    if title and genre and rating:
        new_movie = {
            "title" : title,
            "genre" : genre,
            "rating" : rating
        }
        return new_movie
    return None

def add_to_watched(user_data, movie):
    user_data = {"watched" : [movie]}
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {"watchlist" :[movie]}
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    average_rating = 0 
    sum_list = []
    for i in user_data["watched"]:
        if i["rating"]:
            sum_list.append(i["rating"])
        average_rating = sum(sum_list)/len(user_data["watched"])
    return average_rating

    
def get_most_watched_genre(user_data):
    genre_list =[]
    for i in user_data["watched"]:
        if i["genre"]:
            genre_list.append(i["genre"])
            most_popular = max(set(genre_list), key = genre_list.count)
        return most_popular
    return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    friend_list_movie = []
    user_list_movie = []
    unique_list = []

    for dict in user_data["friends"]:
        for movie in dict["watched"]:
            friend_list_movie.append(movie)

    for movie in user_data["watched"]:
        user_list_movie.append(movie)

    for movie_dict in user_list_movie:
        if movie_dict not in friend_list_movie:
            unique_list.append(movie_dict)
    return unique_list


def get_friends_unique_watched(user_data):
    friend_list_movie =[]
    user_list_movie =[]
    friend_unique_list=[]


    for dict in user_data["friends"]:
        for movie in dict["watched"]:
            friend_list_movie.append(movie)

    for movie in user_data["watched"]:
        user_list_movie.append(movie)

    for movie_dict in friend_list_movie:
        if movie_dict not in user_list_movie:
            friend_unique_list.append(movie_dict)

    check_set = set()
    friend_no_duplicates = []
    for movie_dict in friend_unique_list:
        tuple_dict = tuple(sorted(movie_dict.items()))
        if tuple_dict not in check_set:
            check_set.add(tuple_dict)
            friend_no_duplicates.append(movie_dict)
    return friend_no_duplicates
            

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    movie_with_subscriptions =[]
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["host"] in user_data["subscriptions"] and movie not in user_data["watched"]:
                movie_with_subscriptions.append(movie)
    return movie_with_subscriptions


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

