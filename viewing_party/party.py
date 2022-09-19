from statistics import mean

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    while title and genre and rating:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict

    return None

def add_to_watched(user_data, movie):
    # user_data ={
    #     "watched" : [{movie}]
    # }

    # movie = {
    #     "title" :
    #     "genre" :
    #     "rating":
    # }
    watched_list = user_data["watched"]
    while movie not in watched_list:
        watched_list.append(movie)

    return user_data

def add_to_watchlist(user_data, movie):

    watched_list = user_data["watchlist"]
    watched_list.append(movie)

    return user_data

def watch_movie(user_data, title):
    # watchlist = add_to_watchlist(user_data, movie)
    watchlist = user_data["watchlist"]
    # watched_list = add_to_watchlist(user_data, movie)
    watched_list = user_data["watched"]

    title_list = []
    for movie in watchlist:
        title_list.append(movie["title"])

    while title in title_list:
        # print(title_list)
        watchlist.remove(title)
        watched_list.append(title)

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
# from statistics import mean

def get_watched_avg_rating(user_data):
    # average_rating = 0.0
    rating_list = []
    for movie in user_data.values():
        rating_list.append(movie["rating"])
    return mean(rating_list)

def get_most_watched_genre(user_data):
    while len(user_data["watched"]) > 0:
        genre_list = []
        for movie in user_data.values():
            genre_list.append(movie["genre"])
        return max(set(genre_list), key = genre_list.count)

    return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_watchlist = []
    for movie in user_data["watched"]:
        while movie not in user_data["friends"]:
            unique_watchlist.append(movie)

    return unique_watchlist

def get_friends_unique_watched(user_data):
    friend_unique = []
    for movie in user_data["friends"]:
        while movie not in user_data["watched"]:
            friend_unique.append(movie)

    return friend_unique


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    rec_movie = []
    for movie in user_data["friends"]:
        while movie not in user_data["watched"]:
            if movie["host"] in user_data["subscriptions"]:
                rec_movie.append(movie["host"])
    return rec_movie


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    available_recs = get_available_recs(user_data)
    most_genre = get_most_watched_genre(user_data)
    new_rec_by_genre = []
    for movie in available_recs:
        while movie["genre"] == most_genre:
            new_rec_by_genre.append(movie)
    return new_rec_by_genre

def get_rec_from_favorites(user_data):
    rec_from_favorites = []
    for movie in user_data["favorites"]:
        while movie not in user_data["friends"]:
            rec_from_favorites.append(movie)
    return rec_from_favorites
