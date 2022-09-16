# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movies = {}
    if None in [title, genre, rating]: 
        return None
    movies["title"] = title
    movies["genre"] = genre
    movies["rating"] = rating
    return movies

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"] #[{}]
    watched = user_data["watched"] #[{}]
    for i in range(0, len(watchlist)):
        if title == watchlist[i]["title"]:
            watched.append(watchlist[i])
            watchlist.remove(watchlist[i])
    user_data["watchlist"] = watchlist
    user_data["watched"] = watched
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    ratings = []
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
    if len(ratings) >= 1:
        avg_ratings = sum(ratings)/len(ratings)
        return avg_ratings
    return 0.0

def get_most_watched_genre(user_data):
    genres = []
    if len(user_data["watched"]) >= 1:
        for movie in user_data["watched"]:
            genres.append(movie["genre"])
    
        genres_set = set(genres)
        genres_dict = {}
    
        for genre in genres_set: 
            genres_dict[genre] = genres.count(genre)
        
        genre_most = 0
        max_value = 0
        
        for key, value in genres_dict.items():
            if value > max_value: 
                max_value = value
                genre_most = key
        return genre_most
    return None
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

