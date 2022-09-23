# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {"title": title, "genre": genre, "rating": rating}
    if title is None or genre is None or rating is None:
        new_movie = None
    return new_movie

def add_to_watched(user_data, movie):
    # Intention here to make a new list, in case we needed the old list
    updated_data = user_data
    updated_data["watched"].append(movie)
    return updated_data 

def add_to_watchlist(user_data, movie):
    updated_data = user_data
    updated_data["watchlist"].append(movie)
    return updated_data 

def watch_movie(user_data, movie):
    for item in user_data["watchlist"]:
        if item["title"] == movie:
            watched_movie = item
            user_data["watched"].append(watched_movie)
            user_data["watchlist"].remove(watched_movie)
    updated_data = user_data
    return updated_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# works when I change to float, ask instructor why
def get_watched_avg_rating(user_data):
    number_of_movies = 0
    average_ratings = 0.0
    if len(user_data["watched"]) == 0:
        average_ratings = 0.0
        return average_ratings
    for movie in user_data["watched"]:
        number_of_movies += 1
        average_ratings += float(movie["rating"])
    average_ratings = average_ratings/number_of_movies
    return average_ratings
        
def get_most_watched_genre(user_data):
# to include multiple genres that have high count
    genre_dict = {}
    most_frequent_genre = ""
    if len(user_data["watched"]) == 0:
        return None
    for movie in user_data["watched"]:
        if movie["genre"] not in genre_dict:
            genre_dict[movie["genre"]] = 1
        elif movie["genre"] in genre_dict:
            genre_dict[movie["genre"]] += 1
    most_frequent_genre = [key for key, value in genre_dict.items()\
         if value == max(genre_dict.values())]
    return ' '.join(most_frequent_genre)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    # GOAL: return movies user has watched, but not their friends
    user_watched_movies = []
    friends_watched_movies = []
    unique_movies = []
    if len(user_data["watched"]) == 0:
        return unique_movies
    for movie in user_data["watched"]:
        user_watched_movies.append(movie)
    for friend in user_data["friends"]:
        for film in friend["watched"]:
            friends_watched_movies.append(film)
    for item in user_watched_movies:
        if item not in friends_watched_movies:
            unique_movies.append(item)

    return(unique_movies)

def get_friends_unique_watched(user_data):
    #Determine which movies at least one of the user's friends have watched, but the user has not watched.
    #Return a list of dictionaries, that represents a list of movies
    user_watched_movies = []
    friends_watched_movies = []
    unique_movies = []
    friends_unique = []
    if len(user_data["watched"]) == 0:
        unique_movies
    for movie in user_data["watched"]:
        user_watched_movies.append(movie)
    for friend in user_data["friends"]:
        for film in friend["watched"]:
            if film in friends_watched_movies:
                continue
            else:
                friends_watched_movies.append(film)
    for movie in friends_watched_movies:
        if movie not in user_watched_movies:
            friends_unique.append(movie)
    return friends_unique

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    movie_recs = []
    friends_watched_user_no = get_friends_unique_watched(user_data)
    for movie in friends_watched_user_no:
        if movie["host"] in user_data["subscriptions"]:
            movie_recs.append(movie)
    return movie_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    new_recs = []
    user_most_watched_genre = get_most_watched_genre(user_data)
    friends_watched_user_no = get_friends_unique_watched(user_data)
    for movie in friends_watched_user_no:
        if movie["genre"] == user_most_watched_genre:
            new_recs.append(movie)
    return new_recs

def get_rec_from_favorites(user_data):
    favorite_recs = []
    movies_user_watched_friends_no = get_unique_watched(user_data)
    for movie in movies_user_watched_friends_no:
        if movie in user_data["favorites"]:
            favorite_recs.append(movie)
    return favorite_recs



