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

def get_most_watched_genre(user_data):
    """
    user_data: a dict with a "watched" list of movie dicts
    """
    all_genres = {}
    most_watched_genre = None

    if len(user_data["watched"]) == 0:
        return most_watched_genre
    else:
        for movie in user_data["watched"]:
            if movie["genre"] in all_genres:
                all_genres[movie["genre"]] += 1
            else:
                all_genres[movie["genre"]] = 1
        most_watched_genre = max(all_genres, key=all_genres.get)
        return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
# part 1
def get_unique_watched(user_data):
    """
    user_data = dict w/ these keys:
        "watched" : list of movie dicts
        "friends": list of dicts, within which:
            "watched" : list of movie dicts
                ^ these all contain a "title"       
    """
    unique_watched_movies = []
    friend_watched_list = []
    user_watched_list = [movie["title"] for movie in user_data["watched"]]

    for friends_list in user_data["friends"]:
        for movie in friends_list["watched"]:
            friend_watched_list.append(movie["title"])

    user_watched_set = set(user_watched_list)
    friend_watched_set = set(friend_watched_list)
    unique_watched_set = user_watched_set - friend_watched_set
    
    for movie in user_data["watched"]:
        if movie["title"] in unique_watched_set:
            unique_watched_movies.append(movie)

    return unique_watched_movies

#part 2
def get_friends_unique_watched(user_data):
    """
    user_data = dict w/ two keys:
        "watched": list of movie dicts
        "friends": list of dicts, within which:
            "watched": list of movie dicts
                ^ these all contain a "title"
    """
    unique_watched_movies = []
    friend_watched_list = []
    user_watched_list = [movie["title"] for movie in user_data["watched"]]

    for friends_list in user_data["friends"]:
        for movie in friends_list["watched"]:
            friend_watched_list.append(movie["title"])

    user_watched_set = set(user_watched_list)
    friend_watched_set = set(friend_watched_list)
    unique_watched_set = friend_watched_set - user_watched_set
    
    for friends_list in user_data["friends"]:
        for movie in friends_list["watched"]:
            if movie["title"] in unique_watched_set:
                unique_watched_movies.append(movie)

    return unique_watched_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    """
    user_data contains:
    "subscriptions" = list of strings, representing streaming services user has access to
    "friends" = many friends w/ watched lists
        each movie in watched lists has a "host": streaming service
    """
    # create a list of recommended movies
    # add only movies that fit this critera:
        # not in user_data["watched"]
        # in at least 1 friend's "watched"
        # the movie's "host" is in "subscriptions"
    # return the recommended movie list
    

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
# part 1
def get_new_rec_by_genre(user_data):
    """
    consider the user's most frequently watched genre
    determine a list of movies, adding only if:
        movie not in user's "watched"
        movie in at least 1 friend's "watched"
        movie "genre" is same as user's most watched genre
    return the list of recommended movies
    """
    pass

# part 2
def get_rec_from_favorites(user_data):
    """
    user_data has "favorites"
    "favorites" is list of movie dicts representing user faves
    determine list of movies, adding only if:
        movie in user's "favorites"
        movie not in any friend's "watched"
    return the list of recommended movies
    """
    pass