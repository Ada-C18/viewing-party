# ------------- WAVE 1 --------------------

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(title, genre, rating):
    new_movie = {"title": [], "genre": [], "rating": []}

    new_movie["title"] = MOVIE_TITLE_1
    new_movie["genre"] = GENRE_1
    new_movie["rating"] = RATING_1

    if title and genre and rating:
        return new_movie
    else: 
        return None

    
def add_to_watched(user_data, movie):
    user_data = {"watched": []}
    
    movie = {
        "title": MOVIE_TITLE_1,
        "genre": GENRE_1,
        "rating": RATING_1
    }

    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {"watchlist": []}
    movie = {
    "title": MOVIE_TITLE_1,
    "genre": GENRE_1,
    "rating": RATING_1
    }
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    
    # user_data = {
    #     "watchlist": [{
    #     "title": MOVIE_TITLE_1,
    #     "genre": GENRE_1,
    #     "rating": RATING_1
    #     }],
    #     "watched": []
    #     }

    user_data = {
        "watchlist": [{"title": MOVIE_TITLE_1}],
        "watched": []
        }

    watched_list = []
    
    for key, value in user_data.items():
        if key == "watchlist":
            for i in value:
                for key, value in i.items():
                    if value == title:
                        watched_list.append(title)
                        user_data["watched"] = watched_list
                        user_data["watchlist"].remove(i)
        else:
            return user_data
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

