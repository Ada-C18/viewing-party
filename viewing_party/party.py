# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    if not title or not genre or not rating:
        return None
    else:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if (user_data["watchlist"][i]["title"]) == title:
            watched_movie = (user_data["watchlist"].pop(i))
            user_data["watched"].append(watched_movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum_of_ratings = 0
    if not user_data["watched"]:
        return 0.0
    else:
        for movie in user_data["watched"]:
            sum_of_ratings += movie["rating"]
        average_rating = sum_of_ratings/len(user_data["watched"])
    return average_rating

def get_most_watched_genre(user_data):
    genre_counter = {}
    if not user_data["watched"]:
        return None
    else:
        for movie in user_data["watched"]:
            if movie["genre"] not in genre_counter:
                genre_counter[movie["genre"]] = 1
            elif movie["genre"] in genre_counter:
                genre_counter[movie["genre"]] += 1
        most_frequent_genre = max(genre_counter, key=genre_counter.get)
        return most_frequent_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friend_watched_list = []
    user_unique_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched_list.append(movie)

    for watched_movie in user_data["watched"]:
        if watched_movie not in friend_watched_list:
            user_unique_movies.append(watched_movie)
            
    return user_unique_movies

def get_friends_unique_watched(user_data):
    friend_unique_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in friend_unique_movies:
                friend_unique_movies.append(movie)

    return friend_unique_movies
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recs = []
    movies_from_friends = get_friends_unique_watched(user_data)

    for movie in movies_from_friends:
        if movie["host"] in user_data["subscriptions"]:
            recs.append(movie)
    return recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recs = []
    user_most_frequent_genre = get_most_watched_genre(user_data)
    friend_has_watched = get_friends_unique_watched(user_data)

    for movie in friend_has_watched:
        if movie["genre"] == user_most_frequent_genre:
            recs.append(movie)
    return recs

def get_rec_from_favorites(user_data):
    recs = []
    friend_watched_list = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched_list.append(movie)

    for fav_movie in user_data["favorites"]:
        if fav_movie not in friend_watched_list:
            recs.append(fav_movie)
    return recs

