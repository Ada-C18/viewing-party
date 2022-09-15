# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
            }
        return movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    number_of_movies = len(user_data["watched"])
    if not number_of_movies:
        return 0.0

    total_rating = 0
    for watched_movie in user_data["watched"]:
        total_rating += watched_movie["rating"]
    return total_rating / number_of_movies

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    
    genre_counter = {}
    for watched_movie in user_data["watched"]:
        genre = watched_movie["genre"]
        if genre in genre_counter:
            genre_counter[genre] += 1
        else:
            genre_counter[genre] = 1
    
    most_watched_genre, max_count = None, 0
    for genre, count in genre_counter.items():
        if count > max_count:
            most_watched_genre = genre
            max_count = count
    return most_watched_genre
    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

