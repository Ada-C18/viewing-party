# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movies = {}
    if None in [title, genre, rating]: 
        return None
    movies["title"] = title
    movies["genre"] = genre
    movies["rating"] = rating
    return movies

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"] #[{}]
    watched = user_data["watched"] #[{}]
    for i in range(0, len(watchlist)):
        if title == watchlist[i]["title"]:
            watched.append(watchlist[i])
            watchlist.remove(watchlist[i])
    user_data["watchlist"] = watchlist
    user_data["watched"] = watched
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    ratings = []
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
    if len(ratings) >= 1:
        avg_ratings = sum(ratings)/len(ratings)
        return avg_ratings
    return 0.0

def get_most_watched_genre(user_data):
    genres = []
    genre_most_count = 0
    most_common_genre = None

    for movie in user_data["watched"]:
        genres.append(movie["genre"])
        for genre in genres:
            if genres.count(genre) > genre_most_count:
                genre_most_count = genres.count(genre)
                most_common_genre = genre    
    
    return most_common_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_watched = []
    friends_watched = []
    
    for view_status, movie_list in user_data.items():
        if view_status == "watched":
            for movie in movie_list:
                user_watched.append(movie["title"])
    for friend_view_status in user_data["friends"]:
        for movie in friend_view_status["watched"]:
            friends_watched.append(movie["title"])
    
    if len(user_watched) == 0:
        return user_watched

    user_watched_set = set(user_watched)
    friends_watched_set = set(friends_watched)

    unique_user_watched_set = user_watched_set - friends_watched_set
    unique_user_watched_list = list(unique_user_watched_set)

    unique_user_watched = []
    for movie in user_data["watched"]:
        if movie["title"] in unique_user_watched_list:
            unique_user_watched.append(movie)

    return unique_user_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

