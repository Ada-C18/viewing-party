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
    try:
        return next(m for m in user_data["watchlist"] if m["title"] == movie_title)
    except:
        return None


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
    return sum(ratings) / len(ratings) if len(ratings) else 0


def get_most_watched_genre(user_data):
    genres = [movie["genre"] for movie in user_data["watched"]]
    return max(set(genres), key=genres.count) if genres else None


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
