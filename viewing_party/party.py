# ------------- WAVE 1 --------------------
#added a comment to test commit

from tests.test_constants import MOVIE_TITLE_1


def create_movie(title, genre, rating):
    """
    Returns dictionary with three key-value pairs: "title", "genre"
    and "rating" as keys and parameters as values accordingly 
    or None if parameters are falsy.
    """
    
    if not title or not genre or not rating:
        return None
    new_movie = {"title": title, "genre": genre, "rating": rating}  
    return new_movie

def add_to_watched(user_data, movie):
    """
    Takes dictionary user_data with key "watched" 
    and adds dictionary movie to the watched list.
    Returns the user_data.
    """
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    """
    Takes dictionary user_data with key "watchlist"
    and adds dictionary movie to the watchlist.
    Returns the user_data.
    """
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    """
    Takes dictionary user_data with key "watchlist" and key "watched",
    and the title of the watched movie.
    Moves a movie from watchlist to watched if the title is in the user's watchlist.
    Returns the user_data.
    """
   
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    """
    Takes dictionary user_data with key "watched" and calculates
    the average rating of all movies in the watched list.
    Returns the average rating ors 0.0 if empty watched list.
    """
    watched_list = user_data["watched"]
    average_rating = 0.0
    rating_sum = 0
    
    if not watched_list:
        return average_rating
    
    for movie in user_data["watched"]:
            rating_sum += movie["rating"]
    average_rating = rating_sum / len(watched_list)
    return average_rating    
    

def get_most_watched_genre(user_data):
    """
    Takes dictionary user_data with key "watched" and determines which genre
    is most frequently watched.
    Returns the genre that is the most frequently watched or None if "watched" 
    is an empty list.
    """
    watched_list = user_data["watched"]
    if not watched_list:
        return None

    watched_genre_dict = {}
    for movie in watched_list:
        genre_name = movie["genre"]
        watched_genre_dict[genre_name] = watched_genre_dict.setdefault(genre_name, 0) + 1
   
    most_watched_genre = max(watched_genre_dict, key = watched_genre_dict.get)
    return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# create helper function to get unique movies for all friends
def get_all_friends_unique_watched_list(user_data):
    """
    Returns list of unique watched movies for all friends.
    """
    friends_unique_watched_list = []
    friends_list = user_data["friends"]
   
    for friend in friends_list:
        for movie in friend["watched"]:
            if movie not in friends_unique_watched_list:
                friends_unique_watched_list.append(movie) 
    return friends_unique_watched_list  


def get_unique_watched(user_data): 
    """
    Returns list of the movies (dict) the user has watched, but none of their friends have watched.
    """
    user_unique_list = []
    all_friends_unique_list = get_all_friends_unique_watched_list(user_data)

    for movie in user_data["watched"]:
        if movie not in all_friends_unique_list:
            user_unique_list.append(movie) 
    return user_unique_list  

# create function to get list of movies at least one of the user's friends
# have watched, but the user has not watched.
def get_friends_unique_watched(user_data):
    """
    Returns list of the movies (dict) that added to it only if at least one of the user's friends
    have watched, but the user has not watched.
    """
    friends_unique_list = []
    all_friends_unique_list = get_all_friends_unique_watched_list(user_data)

    for movie in all_friends_unique_list:
        if movie not in user_data["watched"]:
            friends_unique_list.append(movie)  
    return friends_unique_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):
    """
    Returns list of the movies (dict) that added to it only if: user has not watched it, 
    at least one of the user's friends has watched, and the "host"
    of the movie is a service that is in the user's "subscriptions".
    """
    recommended_movies = []
    user_has_not_watched_movies = get_friends_unique_watched(user_data)
    for movie in user_has_not_watched_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    """
    Returns list of the movies (dict) that added to it only if: user has not watched it, 
    at least one of the user's friends has watched, 
    and the "genre" of the movie is the same as the user's most watched genre.
    """
    recommended_movies_by_genre = []
    most_popular_wached_genre = get_most_watched_genre(user_data)
    user_has_not_watched_movies = get_friends_unique_watched(user_data)
    
    # loop though list of movies which the user has not watched;
    # add a movie to the recommended if the "genre" of the movie is the same 
    # as the user's most watched genre
    for movie in user_has_not_watched_movies:
        if most_popular_wached_genre == movie["genre"]:
                recommended_movies_by_genre.append(movie)
    
    return recommended_movies_by_genre
    

def get_rec_from_favorites(user_data):
    """
    Returns list of the movies (dict) that added to it only if: 
    the movie is in the user's "favorites" and None of the user's friends have watched it.
    """
    recommended_from_favorites_movies = []
    all_friends_unique_list = get_all_friends_unique_watched_list(user_data)
    
    # loop though list of the user's favorite movies;
    # add a movie to the recommended from favorites if none of the user's friends have watched it
    for user_favorite_movie in user_data["favorites"]:
        if user_favorite_movie not in all_friends_unique_list:
            recommended_from_favorites_movies.append(user_favorite_movie)
    return recommended_from_favorites_movies


