from collections import Counter

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """Create a dictionary containing information about a movie."""
    if not title or not genre or not rating:
        return None
    return {
        "title": title,
        "genre": genre,
        "rating": rating,
    }

def add_to_watched(user_data, movie):
    """Add a movie to a user's watched list."""
    updated_data = user_data.copy()
    updated_data["watched"].append(movie)
    return updated_data

def add_to_watchlist(user_data, movie):
    """Add a movie to a user's watchlist."""
    updated_data = user_data.copy()
    updated_data["watchlist"].append(movie)
    return updated_data

def watch_movie(user_data, movie):
    """If a movie is in the user's watchlist, add it to watched."""
    updated_data = user_data.copy()
    watchlist = updated_data["watchlist"]
    watched = updated_data["watched"]
    watchlist_titles = {
        watch_item["title"]: watch_item 
        for watch_item in watchlist
    }
    if movie in watchlist_titles:
        movie_details = watchlist_titles[movie]
        watchlist.remove(movie_details)
        watched.append(movie_details)
    return updated_data
        

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    """Return the average rating of a user's watched movies. Return 0 if 
    watched is empty."""
    watched = user_data["watched"]
    total = 0
    for movie in watched:
        total += movie["rating"]
    return (total / len(watched)) if len(watched) else 0

def get_most_watched_genre(user_data):
    """Return the most watched genre in a user's watched list.""" 
    genres = Counter([movie["genre"] for movie in user_data["watched"]])
    return genres.most_common(1)[0][0] if genres else None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    """Return all the movies the user has watched that their friends have not 
    watched."""
    user_watched = {movie["title"]: movie for movie in user_data["watched"]}
    friends_watched = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.add(movie["title"])
    for title in friends_watched:
        if title in user_watched:
            user_watched.pop(title)
    return list(user_watched.values())

def get_friends_unique_watched(user_data):
    """Return all the movies that at least one of the user's friends has 
    watched but the user has not watched."""
    friends_watched = {}
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched[movie["title"]] = movie
    user_watched = {movie["title"] for movie in user_data["watched"]}
    for title in user_watched:
        if title in friends_watched:
            friends_watched.pop(title)
    return list(friends_watched.values())

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    """Return a list of movies that the user has not watched, that one of 
    their friends has watched, and that is available on a service they are 
    subscribed to."""
    # Build list of movies that friends have watched.
    friend_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friend_movies:
                friend_movies.append(movie)
    # Filter out movies not on a service the user is subscribed to.
    recommended_movies = []
    subscriptions = user_data["subscriptions"]
    watched = user_data["watched"]
    for movie in friend_movies:
        if movie not in watched and movie["host"] in subscriptions:
            recommended_movies.append(movie)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    """Return a list of recommended movies in the user's most watched genre."""
    if not user_data["watched"]:
        return []
    most_watched = get_most_watched_genre(user_data)
    available_recs = get_available_recs(user_data)
    new_recs = filter(
        lambda movie: movie["genre"] == most_watched, 
        available_recs
    )
    return list(new_recs)

def get_rec_from_favorites(user_data):
    """Return a list of movies that are in the user's favorites and that 
    haven't been watched by their friends."""
    # Get set of all movies that have been watched by friends.
    friends_watched = set()
    for friend in user_data["friends"]:
        titles = [movie["title"] for movie in friend["watched"]]
        friends_watched = friends_watched.union(titles)
    # Get list of user's favorite movies that have not been watched by their 
    # friends.
    recs = filter(
        lambda movie: movie["title"] not in friends_watched,
        user_data["favorites"]
    )
    return list(recs)
