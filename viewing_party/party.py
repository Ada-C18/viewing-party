# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    '''
    takes in a movie title, genre and rating
    returns dictionary with the keys "title", "genre", and "rating"
    with their respective values.
    '''
    movie = {}
    if None in [title, genre, rating]: 
        return None
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating
    return movie

def add_to_watched(user_data, movie):
    '''
    takes in user_data and movie
    returns updated user_data with movie added to watched
    '''
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    takes in user_data and movie,
    returns updated user_data with movie added to watchlist
    '''
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    '''
    takes user_data and title of a movie, 
    if movie in watchlist, will add movie to watched and remove from watchlist
    returns updated user_data
    '''
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    '''
    takes in user_data, returns average rating of movies in watched
    if no movies in watched, returns 0
    '''
    ratings = []
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
    if len(ratings) >= 1:
        avg_ratings = sum(ratings)/len(ratings)
        return avg_ratings
    return 0.0

def get_most_watched_genre(user_data):
    '''
    takes in user_data, returns the most common genre in watched
    '''
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
# # -----------------------------------------

def get_common_watched(user_data):
    '''
    takes in user_data
    returns the movies that both the user and friends have watched in a list
    '''
    friends_data = user_data["friends"]
    common_watched = []

    for movie in user_data["watched"]:
        for friend in friends_data:
            for friend_movie in friend["watched"]:
                if movie["title"] == friend_movie["title"]:
                    common_watched.append(movie)
    return common_watched

def get_unique_watched(user_data):
    '''
    takes in user_data, 
    returns a list of dictionaries for each movie that only the user has watched
    '''
    # friends data is a list of dictionaries with 
    # duplicate_watched = [title for movie in user_data["watched"] for title in movie]
    user_unique_watched = []
    common_watched = get_common_watched(user_data)

    for movie in user_data["watched"]:
        if movie not in common_watched and movie not in user_unique_watched:
            user_unique_watched.append(movie)

    return user_unique_watched

def get_friends_unique_watched(user_data):
    '''
    takes in user_data, 
    returns a list of dictionaries for each movie that only the friends have watched
    '''
    friends_data = user_data["friends"]
    common_watched = get_common_watched(user_data)
    friends_unique_watched = []
    
    for friend in friends_data:
        for movie in friend["watched"]:
            if movie not in common_watched and movie not in friends_unique_watched:
                friends_unique_watched.append(movie)
    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    '''
    takes in user_data, 
    returns a list of dictionaries for each movie that the 
    user has not watched from friends_unique_watched 
    and are hosted within users subscription
    '''
    user_subscriptions = user_data["subscriptions"]
    friends_movies = get_friends_unique_watched(user_data)
    movie_recs = []
    
    for movie in friends_movies: 
        if movie["host"] in user_subscriptions:
            movie_recs.append(movie)
    
    return movie_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    '''
    takes in user_data, 
    returns a list of dictionaries for each movie that the 
    user has not watched from friends_unique_watched 
    and have the same genre as the users most watched genre
    '''
    movie_recs_by_genre = []
    friends_movies = get_friends_unique_watched(user_data)
    user_genre = get_most_watched_genre(user_data)
    for movie in friends_movies:
        if movie["genre"] == user_genre: 
            movie_recs_by_genre.append(movie)
    return movie_recs_by_genre


def get_rec_from_favorites(user_data):
    '''
    takes in user_data, 
    returns a list of dictionaries for each recommended movies 
    if the movie is in the user's `"favorites"`
    and none of the user's friends have watched it
    '''
    user_unique = get_unique_watched(user_data)
    rec_from_favorites = []
    for user_unique_movie in user_unique:
        for fav_movie in user_data["favorites"]:
            if user_unique_movie["title"] == fav_movie["title"]:
                rec_from_favorites.append(user_unique_movie)
    return rec_from_favorites