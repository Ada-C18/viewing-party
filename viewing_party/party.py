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
    # watched_list = user_data["watched"]
    # while movie not in watched_list:
    #     watched_list.append(movie)
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    # watchlist = add_to_watchlist(user_data, movie)
    watchlist = user_data["watchlist"]
    # watched_list = add_to_watchlist(user_data, movie)
    watched_list = user_data["watched"]

    for movie in watchlist:
        if movie["title"] == title:
            movie_list = watchlist.pop()
            watched_list.append(movie_list)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
from statistics import mean

def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    # watchlist = user_data["watchlist"]
    rating_list = []
    num_movie = len(watched_list)
    if num_movie == 0:
        return 0
    for movie in watched_list:
        # for rating in movie["rating"]:
            rating_list.append(movie["rating"])
    # return rating_list
    return mean(rating_list)

def get_most_watched_genre(user_data):
    watched_list = user_data["watched"]
    genre_list = []
    
    while len(watched_list) > 0:
        for movie in watched_list:
            genre_list.append(movie["genre"])
        return max(set(genre_list), key = genre_list.count)

    return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    watched_list = user_data["watched"]
    friends_list = user_data["friends"]
    # print(watched_list)
    friends_watched = []
    for friends_dict in friends_list:
        for friends_key, friends_value in friends_dict.items():
            if friends_key == "watched" and friends_value not in friends_watched:
                friends_watched.extend(friends_value)

    unique_watched = []
    for movie in watched_list:
        if movie not in friends_watched and movie not in unique_watched:
            unique_watched.append(movie)
    # if unique_watched:
    return unique_watched
    # return None

def get_friends_unique_watched(user_data):
    watched_list = user_data["watched"]
    friends_list = user_data["friends"]
    # print(f'watched_list:{watched_list}/')

    friends_watched = []
    for friends_dict in friends_list:
        for friends_key, friends_value in friends_dict.items():
            if friends_key == "watched" and friends_value not in friends_watched:
                friends_watched.extend(friends_value)
    # print(f'friends_watched:{friends_watched}/')

    friends_unique = []
    for movie in friends_watched:
        if movie not in watched_list and movie not in friends_unique:
            friends_unique.append(movie)
    # if friends_unique:
    return friends_unique
    # return None

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    subs_list = user_data["subscriptions"]
    # print(sub_list)
    friends_watched = get_friends_unique_watched(user_data)
    rec_movie = []
    for movie in friends_watched:
        if movie["host"] in subs_list and movie not in rec_movie:
            rec_movie.append(movie)
    return rec_movie

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    most_genre = get_most_watched_genre(user_data)
    friends_watched = get_friends_unique_watched(user_data)
    new_rec_by_genre = []
    for movie in friends_watched:
        if movie["genre"] == most_genre and movie not in new_rec_by_genre:
            new_rec_by_genre.append(movie)
    return new_rec_by_genre

def get_rec_from_favorites(user_data):
    friends_watched = []
    for friends_dict in user_data["friends"]:
        for friends_key, friends_value in friends_dict.items():
            if friends_key == "watched" and friends_value not in friends_watched:
                friends_watched.extend(friends_value)
    
    rec_from_favorites = []
    for movie in user_data["favorites"]:
        if movie not in friends_watched and movie not in rec_from_favorites:
            rec_from_favorites.append(movie)
    return rec_from_favorites
