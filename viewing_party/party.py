#I'm testing to see if I can pass my changes in!
#trying again!
# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    #create a dictionary with the keys 'title', 'genre', 'rating', and the values the values passed in
    if title and genre and rating:
        movie_dict = {}
        movie_dict['title'] = title
        movie_dict['genre'] = genre
        movie_dict['rating'] = rating
        return movie_dict

def add_to_watched(user_data, movie):
    #user_data is a dictionary with watched as one of the keys.
    #this function adds the movie_dict (listed here as movie) into a list stored as a value connected to watched.
    user_data['watched'].append(movie)
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

