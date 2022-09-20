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

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

