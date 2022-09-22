# ------------- WAVE 1 --------------------


from audioop import avg
from codecs import unicode_escape_decode


def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    return movie


def add_to_watched(user_data, movie):
    # add the movie (a list of dict) to a key "watched" inside user_data
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    # add the movie (a list of dict) to a key "watchlist" inside user_data
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, movie_title):
    # checks to see if a movie title is in a user_data watchlist or watched
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)

    return user_data
# -----------------------------------------

# ------------- WAVE 2 --------------------


def get_watched_avg_rating(user_data):
    # initiate a total_rating to cal avg_rating
    total_rating = 0
    avg_rating = 0
    # iterate over the movie rating in the watched list
    for movie in user_data["watched"]:
        total_rating += movie["rating"]
        avg_rating = total_rating / len(user_data["watched"])
    return avg_rating


def get_most_watched_genre(user_data):
    # user_data_genre = []
    user_data_genre = {}
    most_watched_genre = None
    # again iterating of user_data["watched"] list of dict
    for movie in user_data["watched"]:
        watched_genre = movie["genre"]
        if watched_genre in user_data_genre:
            # user_data_genre.append(watched_genre)
            user_data_genre[watched_genre] += 1
        else:
            user_data_genre[watched_genre] = 0
        most_watched_genre = max(user_data_genre, key=user_data_genre.get)
    return most_watched_genre


# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------

def get_unique_watched(user_data):
    userFriend_watched_movie = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in userFriend_watched_movie:
                userFriend_watched_movie.append(movie)
        # getting unique movie for users ie checking to see if same movie exist in friends watched list
    unique_watched_movie = []
    for movie in user_data["watched"]:
        if movie not in userFriend_watched_movie and movie not in unique_watched_movie:
            unique_watched_movie.append(movie)
    return unique_watched_movie


def get_friends_unique_watched(user_data):
    friends_unique_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in friends_unique_watched:
                friends_unique_watched.append(movie)
    return friends_unique_watched


# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommendations = list()
    # getting movies that only firend watched
    friends_unique_watched = get_friends_unique_watched(user_data)
    for movie in friends_unique_watched:
        #     try:
        #         if movie["host"] in user_data["subscriptions"]:
        #             recommendations.append(movie)
        #     except KeyError:
        #         pass
        # return recommendations
        if "subscriptions" in user_data:
            if movie["host"] in user_data["subscriptions"]:
                recommendations.append(movie)
    return recommendations


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recomm_genre = []
    # getting  most watched genre using the helper func get_most_watched_genre()
    most_watched_genre = get_most_watched_genre(user_data)
    # call the get_available_ rec as a helper func to get possible_rec
    possible_recomm = get_available_recs(user_data)
    for movie in possible_recomm:
        # add movie if genre is equal to user's most watched genre and not yet recommended
        if movie["genre"] == most_watched_genre and movie["genre"] not in recomm_genre:
            recomm_genre.append(movie)
    return recomm_genre


def get_rec_from_favorites(user_data):
    recomm_fav = []
    # get user's  favorites movies
    user_fav = user_data["favorites"]
    # get only unqiue movies watched
    unique_watched_byuser = get_unique_watched(user_data)
    for movie in user_fav:
        if movie in unique_watched_byuser:
            recomm_fav.append(movie)
    return recomm_fav
