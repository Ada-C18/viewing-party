# ------------- WAVE 1 --------------------

from statistics import StatisticsError, mode


def create_movie(title, genre, rating):
    if bool(title) == True and bool(genre) == True and bool(rating) == True:
        return {
            "title": title,
            "genre": genre,
            "rating": rating
            }
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist": [movie]
    }
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            watchlist.remove(movie)
            add_to_watched(user_data, movie)
    return user_data
    
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating (user_data):
    watched = user_data["watched"]
    total_rating = 0
    count = 0
    avg_rating = 0

    for movie in watched:
        count += 1
        total_rating += movie["rating"]
        if count > 1:
            avg_rating = total_rating/count
    return avg_rating

def get_most_watched_genre(user_data):
    genre_list = []
    try: 
        for movie in user_data["watched"]:
            genre_list.append(movie["genre"])
        popular_genre = mode(genre_list)
        return popular_genre
    except StatisticsError:
        return None


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_watched = []
    friends_watched = []
    unique_watched = []
    for movie in user_data["watched"]:
        user_watched.append(movie)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)
    for movie in user_watched:
        if movie not in friends_watched:
            unique_watched.append(movie)
    return unique_watched

def get_friends_unique_watched(user_data):
    user_watched = []
    friends_watched = []
    friends_unique_watched = []
    for movie in user_data["watched"]:
        user_watched.append(movie)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)
    for movie in friends_watched:
        if movie not in user_watched:
            if movie not in friends_unique_watched:
                friends_unique_watched.append(movie)
    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friends_unique_watched = get_friends_unique_watched(user_data)
    subscription = user_data["subscriptions"]
    recommend = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie in friends_unique_watched and movie["host"] in subscription:
                recommend.append(movie)
    return recommend
        
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
#
def get_new_rec_by_genre(user_data):
    recommend = []
    most_watched_genre = get_most_watched_genre(user_data)
    friends_watched = get_friends_unique_watched(user_data)
    for movie in friends_watched:
        if movie["genre"] == most_watched_genre:
            recommend.append(movie)
    return recommend

def get_rec_from_favorites(user_data):
    recommend = []
    favorites = user_data["favorites"]
    friends_watched = get_friends_unique_watched(user_data)
    for movie in favorites:
        if movie not in friends_watched:
            recommend.append(movie)
    return recommend

