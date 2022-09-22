# ------------- WAVE 1 --------------------




def create_movie(title, genre, rating):
    movie = None
    if title == None or genre == None or rating == None:
        movie == None
    else:
        movie = {
            "title" : title,
            "genre" : genre,
            "rating" : rating
        }
    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title in movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum = 0
    counter = 0
    average = 0.0
    for movie in user_data["watched"]:
        if movie["rating"] == False:
            average == 0.0
        else:
            sum += movie["rating"]
            counter += 1
            average = sum / counter
    return average

def get_most_watched_genre(user_data):
    genre_dict = {}
    for movie in user_data["watched"]:
        if movie["genre"] not in genre_dict:
            genre_dict[movie["genre"]] = 1
        elif movie["genre"] in genre_dict:
            genre_dict[movie]["genre"] += 1
        else:
            return None
    
        most_watched = max(genre_dict, key = genre_dict.get)
        return most_watched
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    friend_list = []
    user_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_list.append(movie["title"])       
    
    for movie in user_data["watched"]:
        user_list.append(movie["title"])
    
    unique_movie_list = set(user_list) - set(friend_list)
    movie_list = []
    for title in unique_movie_list:
        for movie in user_data["watched"]:
            if title in movie["title"]:
                movie_list.append(movie)
    
    return movie_list

def get_friends_unique_watched(user_data):
    friend_list = []
    user_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_list.append(movie["title"])       
    
    for movie in user_data["watched"]:
        user_list.append(movie["title"])
    
    unique_movie_list = set(friend_list) - set(user_list)
    movie_list = []
    for title in unique_movie_list:
        for friend in user_data["friends"]:
            for movie in friend["watched"]:
                if movie not in movie_list:               
                    if title in movie["title"]:
                        movie_list.append(movie)
    
    return movie_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    unwatched_movies = get_friends_unique_watched(user_data)
    movie_recs = []
    for movie in unwatched_movies:
        if movie["host"] in user_data["subscriptions"]:
            movie_recs.append(movie)
    return movie_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    unwatched_movies = get_friends_unique_watched(user_data)
    movie_recs = []
    for movie in unwatched_movies:
        if movie["genre"] == get_most_watched_genre(user_data):
            movie_recs.append(movie)
    return movie_recs
