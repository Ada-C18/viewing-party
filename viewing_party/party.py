# ------------- WAVE 1 --------------------

## WAVE 1.01: validating input

def valid_title(title):
    if isinstance(title, str) and len(title) > 0:
        return True
    else:
        return False 

def valid_genre(genre):
    if isinstance(genre, str) and len(genre) > 0:
        return True
    else:
        return False 

def valid_rating(rating):
    # is there a range? 
    if isinstance(rating, float):
        return True
    else:
        return False 



def create_movie(title, genre, rating):
    """create_movie(title, genre, rating) returns a a dict when given:
    title: string, not empty
    genre: string, not empty
    rating: float?"""

    # validate input
    if valid_title(title) and valid_genre(genre) and valid_rating(rating):

        # model our movies as dictionary objects with title, genre, 
        # and rating fields 
        new_movie = {'title': title, 'genre': genre, 'rating': rating}
        return new_movie 

    else:
        return None 

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

