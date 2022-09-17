# ------------- WAVE 1 --------------------
TITLE_KEY = "title"
GENRE_KEY = "genre"
RATING_KEY = "rating"


def create_movie(title, genre, rating):

    new_movie = {
        TITLE_KEY: title,
        GENRE_KEY: genre,
        RATING_KEY: rating}

    if not new_movie[TITLE_KEY]:
        return None
    if not new_movie[GENRE_KEY]:
        return None
    if not new_movie[RATING_KEY]:
        return None

    return new_movie


def add_to_watched(user_data, movie):
    user_data = {"watched": [movie]}
    return user_data


def add_to_watchlist(user_data, movie):
    user_data = {"watchlist": [movie]}
    return user_data

# pop watchlist in list-dict-List title
# store in variable ,append to watched list


def watch_movie(user_data, title):
    if user_data["watchlist"]:
        for i in user_data['watchlist']:
            if i['title'] == title:
                user_data["watched"].append(i)
                user_data['watchlist'].remove(i)
                
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
