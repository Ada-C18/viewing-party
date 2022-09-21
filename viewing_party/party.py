# ------------- WAVE 1 --------------------

from re import M


def create_movie(title, genre, rating):

    # return None if not filled out
    if title == None or genre == None or rating == None:
        return None

    # create movie dictionary
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    return movie

# add watched to list
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

# test adds move to user watchlist
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# moves movie from watchlist to empty watched
# def watch_movie(user_data, title):
#     watchlist= user_data["watchlist"]
#     for movie in range(len(watchlist)):
#         if watchlist[movie]["title"]== title:
#             user_data["watched"].append(watchlist[movie])
#             del watchlist[movie]
#     return user_data

def watch_movie(user_data, title):
    watchlist= user_data["watchlist"]
    for movie in watchlist:
        if movie["title"]== title:
            user_data["watched"].append(movie)
            watchlist.remove(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# calculates average rating
def get_watched_avg_rating(user_data):
    all_rating = []
    watched = user_data["watched"]
    for movie in watched:
        all_rating.append(movie["rating"])

# if rating list is empty return 0
    if len(all_rating) == 0:
        average_rating = 0.0
    else:
        average_rating = sum(all_rating) / (len(all_rating))
    return average_rating


# most viewed genre
def get_most_watched_genre(user_data):
    all_genre = []
    watched = user_data["watched"]
    for movie in watched:
        all_genre.append(movie["genre"])

# if genre list is empty return None
    if len(all_genre) == 0:
        most_watched_genre = None
    else:
        most_watched_genre = max(all_genre, key=all_genre.count)
    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
# create a dictionary that holds the movies of me and my friends
def make_movie_dict_for_me_and_friends(user_data):

    my_movie_titles_set = set()
    friend_movie_titles_set = set()

    watched = user_data["watched"]
    friends = user_data["friends"]

    for friend in friends:
        for movie in friend["watched"]:
                friend_movie_titles_set.add(movie["title"])
    for movie in watched:
        my_movie_titles_set.add(movie["title"])

    unique_movie_dict = {}
    unique_movie_dict["my_movie_titles"] = my_movie_titles_set
    unique_movie_dict["friend_movie_titles"] = friend_movie_titles_set
    return unique_movie_dict


# get unique watched by me
def get_unique_watched(user_data):

    unique_movie_dict = make_movie_dict_for_me_and_friends(user_data)

    unique_watched = unique_movie_dict["my_movie_titles"] - unique_movie_dict["friend_movie_titles"]
        
    unique_movie_list = []
    for uniquemovie in user_data["watched"]:
        if uniquemovie["title"] in unique_watched: 
            unique_movie_list.append(uniquemovie)
    return unique_movie_list


# make unique watched by friends
def get_friends_unique_watched(user_data):

    unique_movie_dict = make_movie_dict_for_me_and_friends(user_data)

    unique_watched = unique_movie_dict["friend_movie_titles"] - unique_movie_dict["my_movie_titles"]

    unique_movie_list = []
    for movie in user_data["friends"]:
        for title in movie["watched"]:
            if title["title"] in unique_watched and title not in unique_movie_list:
                unique_movie_list.append(title)
    return unique_movie_list
    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    movies_for_recs = get_friends_unique_watched(user_data)
    subscriptions_list = []
    for subscription in user_data["subscriptions"]:
        subscriptions_list.append(subscription)

    reccomended_movies = []
    for movie in movies_for_recs:
        if movie["host"] in subscriptions_list:
            reccomended_movies.append(movie)
    return reccomended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# Returns reccomended movies based on genre
def get_new_rec_by_genre(user_data):
    movies_for_rec = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)
    recommended_movies_by_genre = []

    for movie in movies_for_rec:
        if movie["genre"] == most_watched_genre:
            recommended_movies_by_genre.append(movie)
    return recommended_movies_by_genre

# Returns reccommended movies based on favorites
def get_rec_from_favorites(user_data):
    favorites = user_data["favorites"]
    if len(user_data["friends"]) > 0:
        friend_watched_1 = user_data["friends"][0]["watched"]
        friend_watched_2 = user_data["friends"][1]["watched"]
    recommended_movies_by_favorites = []

    for fav_movie in favorites:
        if len(user_data["friends"]) == 0:
            recommended_movies_by_favorites.append(fav_movie)
        elif fav_movie in favorites and fav_movie not in friend_watched_1 and fav_movie not in friend_watched_2:
            recommended_movies_by_favorites.append(fav_movie)
    return recommended_movies_by_favorites


