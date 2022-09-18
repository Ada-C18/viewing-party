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
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    # watchlist = user_data["watchlist"] #[{}]
    # watched = user_data["watched"] #[{}]
    # for i in range(0, len(watchlist)):
    #     if title == watchlist[i]["title"]:
    #         watched.append(watchlist[i])
    #         watchlist.remove(watchlist[i])
    # user_data["watchlist"] = watchlist
    # user_data["watched"] = watched
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
    friends_data= user_data["friends"]
    friends_list = []
    user_list = []

    for movie in user_data["watched"]:
        user_list.append(movie["title"])
    for friend in friends_data:
        for movie in friend["watched"]:
            # if movie not in friends_list:
            friends_list.append(movie["title"])
    
    user_unique_titles = list(set(user_list) - set(friends_list))
    # user_unique_list = list(user_unique)
    user_unique_movies = []

    for movie in user_data["watched"]:
        if movie["title"] in user_unique_titles: 
            user_unique_movies.append(movie)
    
    return user_unique_movies

def get_friends_unique_watched(user_data):
    friends_data= user_data["friends"]
    friends_list = []
    user_list = []

    for movie in user_data["watched"]:
        user_list.append(movie["title"])
    for friend in friends_data:
        for movie in friend["watched"]:
            # if movie not in friends_list:
            friends_list.append(movie["title"])
    
    friends_unique_titles = list(set(friends_list) - set(user_list))
    # user_unique_list = list(user_unique)
    friends_unique_movies = []
    for friend in friends_data:
        for movie in friend["watched"]:
            if movie["title"] in friends_unique_titles:
                friends_unique_movies.append(movie)
                friends_unique_titles.remove(movie["title"]) #prevent appending repeat movies

    return friends_unique_movies
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    user_subscriptions = user_data["subscriptions"]
    friends_movies = get_friends_unique_watched(user_data)
    movie_recs = []
    # for index in range(len(friends_movies)):
    #     for movie in friends_movie
    for movie in friends_movies: 
        if movie["host"] in user_subscriptions:
            movie_recs.append(movie)
    
    return movie_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    movie_recs_by_genre = []
    friends_movies = get_friends_unique_watched(user_data)
    user_genre = get_most_watched_genre(user_data)
    for movie in friends_movies:
        if movie["genre"] == user_genre: 
            movie_recs_by_genre.append(movie)
    return movie_recs_by_genre


def get_rec_from_favorites(user_data):
    user_unique = get_unique_watched(user_data)
    rec_from_favorites = []
    for user_unique_movie in user_unique:
        for fav_movie in user_data["favorites"]:
            if user_unique_movie["title"] == fav_movie["title"]:
                rec_from_favorites.append(user_unique_movie)
    return rec_from_favorites