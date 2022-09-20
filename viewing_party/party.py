# ------------- WAVE 1 --------------------

from re import I


def create_movie(title, genre, rating):
    new_movie = {}
    if title == None or genre == None or rating == None:
        return None
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating

    user_data = {
        "watched": [],
        "watchlist": [],
    }

    add_to_watched(user_data, new_movie)
    add_to_watchlist(user_data, new_movie)

    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie):
    for movie_dict in user_data["watchlist"]:
        if movie_dict["title"] == movie:
            user_data["watchlist"].remove(movie_dict)
            user_data["watched"].append(movie_dict)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_total = 0
    num_watched = 0
    if len(user_data["watched"]) == 0:
        avg_rating = 0
    else:
        for movie_dict in user_data["watched"]:
            for key, value in movie_dict.items():
                if key == "rating":
                    rating_total += value
                    num_watched += 1
        avg_rating = rating_total / num_watched
    return avg_rating

def get_most_watched_genre(user_data):
    genre_map = {}
    most_genre = None
    highest_num = None
    if len(user_data["watched"]) == 0:
        return most_genre
    for movie in user_data["watched"]:
        for key, value in movie.items():
            if key == "genre":
                if value not in genre_map:
                    genre_map[value] = 1
                else:
                    genre_map[value] += 1
    for genre, num in genre_map.items():
        if most_genre == None:
            most_genre = genre
            highest_num = num
        elif num > highest_num:
            most_genre = genre
            highest_num = num
        else:
            continue


    return most_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_movies = []
    friend_movies = get_friend_movie_lists(user_data)
    user_movies = get_user_movie_list(user_data)
    for movie_dict in user_movies:
        if movie_dict not in friend_movies:
            unique_movies.append(movie_dict)

    return unique_movies

def get_friends_unique_watched(user_data):
    unique_movies = []
    friend_movies = get_friend_movie_lists(user_data)
    user_movies = get_user_movie_list(user_data)
    for movie_dict in friend_movies:
        if movie_dict not in user_movies:
            unique_movies.append(movie_dict)

    return unique_movies

def get_user_movie_list(user_data):
    user_movies = []
    for movie_dict in user_data["watched"]:
        if movie_dict not in user_movies:
            user_movies.append(movie_dict)
    return user_movies

def get_friend_movie_lists(user_data):
    friend_movies = []
    for friend in user_data["friends"]:
        for movie_dict in friend["watched"]:
            if movie_dict not in friend_movies:
                friend_movies.append(movie_dict)
    return friend_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    all_available_recs = get_friends_unique_watched(user_data)
    user_subscriptions = get_user_subscription(user_data)
    recs_by_subscription = []
    for subscription in user_subscriptions:
        for movie_dict in all_available_recs:
            if subscription in movie_dict["host"]:
                recs_by_subscription.append(movie_dict)
    return recs_by_subscription

def get_user_subscription(user_data):
    subs = []
    if "subscriptions" in user_data:
        for subscription in user_data["subscriptions"]:
            subs.append(subscription)
    return subs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    fav_genre_recs = []
    fav_genre = most_frequent_genre(user_data)

    if fav_genre is None:
        return fav_genre_recs

    available_recs_by_subs = get_available_recs(user_data)

    for movie_dict in available_recs_by_subs:
        if movie_dict["genre"] == fav_genre:
            fav_genre_recs.append(movie_dict)
        else:
            continue

    return fav_genre_recs

def most_frequent_genre(user_data):
    genre_count = {}
    user_movie_list = get_user_movie_list(user_data)
    if len(user_movie_list) == 0:
        return None
    for movie_dict in user_movie_list:
        for key, value in movie_dict.items():
            if key == "genre":
                if value not in genre_count:
                    genre_count[value] = 1
                else:
                    genre_count[value] += 1

    fav_genre = str(max(genre_count, key =genre_count.get))

    return fav_genre

def get_rec_from_favorites(user_data):
    fav_movie_rec_list = []
    user_fav_movies = get_user_fav_list(user_data)
    friend_movies = get_friend_movie_lists(user_data)

    for movie_dict in user_fav_movies:
        if movie_dict not in friend_movies:
            fav_movie_rec_list.append(movie_dict)

    return fav_movie_rec_list


def get_user_fav_list(user_data):
    user_fav_movies = []
    for movie_dict in user_data["favorites"]:
        if movie_dict not in user_fav_movies:
            user_fav_movies.append(movie_dict)
    return user_fav_movies