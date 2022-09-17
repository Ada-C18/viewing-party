# ------------- WAVE 1 --------------------

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    new_movie = {
        "title": MOVIE_TITLE_1,
        "genre": GENRE_1,
        "rating": RATING_1
    }
    return new_movie

def add_to_watched(user_data, movie):
    for watched_list in user_data.values():
        watched_list.append(movie)

    updated_data = user_data
    return updated_data

def add_to_watchlist(user_data, movie):
    for watched_list in user_data.values():
        watched_list.append(movie)

    updated_data = user_data
    return updated_data

def watch_movie(janes_data, title):
    watched = {}
    for watchlist_list in janes_data.values():
        if not watchlist_list:
            pass
        else:
            for i in range(len(watchlist_list)):
                if watchlist_list[i]['title'] == title:
                    watched = watchlist_list.pop(i)
    if watched: 
        janes_data["watched"].append(watched)
    updated_data = janes_data
    return updated_data

# move movie to watch (title) to watched

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

