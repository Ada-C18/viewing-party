# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    """ 
    input: a str title, str genre, and float rating
    output: a dict of the given arguments if the inputs are valid OR None if the input is invalid
    """
    if title and genre and rating:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie
    else:
        return None

def add_to_watched(user_data, movie):
    """
    user_data: a dictionary with a key "watched" and a value list of dictionaries representing the movies the user watched
    movie: a dictionary in this format -
        {
            title": "Title A",
            "genre": "Horror",
            "rating": 3.5
        }
    """
    access_watched = user_data["watched"]
    access_watched.append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    """
    user_data: a dict with the key "watchlist" and value list of dictionaries representing the movies the user wants to watch
    movie: a dicitonary in this format:
        {
            title": "Title A",
            "genre": "Horror",
            "rating": 3.5
        }
    """
    access_watchlist = user_data["watchlist"]
    access_watchlist.append(movie)
    return user_data

def watch_movie(user_data, title):
    """
    user_data: a dict with keys "watchlist" and "watched"
    title: a str representing the title of the movie the user has watched
    """
    counter = 0
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            movie_watched = user_data["watchlist"].pop(counter)
            user_data["watched"].append(movie_watched)
            return user_data
        counter += 1
    else:
        return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
# part 1
def get_watched_avg_rating(user_data):
    """
    user_data: a dict with a "watched" list of movie dicts
    """
    num_movies_watched = len(user_data["watched"])
    all_ratings = 0.0

    if num_movies_watched == 0:
        return all_ratings
    else:
        for movie in user_data["watched"]:
            all_ratings += movie["rating"]
        average_rating = all_ratings / num_movies_watched
        return average_rating

# part 2
def get_most_watched_genre(user_data):
    """
    user_data: a dict with a "watched" list of movie dicts
    """
    # if watched list is empty:
        # return none
    # else:
        # iterate over the genres in watch list
        # return the most-watched genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

