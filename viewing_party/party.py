# ------------- WAVE 1 --------------------



def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    movie = {"title": title, "genre": genre, "rating": rating}
    return movie

def add_to_watched(user_data, movie):
    if not "watched" in user_data:
        user_data["watched"] = []
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    if not "watchlist" in user_data:
        user_data["watchlist"] = []
    user_data["watchlist"].append(movie)
    return user_data
    
def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    length = len(user_data["watched"])
    if length < 1:
        return 0.0
    sum_rating = 0.0
    if "watched" in user_data and length > 0:
        for movie in user_data["watched"]:
            sum_rating += movie["rating"]
        avg_rating = sum_rating/length
    return avg_rating


def get_most_watched_genre(user_data):
    if len(user_data["watched"]) < 1:
        return None
    counter = {}
    res = None
    for movie in user_data["watched"]:
        if not movie["genre"] in counter:
            counter[movie["genre"]] = 1
        else:
            counter[movie["genre"]] += 1
    max_count = 0
    for k, v in counter.items():
        if v > max_count:
            res = k
            max_count = v
    return res



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    res = []
    friends_movie_set = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movie_set.add(movie["title"])
    for movie in user_data["watched"]:
        if not movie["title"] in friends_movie_set:
            res.append(movie)
    return res

def get_friends_unique_watched(user_data):
    res = []
    watched_moive_set = set()
    for movie in user_data["watched"]:
        watched_moive_set.add(movie["title"])
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if not movie["title"] in watched_moive_set and not movie in res:
                res.append(movie)
    return res


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movie = []
    friends_movies = get_friends_unique_watched(user_data)
    for movie in friends_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movie.append(movie)
    return recommended_movie



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    recommended_movie2 = []
    friends_movies = get_friends_unique_watched(user_data)
    most_freq_movie_genre = get_most_watched_genre(user_data)
    for movie in friends_movies:
        if movie["genre"] == most_freq_movie_genre:
            recommended_movie2.append(movie)
    return recommended_movie2

def get_rec_from_favorites(user_data):
    movies_from_favorites_rec = []
    fav_movie = user_data["favorites"]
    friends_movie_set = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movie_set.add(movie["title"])
    for movie in fav_movie:
        if not movie["title"] in friends_movie_set:
            movies_from_favorites_rec.append(movie)
    return movies_from_favorites_rec