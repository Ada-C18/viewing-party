def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {"title": title, "genre": genre, "rating": rating}
    else: 
        movie = None
    return movie

def add_to_watched(user_data, movie):
    user_data["watched"] = [movie]
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]
    return user_data

def watch_movie(user_data, movie_title):
    for movies in user_data["watchlist"]:
        if movies["title"] == movie_title:
            user_data["watched"].append(movies)
            user_data["watchlist"].remove(movies)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    ratings_list = []
    for movies in user_data["watched"]:
                ratings_list.append(movies["rating"])
    if ratings_list:
        rating_average = sum(ratings_list)/len(ratings_list)
    else:
        rating_average = 0.0
    return rating_average

def get_most_watched_genre(user_data):
    genres = []
    for movies in user_data["watched"]:
        genres.append(movies["genre"])
    if genres:
        most_watched_genre = max(genres, key = genres.count)
    else:
        most_watched_genre = None
    return most_watched_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_watched = []
    friends_watched = []
    for i in range(len(user_data["friends"])):
        for item in user_data["friends"][i]["watched"]:
            friends_watched.append(item)
    for movie in user_data["watched"]:
            if movie not in friends_watched:
                unique_watched.append(movie)
    return unique_watched

def get_friends_unique_watched(user_data):
    friends_watched = []
    friends_unique_watched = []
    for i in range(len(user_data["friends"])):
        for item in user_data["friends"][i]["watched"]:
            friends_watched.append(item)
    for movie in friends_watched:
        if (movie not in user_data["watched"] 
        and movie not in friends_unique_watched):
            friends_unique_watched.append(movie)
    
    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friends_unique_watched = get_friends_unique_watched(user_data)
    reccommendations = []
    for movie in friends_unique_watched:
        if movie["host"] in user_data["subscriptions"]:
            reccommendations.append(movie)
    print(reccommendations)
    return reccommendations
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    favorite_genre = get_most_watched_genre(user_data)
    friends_movies = get_friends_unique_watched(user_data)
    rec_list_by_genre = []
    if friends_movies:
        for movie in friends_movies:
            if movie["genre"] == favorite_genre:
                rec_list_by_genre.append(movie)
    else:
        return None
    return rec_list_by_genre

def get_rec_from_favorites(user_data):
    user_unique_movies = get_unique_watched(user_data)
    rec_list_from_favorites = []
    for movie in user_data["watched"]:
        if (movie in user_unique_movies 
        and movie in user_data["favorites"]):
            rec_list_from_favorites.append(movie)
    return rec_list_from_favorites