# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    
    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie
    
    return None 

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    
    return user_data

def watch_movie(user_data, movie_to_watch):
    updated_watchlist = user_data["watchlist"]
    updated_watched = user_data["watched"]
    updated_data = {
        "watchlist": list(user_data["watchlist"]),
        "watched": list(user_data["watched"])
    }
    
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_to_watch:
            updated_data["watched"].append(movie)
            updated_data["watchlist"].remove(movie)
    
    return updated_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    ratings = []
    
    if not user_data["watched"]:
        return 0.0
    
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
    
    avg_rating = sum(ratings) / len(ratings)
    return avg_rating

def get_most_watched_genre(user_data):
    genre_count = {}
    
    if not user_data["watched"]:
        return None
    
    for movie in user_data["watched"]:
        if movie["genre"] in genre_count:
            genre_count[movie["genre"]] += 1
        else:
            genre_count[movie["genre"]] = 1
    
    most_watched = max(genre_count, key=genre_count.get)
    return most_watched

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_movies = []
    friends_watched = []
    
    for watched_dict in user_data["friends"]:
        for movie in watched_dict["watched"]:
            friends_watched.append(movie)
    
    for movie in user_data["watched"]:
        if not movie in friends_watched:
            unique_movies.append(movie)
    
    return unique_movies

def get_friends_unique_watched(user_data):
    user_watched = []
    friends_unique_watched = []
    
    for movie in user_data["watched"]:
        user_watched.append(movie)
    
    for watched_dict in user_data["friends"]:
        for movie in watched_dict["watched"]:
            if not (movie in user_watched 
                    or movie in friends_unique_watched): 
                friends_unique_watched.append(movie)
    
    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friends_unique_watched = get_friends_unique_watched(user_data)
    recommendations = []
    
    if len(friends_unique_watched) > 0:
        for movie in friends_unique_watched:
            if movie["host"] in user_data["subscriptions"]:
                recommendations.append(movie)
    
    return recommendations
    
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    friends_unique_watched = get_friends_unique_watched(user_data)
    user_watched_genres = []
    recommendations = []
    
    if (len(friends_unique_watched) > 0
        and len(user_data["watched"]) > 0):
    
        for movie in user_data["watched"]:
            user_watched_genres.append(movie["genre"])
        
        for movie in friends_unique_watched:
            if (movie["host"] in user_data["subscriptions"] 
                and movie["genre"] in user_watched_genres):
                recommendations.append(movie)
    
    return recommendations

def get_rec_from_favorites(user_data):
    user_unique_watched = get_unique_watched(user_data)
    recommendations = []
    
    if len(user_data["favorites"]) > 0:
        
        for movie in user_data["favorites"]:
            if movie in user_unique_watched:
                recommendations.append(movie)
        
    return recommendations