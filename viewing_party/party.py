# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    if title and genre and rating:
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
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    # watchlist = user_data["watchlist"]
    # watched = user_data["watched"]

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
        return user_data




# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    list_of_ratings = []
    for movie in user_data["watched"]:
        list_of_ratings.append(movie["rating"])
    if len(user_data["watched"]) == 0:
        avg_rating = 0
    else:
        avg_rating = sum(list_of_ratings)/len(list_of_ratings)
    return avg_rating

def get_most_watched_genre(user_data):
    genre_list = []
    for movie in user_data["watched"]:
        genre_list.append(movie["genre"])

    if user_data["watched"] == []:
        return None
    else:
        counter = 0
        for genre in genre_list:
            frequency = genre_list.count(genre)
            if frequency > counter:
                counter = frequency
                most_watched_genre = genre
            return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_watched = []
    friends_movies = set()
    users_movies = set()
    # We want to access "friends"
    # and for every friend in there, we want to 
    # access a movie in their "watched" list of
    # movie dictionaries.
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.add(movie["title"])
    for movie in user_data["watched"]:
        users_movies.add(movie["title"])
    unique_movies = users_movies - friends_movies
    for movie in user_data["watched"]:
        if movie["title"] in unique_movies:
            unique_watched.append(movie)
    return unique_watched

def get_friends_unique_watched(user_data):
    unique_watched = []
    friends_movies = set()
    users_movies = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.add(movie["title"])
    for movie in user_data["watched"]:
        users_movies.add(movie["title"])
    unique_movies = friends_movies - users_movies
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in unique_movies:
                if movie not in unique_watched:
                    unique_watched.append(movie)
    return unique_watched 
    

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies = []
    host_list = user_data["subscriptions"]
    unique_watched = get_friends_unique_watched(user_data)
    for movie in unique_watched:
        if movie["host"] in host_list:
            recommended_movies.append(movie)
    return recommended_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    recs_by_genre = []
    fav_genre = get_most_watched_genre(user_data)
    recommended = get_friends_unique_watched(user_data)
    for movie in recommended:
        if movie["genre"] == fav_genre:
            recs_by_genre.append(movie)
    return recs_by_genre

def get_rec_from_favorites(user_data):
    unique_recs = get_unique_watched(user_data)
    recs_from_favs = []
    
    for movie in unique_recs:
        if movie in user_data["favorites"]:
            recs_from_favs.append(movie)
    return recs_from_favs

    