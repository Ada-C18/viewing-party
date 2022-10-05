# ------------- WAVE 1 --------------------
from logging.config import dictConfig


def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    else:
        movie ={"title": title,
        "genre": genre,
        "rating": rating,

        }
    
    return movie

def add_to_watched(user_data, movie):
    user_data = {}
    user_data["watched"] = [movie]

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]

    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    for item in range(len(watchlist)):
        if watchlist[item]["title"] == title:
            user_data["watched"].append(watchlist[item])
            del watchlist[item]

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0
    num_of_ratings = 0
    watched_list = user_data["watched"]
    for dictionary in watched_list:
        sum += dictionary["rating"]
        num_of_ratings += 1
    if num_of_ratings == 0:
        return 0
    else:
        rating_avg = sum / num_of_ratings

    return rating_avg

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) < 1:
        return None
    genres = []
    for dictionary in user_data["watched"]:
        genres.append(dictionary["genre"])
    genre_set = set(genres)
    top_genre_dict = {genre : genres.count(genre) for genre in genre_set}
    counter = 0
    for value in top_genre_dict.values():
        if counter < value:
            counter = value
            top_genre = list(top_genre_dict.keys())[list(top_genre_dict.values()).index(counter)]
        
    return top_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_movie_list = user_data["watched"]
    friend_watched_list = user_data["friends"]
    user_unique_movies = []
    #------------------user data-------------------
    for dictionary in user_movie_list:
        if dictionary["title"] not in user_unique_movies:
            user_unique_movies.append(dictionary)
    
    #--------------friend watched items-------------
    for friends_dict in friend_watched_list:
        for watched_list in friends_dict:
            for dict in friends_dict[watched_list]:
                for dictionary in user_unique_movies:
                    if dictionary["title"] == dict["title"]:
                        user_unique_movies.remove(dictionary)

    return user_unique_movies

def get_friends_unique_watched(user_data):
    user_movie_list = user_data["watched"]
    friend_watched_list = user_data["friends"]
    friends_unique_movies = []

    for friends_dict in friend_watched_list:
        for dict in friends_dict["watched"]:
            if dict["title"] == None:
                return friends_unique_movies
            if dict not in friends_unique_movies:
                #### end up getting 4 instead of 3 movies in the final dictionary###
                friends_unique_movies.append(dict)

    for dictionary in user_movie_list:
        for dict in friends_unique_movies:
            if dictionary["title"] == dict["title"]:
                #########does not remove common titles between user & friend. Look into it######
                friends_unique_movies.remove(dict)

    return friends_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    subscribed = user_data["subscriptions"]
    not_seen_friends_watched_list = get_friends_unique_watched(user_data)
    recommendations = []
    for movie_dict in not_seen_friends_watched_list:
        if movie_dict["host"] in subscribed:
            recommendations.append(movie_dict)
    
    if recommendations == []:
        return recommendations

    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    user_movie_list = user_data["watched"]
    not_seen_friends_watched_list = get_friends_unique_watched(user_data)
    users_top_genre = get_most_watched_genre(user_data)
    recommendations = []

    for movie in not_seen_friends_watched_list:
        if movie["genre"] == users_top_genre and movie not in user_movie_list:
            recommendations.append(movie)
    if recommendations == []:
        return recommendations

    return recommendations

def get_rec_from_favorites(user_data):
    user_favorites = user_data['favorites']
    friend_watched_list = user_data["friends"]
    give_recommendation = []

    for movie in user_favorites:
        give_recommendation.append(movie)
    
    if friend_watched_list == []:
        return give_recommendation

    for friend in friend_watched_list:
        for movie in friend["watched"]:
            if movie in give_recommendation:
                give_recommendation.remove(movie)    

    return give_recommendation