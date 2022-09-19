# ------------- WAVE 1 --------------------
# Create create_movie function that adds movies (title, genre, rating) to a dictionary
def create_movie(title, genre, rating):
    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating
    
    for category in movie_dict:
        if movie_dict[category] == None:
            return None
    
    print(movie_dict)
    return movie_dict

# Create add_to_watched function that adds movies that a user has watched to a dict
def add_to_watched(user_data, movie):
    watched_list = []
    watched_list.append(movie)
    user_data["watched"] = watched_list

    print(user_data)
    return user_data

# Create add_to_watchlist function that adds movies to a user's watchlist in a dict
def add_to_watchlist(user_data, movie):
    watchlist = []
    watchlist.append(movie)
    user_data["watchlist"] = watchlist

    print(user_data)
    return user_data

# Create watch_movie function that moves movies from watchlist to watched list
def watch_movie(user_data, movie_to_watch):
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == movie_to_watch:
            movie_watched = user_data["watchlist"][i]
            user_data["watched"].append(movie_watched)
            user_data["watchlist"].remove(movie_watched)
    
    print(user_data)
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# Create get_watched_avg_rating function to calculate average movie rating
def get_watched_avg_rating(user_data):
    total_watched_rating = 0
    for i in range(len(user_data["watched"])):
        total_watched_rating += user_data["watched"][i]["rating"]

    if user_data["watched"] == []:
        return 0.0
    else:
        avg_rating = total_watched_rating / len(user_data["watched"])
        return avg_rating

# Create get_most_watched_genre function to find the genre watched the most
def get_most_watched_genre(user_data):
    watched_genres = {}
    if user_data["watched"] == []:
        return None
    else:
        for i in range(len(user_data["watched"])):
            if user_data["watched"][i]["genre"] not in watched_genres:
                watched_genres[user_data["watched"][i]["genre"]] = 1
            else:
                watched_genres[user_data["watched"][i]["genre"]] += 1

    most_watched = max(watched_genres, key=watched_genres.get)
    return most_watched

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# Create get_unique_watched function
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

# Create get_friends_unique_watched function
def get_friends_unique_watched(user_data):
    friends_unique_watched_list = []
    full_list_of_friends_watched = []
    for i in range(len(user_data["friends"])):
        full_list_of_friends_watched += user_data["friends"][i]["watched"]
    
    for movie in full_list_of_friends_watched:
        if movie not in user_data["watched"]:
            friends_unique_watched_list.append(movie)
    return friends_unique_watched_list
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------