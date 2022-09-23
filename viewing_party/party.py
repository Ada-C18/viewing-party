# ------------- WAVE 1 --------------------

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(title, genre, rating):
    new_movie = {}
    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie
    
    return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie) 

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) == 0:
        
        return 0.0

    rating_average = 0
    for movie in user_data["watched"]:
        rating_average += movie["rating"]
    
    return rating_average / len(user_data.get("watched"))

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        
        return None

    popular_genre = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre not in popular_genre:
            popular_genre[genre] = 1
        else:
            popular_genre[genre] += 1

    genre_count = 0
    most_popular_genre = ""
    for genre, value in popular_genre.items():
        if value > genre_count:
            genre_count = value
            most_popular_genre = genre
    
    return most_popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friends_watched_list = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_list.append(movie)

    user_watched = user_data['watched']
    unique_watched_list = []

    for movie in user_watched:
        if movie not in friends_watched_list:
            unique_watched_list.append(movie)

    return unique_watched_list

def get_friends_unique_watched(user_data):
    friends_watched_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched_list:
                friends_watched_list.append(movie)

    user_watched_list = user_data["watched"]
    friends_unique_watched_list = []
    for movie in friends_watched_list:
        if movie not in user_watched_list:
            friends_unique_watched_list.append(movie)

    return friends_unique_watched_list
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommendations = []
    friends_unique_watched_list = get_friends_unique_watched(user_data)
    for movie in friends_unique_watched_list:
        if movie["host"] in user_data["subscriptions"]:
            recommendations.append(movie)

    return recommendations


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    friends_unique_watched = get_friends_unique_watched(user_data)
    most_popular_genre = get_most_watched_genre(user_data)
    recommendations = []
    for movie in friends_unique_watched:
        if most_popular_genre == movie["genre"]:
            recommendations.append(movie)

    return recommendations

def get_rec_from_favorites(user_data):
    friends_watched_list = []
    recommendations = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched_list.append(movie)

    recommendations = []
    for movie in user_data["favorites"]:
        if movie not in friends_watched_list:
            recommendations.append(movie)
    return recommendations
