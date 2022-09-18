# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    inputs = [title, genre, rating]
    for input in inputs:
        if input == None:
            return None
    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
    return new_movie

def add_to_watched(user_data, movie): 
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    movie_index = 0
    for movie in user_data["watchlist"]:
        if movie_title == movie["title"]:
            movie_dict = user_data["watchlist"][movie_index]
            user_data["watched"].append(movie_dict)
            user_data["watchlist"].pop(movie_index)
        movie_index += 1

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) == 0:
        return 0.0
    ratings_list = []
    for movie in user_data["watched"]:
        ratings_list.append(movie["rating"])
    return sum(ratings_list)/len(ratings_list)
    
def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    genre_count = {}
    for movie in user_data["watched"]:
        movie_genre = movie["genre"]
        if movie_genre not in genre_count:
            genre_count[movie_genre] = 1
        elif movie_genre in genre_count:
            genre_count[movie_genre] += 1
    
    genre_max = max(genre_count, key=genre_count.get)
    return genre_max      
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_movies = []
    friend_movies = []
    unique_movies = []
    for movie in user_data["watched"]:
        user_movies.append(movie)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.append(movie)
    for movie in user_movies:
        if movie not in friend_movies and movie not in unique_movies:
            unique_movies.append(movie)
    return unique_movies
        
def get_friends_unique_watched(user_data):
    user_movies = []
    friend_movies = []
    unique_movies = []
    for movie in user_data["watched"]:
        user_movies.append(movie)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.append(movie)
    for movie in friend_movies:
        if movie not in user_movies and movie not in unique_movies:
            unique_movies.append(movie)
    return unique_movies
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommendations = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
                recommendations.append(movie)
    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    fav_genre = get_most_watched_genre(user_data)
    friends_movies = get_friends_unique_watched(user_data)
    rec_list = []
    for movie in friends_movies:
        if movie["genre"] == fav_genre:
            rec_list.append(movie)
    return rec_list

def get_rec_from_favorites(user_data):
    users_unique_movies = get_unique_watched(user_data)
    rec_list = []
    for movie in users_unique_movies:
        if movie in user_data["favorites"]:
            rec_list.append(movie)
    return rec_list