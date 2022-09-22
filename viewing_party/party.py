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
        return 0
    else:
        for i in range(len(user_data["watched"])):
            sum_of_ratings += user_data["watched"][i]["rating"]
        average_rating = sum_of_ratings/len(user_data["watched"])
    return average_rating  

def get_most_watched_genre(user_data):
    genre_list = []
    genre_counter = {}
    if not user_data["watched"]:
        return None
    else:
        for i in range(len(user_data["watched"])):
            genre_list.append(user_data["watched"][i]["genre"])
        for genre in genre_list:
            if genre not in genre_counter:
                genre_counter[genre] = 1
            elif genre in genre_counter:
                genre_counter[genre] += 1
        max_value = max(genre_counter.values())
        for key, value in genre_counter.items():
            if max_value == value:
                return key
    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_watched_list = user_data["watched"]
    user_unique_movies = []
    friend_watched_list = []

    for friend in user_data['friends']:
        for movie in friend['watched']:
            friend_watched_list.append(movie)

    for watched_movie in user_watched_list:
        if watched_movie not in friend_watched_list:
            user_unique_movies.append(watched_movie)
    return user_unique_movies

def get_friends_unique_watched(user_data):
    user_watched_list = user_data["watched"]
    friend_unique_movies = []

    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie not in user_watched_list and movie not in friend_unique_movies:
                friend_unique_movies.append(movie)

    return friend_unique_movies
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recs = []
    movies_from_friends = get_friends_unique_watched(user_data)
    for i in range(len(movies_from_friends)):
        if (movies_from_friends[i]['host']) in user_data['subscriptions']:
            recs.append(movies_from_friends[i])
    return recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    user_most_frequent_genre = get_most_watched_genre(user_data)
    recs = []
    friend_has_watched = get_friends_unique_watched(user_data)
    for i in range(len(friend_has_watched)):
        if friend_has_watched[i]["genre"] == user_most_frequent_genre:
            recs.append(friend_has_watched[i])
    return recs

def get_rec_from_favorites(user_data):
    user_fav_movies = []
    friend_watched_list = []
    recs = []

    for movie in user_data["favorites"]:
        user_fav_movies.append(movie)

    for friend_movie in user_data['friends']:
        for movie in friend_movie['watched']:
            friend_watched_list.append(movie)

    for fav_movie in user_fav_movies:
        if fav_movie not in friend_watched_list:
            recs.append(fav_movie)
    return recs

