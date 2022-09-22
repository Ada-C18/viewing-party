# ------------- WAVE 1 --------------------
def create_movie(title: str, genre: str, rating: float):
    """ Create a movie dictionary utilizing the arguments and return it.
    If one of the arguments is Falsy, instead return None.

    Keyword arguments:
    title -- a string movie title
    genre -- a string genre name
    rating -- a float value
    """
    if title and genre and rating:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie
    else:
        return None

def add_to_watched(user_data: dict, movie: dict):
    """ Add a movie dictionary to the "watched" key in user_data.
    Return user_data.

    Keyword arguments:
    user_data -- a dictionary with a "watched" key with a list value
    movie -- a dictionary with movie info
    """
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data: dict, movie: dict):
    """ Add a movie dictionary to the "watchlist" key in user_data.
    Return user_data.

    Keyword arguments:
    user_data -- a dictionary with a "watchlist" key with a list value
    movie -- a diictionary with movie info
    """
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data: dict, title: str):
    """ Move a movie in user_data from "watchlist" to "watched".
    Return user_data.

    Keyword arguments:
    user_data -- a dictionary with "watchlist" and "watched" keys
    title -- the title of the movie being moved
    """
    counter = 0
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            movie_watched = user_data["watchlist"].pop(counter)
            user_data["watched"].append(movie_watched)
            return user_data
        counter += 1
    else:
        return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data: dict):
    """ Return the average rating for "watched" movies in user_data.
    
    Keyword arguments:
    user_data -- a dictionary with a "watched" key with a list value
    """
    num_movies_watched = len(user_data["watched"])
    all_ratings = 0.0

    if num_movies_watched == 0:
        return all_ratings
    else:
        for movie in user_data["watched"]:
            all_ratings += movie["rating"]
        average_rating = all_ratings / num_movies_watched
        return average_rating

def get_most_watched_genre(user_data: dict):
    """ Return the most-watched genre in user_data.
    
    Keyword arguments:
    user_data -- a dictionary with a "watched" key with a list value
    """
    all_genres = {}
    most_watched_genre = None

    if len(user_data["watched"]) == 0:
        return most_watched_genre
    else:
        for movie in user_data["watched"]:
            if movie["genre"] in all_genres:
                all_genres[movie["genre"]] += 1
            else:
                all_genres[movie["genre"]] = 1
        most_watched_genre = max(all_genres, key=all_genres.get)
        return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data: dict):
    """Return a list of movies uniquely watched by the user.

    Keyword arguments:
    user_data -- A dictionary with "watched" and "friends" keys.      
    """
    friend_movies = get_friend_watched(user_data)

    unique_movies = [movie for movie in user_data["watched"]
                     if movie not in friend_movies]
    return unique_movies

def get_friends_unique_watched(user_data):
    """
    user_data = dict w/ two keys:
        "watched": list of movie dicts
        "friends": list of dicts, within which:
            "watched": list of movie dicts
                ^ these all contain a "title"
    """
    unique_watched_movies = []
    friend_watched_titles_only = []
    all_friend_watched = []
    unique_movie_titles = set()
    user_watched_list = [movie["title"] for movie in user_data["watched"]]

    for friends_list in user_data["friends"]:
        for movie in friends_list["watched"]:
            friend_watched_titles_only.append(movie["title"])
            all_friend_watched.append(movie)

    user_watched_set = set(user_watched_list)
    friend_watched_set = set(friend_watched_titles_only)
    unique_watched_set = friend_watched_set - user_watched_set

    for movie in all_friend_watched:
        if movie["title"] in unique_watched_set:
            if movie["title"] not in unique_movie_titles:
                unique_watched_movies.append(movie)
                unique_movie_titles.add(movie["title"])

    return unique_watched_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data: dict):
    """ Return a list of recommended movies based on user_data.
    Will only return movies available on user's streaming subscriptions.

    Keyword arguments:
    user_data -- a dictionary with "subscriptions" and "friends" keys
    """
    recommended_movies = []
    friend_recommendations = get_friends_unique_watched(user_data)
    
    for movie in friend_recommendations:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data: dict):
    """ Return a list of recommended movies based on user_data.
    Will select movies that match user's most frequently watched genre.

    Keyword arguments:
    user_data -- a dictionary with "friends" and "watched" keys
    """
    fave_genre = get_most_watched_genre(user_data)
    friend_recs = get_friends_unique_watched(user_data)
    genre_recs = []

    for movie in friend_recs:
        if movie["genre"] == fave_genre:
            genre_recs.append(movie)
    return genre_recs

def get_rec_from_favorites(user_data: dict):
    """ Return a list of user's movie recommendations.
    Will select user's favorite movies that friends haven't watched.

    Keyword arguments:
    user_data -- a dictionary with "favorites" and "friends" keys
    """
    recs = []
    friend_watched = get_friend_watched(user_data)

    for movie in user_data["favorites"]:
        if movie not in recs and movie not in friend_watched:
            recs.append(movie)
    return recs

# -----------------------------------------
# ----------- HELPER FUNCTIONS ------------
# -----------------------------------------
def get_friend_watched(user_data: dict):
    """ Return a list of all friends' watched movies from user_data.

    Keyword arguments:
    user_data -- A dictionary with a "friends" key with a list value. 
        Each item in the list is a dictionary with a "watched" key.
    """
    friend_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched.append(movie)
    return friend_watched