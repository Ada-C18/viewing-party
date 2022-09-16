# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
    return (
        {"title": title, "genre": genre, "rating": rating}
        if title and genre and rating
        else None
    )


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def get_movie_from_watchlist(user_data, movie_title):
    return next((m for m in user_data["watchlist"] if m["title"] == movie_title), None)


def watch_movie(user_data, movie_title):
    movie = get_movie_from_watchlist(user_data, movie_title)
    if movie:
        user_data["watchlist"].remove(movie)
        return add_to_watched(user_data, movie)
    else:
        return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):
    ratings = [movie["rating"] for movie in user_data["watched"]]
    average = sum(ratings) / len(ratings) if ratings else 0
    return average


def get_most_watched_genre(user_data):
    genres = [movie["genre"] for movie in user_data["watched"]]
    most_watched = max(set(genres), key=genres.count) if genres else None
    return most_watched


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    friends_watched_titles = [
        movie["title"] for friend in user_data["friends"] for movie in friend["watched"]
    ]
    unique_watched = [
        movie
        for movie in user_data["watched"]
        if movie["title"] not in friends_watched_titles
    ]
    return unique_watched


def get_friends_unique_watched(user_data):
    watched_titles = set([movie["title"] for movie in user_data["watched"]])
    friends_watched_movies = dict()
    for friend in user_data["friends"]:
        friends_watched_movies.update(
            {movie["title"]: movie for movie in friend["watched"]}
        )
    friends_unique_watched = [
        movie
        for title, movie in friends_watched_movies.items()
        if title not in watched_titles
    ]
    return friends_unique_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):
    return [
        movie
        for movie in get_friends_unique_watched(user_data)
        if movie["host"] in user_data["subscriptions"]
    ]


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    new_rec_by_genre = [
        movie
        for movie in get_friends_unique_watched(user_data)
        if movie["genre"] is get_most_watched_genre(user_data)
    ]
    return new_rec_by_genre


def get_rec_from_favorites(user_data):
    favorite_titles = [movie["title"] for movie in user_data["favorites"]]
    rec_from_favorites = [
        movie
        for movie in get_unique_watched(user_data)
        if movie["title"] in favorite_titles
    ]
    return rec_from_favorites
