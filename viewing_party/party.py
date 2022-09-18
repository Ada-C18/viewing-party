# ------------- WAVE 1 --------------------

# Instantiate movie as dictionary if all fields are populated
def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {
            "title" : title,
            "genre" : genre,
            "rating" : rating,
        }
        return movie

# User_data set up as dictonary with the key watched corresponding to a list of movie dictionaries
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

#Watchlist key added as a list of dictionaries within the user_data dictionary
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


# function to remove a movie from the watchlist and add it to the watched list
def watch_movie(user_data, movie_title):

    # remove movie from watchlist 
    for movie in user_data["watchlist"]:
        if movie_title in movie["title"]:
            user_data["watchlist"].remove(movie)
            
    # Add movie to watched (inside of if so that if the movie was not in the watchlist, it will do nothing)
            user_data["watched"].append(movie)
    
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

