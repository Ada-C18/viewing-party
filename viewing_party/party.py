from collections import Counter

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    return {
        "title": title,
        "genre": genre,
        "rating": rating,
    }

def add_to_watched(user_data, movie):
    updated_data = user_data.copy()
    updated_data["watched"].append(movie)
    return updated_data

def add_to_watchlist(user_data, movie):
    updated_data = user_data.copy()
    updated_data["watchlist"].append(movie)
    return updated_data

def watch_movie(user_data, movie):
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
    watched = user_data["watched"]
    total = 0
    for movie in watched:
        total += movie["rating"]
    return (total / len(watched)) if len(watched) else 0

def get_most_watched_genre(user_data):
    genres = Counter([movie["genre"] for movie in user_data["watched"]])
    return genres.most_common(1)[0][0] if genres else None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
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
    friend_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friend_movies:
                friend_movies.append(movie)
    
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
    if not user_data["watched"]:
        return []
    most_watched = get_most_watched_genre(user_data)
    available_recs = get_available_recs(user_data)
    new_recs = filter(
        lambda movie: movie["genre"] == most_watched, 
        available_recs)
    return list(new_recs)

