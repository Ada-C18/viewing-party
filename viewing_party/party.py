# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    else:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data


def watch_movie(user_data, movie_title):
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    for movie in watchlist:
        if movie["title"] == movie_title:
            watchlist.remove(movie)
            watched.append(movie)

    return user_data

    # -----------------------------------------
    # ------------- WAVE 2 --------------------
    # -----------------------------------------


def get_watched_avg_rating(user_data):
    ratings_list = []
    watched = user_data["watched"]

    if len(watched) > 0:
        for i in range(len(watched)):
            ratings_list.append(watched[i]["rating"])
    else:
        return 0

    ratings_sum = 0
    for rating in ratings_list:
        ratings_sum += rating

    return ratings_sum/len(ratings_list)


def get_most_watched_genre(user_data):
    counts = {}
    watched = user_data["watched"]

    if len(watched) > 0:
        for i in range(len(watched)):
            genre = watched[i]["genre"]
            counts[genre] = counts.get(genre, 0) + 1
    else:
        return None

    return max(counts, key=counts.get)

    # -----------------------------------------
    # ------------- WAVE 3 --------------------
    # -----------------------------------------

# *******


def get_unique_watched(user_data):
    watched_list = user_data["watched"]
    friends_watched_list = []
    unique_list = []

    for dict in user_data["friends"]:
        for item in dict["watched"]:
            friends_watched_list.append(item)

    for movie in watched_list:
        if movie not in friends_watched_list:
            unique_list.append(movie)

    return unique_list


def get_friends_unique_watched(user_data):
    watched_list = user_data["watched"]
    friends_watched_list = []
    unique_list = []

    for dict in user_data["friends"]:
        for item in dict["watched"]:
            friends_watched_list.append(item)

    for movie in friends_watched_list:
        if movie not in watched_list and movie not in unique_list:
            unique_list.append(movie)

    return unique_list

    # -----------------------------------------
    # ------------- WAVE 4 --------------------
    # -----------------------------------------


def get_available_recs(user_data):
    potential_recs_list = get_friends_unique_watched(user_data)
    recs_list = []

    for i in range(len(potential_recs_list)):
        for sub in user_data["subscriptions"]:
            if sub == potential_recs_list[i]["host"]:
                recs_list.append(potential_recs_list[i])

    return recs_list

    # -----------------------------------------
    # ------------- WAVE 5 --------------------
    # -----------------------------------------


def get_new_rec_by_genre(user_data):
    potential_recs_list = get_friends_unique_watched(user_data)
    genre_count = {}
    recs_by_genre = []
    friends_watched_list = []

# ******
    for dict in user_data["friends"]:
        for item in dict["watched"]:
            friends_watched_list.append(item)

    if len(user_data["watched"]) > 0 and len(friends_watched_list) > 0:
        for i in range(len(user_data["watched"])):
            genre = user_data["watched"][i]["genre"]
            genre_count[genre] = genre_count.get(genre, 0) + 1

        most_frequent_genre = max(genre_count, key=genre_count.get)

        for j in range(len(potential_recs_list)):
            if potential_recs_list[j]["genre"] == most_frequent_genre:
                recs_by_genre.append(potential_recs_list[j])

    return recs_by_genre


def get_rec_from_favorites(user_data):
    friends_watched_list = []
    favorite_recs = []

    for dict in user_data["friends"]:
        for item in dict["watched"]:
            friends_watched_list.append(item)

    for movie in user_data["favorites"]:
        if movie not in friends_watched_list:
            favorite_recs.append(movie)

    return favorite_recs
