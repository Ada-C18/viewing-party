# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """
    Create and return a movie entry.
        Args:
            title (str): The movie title.
            genre (str): The movie genre.
            rating (float): The movie rating. 
        Returns: 
            movie (dict): A dict of the movie information.
    """
    if (title is None) or (genre is None) or (rating is None):
        return None
    else:
        movie = {'title': title, 'genre': genre, 'rating': rating}
        return movie


def add_to_watched(user_data, movie):
    """Add a movie to the users 'watched' list."""
    user_data["watched"] += [movie]
    return user_data


def add_to_watchlist(user_data, movie):
    """Add a movie to the users 'to watch' list."""
    user_data["watchlist"] += [movie]
    return user_data


def watch_movie(user_data, title):
    """Move a movie from the users watchlist to the users watched list."""
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data = add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
        
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    """
    Return the average rating of all movies in the watched list.
        Args:
            user_data (dict): A dict of movies the user has watched.
        Returns:
            average (float): The average movie rating.
    """
    if len(user_data["watched"]) == 0:
        return 0.0
    else:
        ratings_total = 0
        ratings_count = 0
        for movie in user_data["watched"]:
            ratings_total += movie["rating"]
            ratings_count +=1

        average_rating = ratings_total / ratings_count
        return average_rating


def get_most_watched_genre(user_data):
    """
    Return the most watched genre in the users watched list.
        Args:
            user_data (dict): A dict of movies the user has watched.
        Returns:
            most_watched_genre (string): The users most watched genre.
    """
    if len(user_data["watched"]) == 0:
        return None
    else:
        genre_count = {}
        for movie in user_data["watched"]:
            if movie["genre"] in genre_count:
                genre_count[movie["genre"]] += 1
            else:
                genre_count[movie["genre"]] = 1

        most_watched_genre = max(genre_count, key=genre_count.get)
        return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    """
    Return the movies the user has watched but none of their friends have watched.
        Args:
            user_data (dict): A dict of movies the user has watched and 
            their friends have watched. 
        Returns:
            user_unique_watched (list): Movies only the user has watched.
    """
    user_unique_watched = user_data["watched"].copy()

    for friend in user_data["friends"]:
        for user_movie in user_data["watched"]:
            if user_movie in friend["watched"] and (
            user_movie in user_unique_watched):
                user_unique_watched.remove(user_movie)

    return user_unique_watched


def get_friends_unique_watched(user_data):
    """
    Return the movies at least one of the user's friends have watched but the
    user has not watched.
        Args:
            user_data (dict): A dict of movies the user has watched and 
            their friends have watched. 
        Returns:
            friend_unique_watched (list): Movies only the users friends 
            have watched.
    """
    friends_unique_watched = []

    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if friend_movie not in user_data["watched"] and (
            friend_movie not in friends_unique_watched):
                friends_unique_watched.append(friend_movie)
    
    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    """
    Return a list of recommended movies for the user based on their subscriptions.
        Args:
            user_data (dict): A dict of the users watched movies and subscriptions,
            and their friends' watched movies.
        Returns:
            recommended_movies (list): Movies only the user friends have watched
            and that are available in the users subscriptions.
    """
    recommended_movies = []

    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if friend_movie not in user_data["watched"] and (
            friend_movie["host"] in user_data["subscriptions"]):
                    recommended_movies.append(friend_movie)

    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    """
    Return a list of recommended movies for the user based on genre.
        Args:
            user_data (dict): A dict of the users watched movies, subscriptions,
            and favorites, and their friends' watched movies.
        Returns:
            recommended_movies (list): Movies of the users most watched genre
            that the user hasn't watched.
    """
    recommended_movies = []
    user_favorite_genre = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)

    for movie in friends_unique_watched:
        if movie["genre"] == user_favorite_genre:
            recommended_movies.append(movie)

    return recommended_movies


def get_rec_from_favorites(user_data):
    """
    Return a list of recommended movies based on the users favorites.
        Args:
            user_data (dict): A dict of the users watched movies, subscriptions,
            and favorites, and their friends' watched movies.
        Returns:
            recommended_movies (list): Movies in the users favorites that their
            friends haven't watched.
    """
    recommended_movies = []
    
    user_unique_watched = get_unique_watched(user_data)
    for movie in user_unique_watched:
        if movie in user_data["favorites"]:
            recommended_movies.append(movie)
    
    return recommended_movies