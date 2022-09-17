# ------------- WAVE 1 --------------------

import re
from shutil import move
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
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# def add_to_watched(user_data, movie):
    # user_data = {"watched" : }
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------