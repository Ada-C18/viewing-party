# ------------- WAVE 1 --------------------

from tests.test_constants import USER_DATA_2


def create_movie(title, genre, rating):
    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict ["rating"] = rating
    
    movie_info = [title,genre,rating]
    if None in movie_info:
        return None
    else:
        return movie_dict

def add_to_watched(user_data,movie):
    user_data = {}
    user_data["watched"] = [movie]

    return user_data

def add_to_watchlist(user_data,movie):
    user_data = {}
    user_data["watchlist"] = [movie]

    return user_data

def watch_movie(user_data,title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    watched_value = []
    avg = 0
    
    for key in user_data["watched"]:
        avg += 1
        watched_value.append(key["rating"])
    
    if avg == 0:
        return 0.0
    
    average = sum(watched_value) / len (watched_value)
    return average

def get_most_watched_genre(user_data):
    watched_genre = []
    for key in user_data["watched"]:
        watched_genre.append(key["genre"])
        return max(set(watched_genre), key = watched_genre.count)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    my_movies = []
    same_movies = []

    for movie in user_data["watched"]:
        for friend in user_data["friends"]:
            if movie in friend["watched"]:
                same_movies.append(movie)
            print(movie, same_movies)

    for movies in user_data["watched"]:
        if movies not in same_movies:
            my_movies.append(movies)
    return my_movies    
        
def get_friends_unique_watched(user_data):
    friends_unique_watched = []
    friends_movie_list = []
    user_movie_list = user_data["watched"]

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_movie_list:
                friends_movie_list.append(movie)

    for movie in friends_movie_list:
        if movie not in user_movie_list:
            friends_unique_watched.append(movie)
    return friends_unique_watched
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies =[]
    friends_watched = get_friends_unique_watched(user_data)
    
    for movie in friends_watched:
        if movie["host"] in user_data.get("subscriptions"):
            recommended_movies.append(movie)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    recommended_movies= []
    my_genre = get_most_watched_genre(user_data)
    friends_watched = get_friends_unique_watched(user_data)
    
    for movie in friends_watched:
        if my_genre == movie["genre"]:
            recommended_movies.append(movie)  
    return recommended_movies


def get_rec_from_favorites(user_data):
    recommended_movies = []
    friends_watched = get_unique_watched(user_data)

    for movie in user_data["favorites"]:
        if movie in friends_watched:
            recommended_movies.append(movie)
    return recommended_movies