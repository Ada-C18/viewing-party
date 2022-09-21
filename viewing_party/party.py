# ------------- WAVE 1 --------------------

from enum import unique


def create_movie(title, genre, rating):
    all_movies = {
    "title": title,
    "genre": genre,
    "rating": rating
        }
    if not title or not genre or not rating:
        all_movies = None
    return all_movies

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie_title): 
    for movie in user_data["watchlist"]:
        if movie['title'] == movie_title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    
    return user_data
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):

    def clean_wave_2_data():
        clean_data = user_data["watched"]
        return clean_data
    
    clean_data = clean_wave_2_data()

    rating_sum = 0
    all_ratings = []

    for movie in clean_data:
        rating = movie['rating']
        all_ratings.append(rating)
        rating_sum += rating
    if len(all_ratings) == 0:
        return float(0)
    else:
        return float(rating_sum/len(all_ratings))

def get_most_watched_genre(user_data):
    clean_data = user_data["watched"]
    all_genres = [] # this is a list of all genres

    for movie in clean_data:
        genre = movie["genre"] 
        all_genres.append(genre)
    
    genre_count = {}
    

    for genre in all_genres:
        genre_count[genre] = all_genres.count(genre)

    if len(genre_count) == 0:
        return None
    else:
        return max(genre_count, key = genre_count.get)
        # max(arg1, arg2, *args, key)
        # .get is grabbing the key with the max value


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):

    watched_by_user = user_data["watched"]
    friends = user_data["friends"] 
    watched_by_friends = []


    for watched in friends:
        for movies in watched.values():
            for movie in movies:
                watched_by_friends.append(movie)

    return [movie for movie in watched_by_user if movie not in watched_by_friends]
            # keep movie for movie in watched by user list if movie is not in the watched by friends list

def get_friends_unique_watched(user_data):
    watched_by_user = user_data["watched"]
    friends = user_data["friends"] 
    watched_by_friends = []


    for watched in friends:
        for movies in watched.values():
            for movie in movies:
                if movie not in watched_by_friends:
                    watched_by_friends.append(movie)
                

    return [movie for movie in watched_by_friends if movie not in watched_by_user]

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friends_watched = get_friends_unique_watched(user_data)
    subscriptions= user_data["subscriptions"]
    movie_recs = []

    for movie in friends_watched:
        if movie["host"] in subscriptions:
            movie_recs.append(movie)
    return movie_recs
# -----------------------------------------
# ------------- WAVE 5 --------------------
# ----------------------------------------- 
def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    friends_watched = get_friends_unique_watched(user_data)
    movie_recs = []

    for movie in friends_watched:
        if movie["genre"] == most_watched_genre:
            movie_recs.append(movie)
    return movie_recs
    # Check with classmates if their 5.3 test (Act, Assert) is different

def get_rec_from_favorites(user_data):
    favorites = user_data["favorites"]
    unique_movies = get_unique_watched(user_data)
    movie_recs = []

    for movie in favorites:
        if movie in unique_movies:
            movie_recs.append(movie)


    return movie_recs
    
# 