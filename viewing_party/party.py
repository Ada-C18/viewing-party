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


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

