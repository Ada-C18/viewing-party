# ------------- WAVE 1 --------------------
#added a comment to test commit
from tests.test_constants import MOVIE_TITLE_1


def create_movie(title, genre, rating):
    new_movie = {}
    if not title  or not genre or not rating:
        return None
    else:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    return new_movie

def add_to_watched(user_data, movie):
    user_data  = {"watched": [movie]}
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

