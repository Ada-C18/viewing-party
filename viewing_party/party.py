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
    # since I'm calculating the average later, also check to make sure that 
    # 0 <= rating <= 5 (assumed)
    # for example, if someone enters a tomatometer rating (1-100), return 
    # None 
    if not isinstance(rating, float):
        return False
    elif rating < 0.0 or rating > 5.0:
        return False 
    else:
        return True



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

