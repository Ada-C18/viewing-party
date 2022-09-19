# ------------- WAVE 1 --------------------

from hashlib import new
from re import M

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(title, genre, rating):
    # for i in range(MOVIE_TITLE_1):
    new_movie = {}
    if title != None and genre != None and rating != None:
        new_movie = {
            "title": MOVIE_TITLE_1,
            "genre": GENRE_1,
            "rating": RATING_1
        }
        return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    updated_data = {"watched": {}}
    for finished_movie in movie:
        updated_data["watched"] = [
            {
                "title": movie["title"],
                "genre": movie["genre"],
                "rating": movie["rating"]
            }
        ]            
    return updated_data
    
def add_to_watchlist(user_data, movie):
    updated_data = {"watchlist": {}}
    for finished_movie in movie:
        updated_data["watchlist"] = [
            {
                "title": movie["title"],
                "genre": movie["genre"],
                "rating": movie["rating"]
            }
        ]            
    return updated_data

def watch_movie(janes_data, MOVIE_TITLE_1):
    updated_data = janes_data
    watched_movie = MOVIE_TITLE_1
    for i in range(len(updated_data["watchlist"])):
        if updated_data["watchlist"][i]["title"] == watched_movie:
            move_from_watchlist_to_watched = {
                    "title": updated_data["watchlist"][i].pop("title"),
                    "genre": updated_data["watchlist"][i].pop("genre"),
                    "rating": updated_data["watchlist"][i].pop("rating")
                }
            updated_data["watched"].append(move_from_watchlist_to_watched)
        else:
            continue
    updated_data["watchlist"] = list(filter(None, updated_data["watchlist"]))         
    return updated_data

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

