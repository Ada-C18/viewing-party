# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {"title":title, 
                    "genre": genre, 
                    "rating": rating
                    }
        return movie_dict
    else:
        return None
    
def add_to_watched(user_data, movie):    
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if title in user_data["watchlist"][i]["title"]:
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].remove(user_data["watchlist"][i])
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) > 0:
        sum_watched_rating = 0.0
        for i in range(len(user_data["watched"])):
            sum_watched_rating += user_data["watched"][i]["rating"]
        watched_avg_rating = sum_watched_rating / len(user_data["watched"])
    else:
        watched_avg_rating = 0.0
    return watched_avg_rating


def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    else:
        genre_list = []
        for i in range(len(user_data["watched"])):
            genre_list.append(user_data["watched"][i]["genre"])
        
        genre_dict = {}
        max_freq = 0

        for genre in genre_list:
            genre_dict[genre] = genre_dict.get(genre,0) + 1
            
            # Note: this will break if there are ties for genres. If there are ties, need to make a list to hold ties and have an elif statement
            if genre_dict[genre] > max_freq:
                max_freq = genre_dict[genre]
                most_common_genre = genre
        return most_common_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

#helper function
def list_friends_movies(user_data):
    friends_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_movies.append(movie)
    
    return friends_movies

def get_unique_watched(user_data):
    user_unique_watched = []
    user_movies = user_data["watched"]
    friends_movies = list_friends_movies(user_data)

    for movie in user_movies:
        if movie not in friends_movies:
            user_unique_watched.append(movie)
    
    return user_unique_watched       

def get_friends_unique_watched(user_data):
    friends_unique_watched = []
    user_movies = user_data["watched"]
    friends_movies = list_friends_movies(user_data)

    for movie in friends_movies:
        if movie not in user_movies and movie not in friends_unique_watched:
            friends_unique_watched.append(movie)
    
    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies = []
    friends_unique_watched = get_friends_unique_watched(user_data)

    for movie in friends_unique_watched:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    
    return recommended_movies
    

# -----------------------------------------
# ------------- WAVE 5 --------------------
# ----------------------------------------- 
def get_new_rec_by_genre(user_data):
    recommended_by_genre = []
    friends_unique_watched = get_friends_unique_watched(user_data)
    user_most_watched_genre = get_most_watched_genre(user_data)

    for movie in friends_unique_watched:
        if movie["genre"] == user_most_watched_genre:
            recommended_by_genre.append(movie)

    return recommended_by_genre


def get_rec_from_favorites(user_data):
    recommended_favorites = []
    user_favorites = user_data["favorites"]
    user_unique_watched = get_unique_watched(user_data)

    for movie in user_favorites:
        if movie in user_unique_watched:
            recommended_favorites.append(movie)
    
    return recommended_favorites
