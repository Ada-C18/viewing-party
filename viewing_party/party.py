# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    movie = {}

    if title == None or genre == None or rating == None:
        return None
    else:
        movie['title'] = title
        movie['genre'] = genre
        movie['rating'] = rating
        
    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)   

    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].pop()
    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total_ratings = 0
    total_movies = len(user_data['watched'])
    
    for index in range(len(user_data["watched"])):
        total_ratings+= user_data["watched"][index]["rating"]

    if total_ratings == 0:
        return 0.0

    average = total_ratings/total_movies
    
    return average

def get_most_watched_genre(user_data):
    if len

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
