# ------------- WAVE 1 --------------------
# Create create_movie function that adds movies (title, genre, rating) to a dictionary
def create_movie(title, genre, rating):
    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating
    
    for category in movie_dict:
        if not movie_dict[category]:
            return None
    
    # print(movie_dict)
    return movie_dict

# Create add_to_watched function that adds movies that a user has watched to a dict
def add_to_watched(user_data, movie):
    watched_list = []
    watched_list.append(movie)
    user_data["watched"] = watched_list

    # print(user_data)
    return user_data

# Create add_to_watchlist function that adds movies to a user's watchlist in a dict
def add_to_watchlist(user_data, movie):
    watchlist = []
    watchlist.append(movie)
    user_data["watchlist"] = watchlist

    # print(user_data)
    return user_data

# Create watch_movie function that moves movies from watchlist to watched list
def watch_movie(user_data, movie_to_watch):
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_to_watch:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    
    # print(user_data)
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# Create get_watched_avg_rating function to calculate average movie rating
def get_watched_avg_rating(user_data):
    total_watched_rating = 0
    for movie in user_data["watched"]:
        total_watched_rating += movie["rating"]

    if not user_data["watched"]:
        return 0.0
    else:
        avg_rating = total_watched_rating / len(user_data["watched"])
        return avg_rating

# Create get_most_watched_genre function to find the genre watched the most
def get_most_watched_genre(user_data):
    watched_genres = {}
    if not user_data["watched"]:
        return None
    else:
        for movie in user_data["watched"]:
            if movie["genre"] not in watched_genres:
                watched_genres[movie["genre"]] = 1
            else:
                watched_genres[movie["genre"]] += 1

    most_watched = max(watched_genres, key=watched_genres.get)
    return most_watched

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# Create get_friends_watched helper function to get a list of movies that friends have watched
def get_friends_watched(user_data):
    friends_watched_list = []
    for friends_movies in user_data["friends"]:
        friends_watched_list += friends_movies["watched"]
    
    return friends_watched_list

# Create get_unique_watched function to get list of movies user watched, but not friends
def get_unique_watched(user_data):
    unique_watched_list = []
    # Empty full_list_of_friends_watched list to add the movies that friends have watched to make one list
    full_list_of_friends_watched = []
    for i in range(len(user_data["friends"])):
        full_list_of_friends_watched += user_data["friends"][i]["watched"]
    
    # Compare user's "watched" list with full_list_of_friends_watched list 
    for movie in user_data["watched"]:
        if movie not in full_list_of_friends_watched:
            unique_watched_list.append(movie)
    return unique_watched_list

# Create get_friends_unique_watched function to get list of movies friends watched, but not user
def get_friends_unique_watched(user_data):
    friends_unique_watched_list = []
    full_list_of_friends_watched = []
    for i in range(len(user_data["friends"])):
        full_list_of_friends_watched += user_data["friends"][i]["watched"]
    
    for movie in full_list_of_friends_watched:
        if movie not in user_data["watched"] and movie not in friends_unique_watched_list:
            friends_unique_watched_list.append(movie)
    return friends_unique_watched_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# Create get_available_recs function to get list of movies user hasn't watched and has appropriate subscription
def get_available_recs(user_data):
    # Call get_friends_unique_watched function to get list of unique movies friends have watched
    list_of_friends_unique_watched = get_friends_unique_watched(user_data)
    # Empty recommended movies list
    recommended_movies = []
    for subscription in user_data["subscriptions"]:
        for i in range(len(list_of_friends_unique_watched)):
            if subscription == list_of_friends_unique_watched[i]["host"]:
                recommended_movies.append(list_of_friends_unique_watched[i])
    
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# Create get_new_rec_by_genre function to get a list of recommended movies with the genre of the user's most frequent genre
def get_new_rec_by_genre(user_data):
    # Get user's more frequently watched genre
    genre = get_most_watched_genre(user_data)
    # Call get_friends_unique_watched function to get list of unique movies friends have watched
    list_of_friends_unique_watched = get_friends_unique_watched(user_data)
    rec_movies_by_genre = []
    for i in range(len(list_of_friends_unique_watched)):
        if genre == list_of_friends_unique_watched[i]["genre"]:
            rec_movies_by_genre.append(list_of_friends_unique_watched[i])
    return rec_movies_by_genre

# Create get_rec_from_favorites function to get a list of user's favorite movies that friends have not watched
def get_rec_from_favorites(user_data):
    # Get list of movies user has watched, but friends haven't
    unique_watched_list = get_unique_watched(user_data)
    rec_movies_from_favorites = []

    for movie in user_data["favorites"]:        
        for watched_movie in unique_watched_list:
            if movie["title"] == watched_movie["title"]:
                rec_movies_from_favorites.append(watched_movie)

    return rec_movies_from_favorites