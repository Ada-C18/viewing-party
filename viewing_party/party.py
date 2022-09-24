# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not (title and genre and rating):
        return None
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
    sum = 0.0
    len_arr = len(user_data["watched"])

    if len_arr == 0:
        return sum

    for movie in user_data["watched"]:
        sum += movie["rating"]

    return sum/len_arr


def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None

    genre_count = {}

    for movie in user_data["watched"]:
        genre = movie["genre"]
        genre_count[genre] = genre_count.get(genre, 0) + 1

    max_count = max(genre_count.values())

    for k, v in genre_count.items():
        if v == max_count:
            return k

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# USER_DATA_3["friends"] =  [
#         {
#             "watched": [
#                 FANTASY_1,
#                 FANTASY_3,
#                 FANTASY_4,
#                 HORROR_1,
#             ]
#         },
#         {
#             "watched": [
#                 FANTASY_1,
#                 ACTION_1,
#                 INTRIGUE_1,
#                 INTRIGUE_3,
#             ]
#         }
#     ]


def get_unique_watched(user_data):

    unique = list(user_data["watched"])
    friends = list(user_data["friends"])

    for friend_dict in friends:
        for movie in friend_dict["watched"]:
            if movie in unique:
                unique.remove(movie)

    return unique


def get_friends_unique_watched(user_data):

    unique = []
    friends = user_data["friends"]

    for friend_dict in friends:
        for movie in friend_dict["watched"]:
            if (movie not in user_data["watched"]
                    and movie not in unique):
                unique.append(movie)

    return unique
    # -----------------------------------------
    # ------------- WAVE 4 --------------------
    # -----------------------------------------


def get_available_recs(user_data):
    subscriptions = user_data["subscriptions"]
    friends = user_data["friends"]
    recs = []

    for friend_dict in friends:
        for movie in friend_dict["watched"]:
            if (movie not in user_data["watched"]
                and movie not in recs
                    and movie["host"] in subscriptions):
                recs.append(movie)

    return recs

    # -----------------------------------------
    # ------------- WAVE 5 --------------------
    # -----------------------------------------


def get_new_rec_by_genre(user_data):
    friends = user_data["friends"]
    recs = []
    fav_genre = get_most_watched_genre(user_data)

    for friend_dict in friends:
        for movie in friend_dict["watched"]:
            if (movie not in user_data["watched"]
                and movie not in recs
                    and movie["genre"] == fav_genre):
                recs.append(movie)

    return recs


def get_rec_from_favorites(user_data):
    # I wonder what is the most efficient way to do this
    #
    # 1. create dictionary of user favorites; go thru friends and mark movies that have
    #   been watched and return unmarked keys as a list?

    # 2. copy favorites as a list and remove from list
    #   as we iterate thru friends' watched?

    # i think removing from a list is expensive to do in a loop
    #   but it's easier to code
    #   so i will do that

    recs = list(user_data["favorites"])
    friends = user_data["friends"]

    for friend_dict in friends:
        for movie in friend_dict["watched"]:
            if movie in recs:
                recs.remove(movie)

    return recs
