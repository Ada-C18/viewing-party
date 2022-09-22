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
def get_watched_avg_rating(user_data):
    """
    user_data: a dict with a "watched" list of movie dicts
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

def get_most_watched_genre(user_data):
    """
    user_data: a dict with a "watched" list of movie dicts
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
def get_unique_watched(user_data):
    """
    user_data = dict w/ these keys:
        "watched" : list of movie dicts
        "friends": list of dicts, within which:
            "watched" : list of movie dicts
                ^ these all contain a "title"       
    """
    unique_watched_movies = []
    friend_watched_list = []
    user_watched_list = [movie["title"] for movie in user_data["watched"]]

    for friends_list in user_data["friends"]:
        for movie in friends_list["watched"]:
            friend_watched_list.append(movie["title"])

    user_watched_set = set(user_watched_list)
    friend_watched_set = set(friend_watched_list)
    unique_watched_set = user_watched_set - friend_watched_set
    
    for movie in user_data["watched"]:
        if movie["title"] in unique_watched_set:
            unique_watched_movies.append(movie)

    return unique_watched_movies

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
def get_available_recs(user_data):
    """
    user_data contains:
    "subscriptions" = list of strings, representing streaming services user has access to
    "friends" = many friends w/ watched lists
        each movie in watched lists has a "host": streaming service
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
def get_new_rec_by_genre(user_data):
    """
    consider the user's most frequently watched genre
    determine a list of movies, adding only if:
        movie not in user's "watched"
        movie in at least 1 friend's "watched"
        movie "genre" is same as user's most watched genre
    return the list of recommended movies
    """
    fave_genre = get_most_watched_genre(user_data)
    friend_recs = get_friends_unique_watched(user_data)
    genre_recs = []

    for movie in friend_recs:
        if movie["genre"] == fave_genre:
            genre_recs.append(movie)
    
    return genre_recs

def get_rec_from_favorites(user_data):
    """
    user_data has "favorites"
    "favorites" is list of movie dicts representing user faves
    determine list of movies, adding only if:
        movie in user's "favorites"
        movie not in any friend's "watched"
    return the list of recommended movies
    """
    rec_list = []
    friend_watched_list = []
    user_fave_list = [movie["title"] for movie in user_data["favorites"]]

    for friends_list in user_data["friends"]:
        for movie in friends_list["watched"]:
            friend_watched_list.append(movie["title"])
    
    user_fave_set = set(user_fave_list)
    friend_watched_set = set(friend_watched_list)
    user_fave_recs = user_fave_set - friend_watched_set

    for movie in user_data["favorites"]:
        if movie["title"] in user_fave_recs:
            rec_list.append(movie)

    return rec_list