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


def get_unique_watched(user_data):
    friends_watched_titles = [
        movie["title"] for friend in user_data["friends"] for movie in friend["watched"]
    ]
    my_unique_watched = [
        movie
        for movie in user_data["watched"]
        if movie["title"] not in friends_watched_titles
    ]
    return my_unique_watched


def get_friends_unique_watched(user_data):
    my_watched_titles = set([movie["title"] for movie in user_data["watched"]])
    friends_unique_watched = dict()
    for friend in user_data["friends"]:
        friends_unique_watched.update(
            {
                movie["title"]: movie
                for movie in friend["watched"]
                if movie["title"] not in my_watched_titles
            }
        )
    return list(friends_unique_watched.values())


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
