# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {"title": title,"genre":genre,"rating":rating}
        return movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    user_data = {"watched":[]}
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {"watchlist":[]}
    user_data["watchlist"].append(movie)
    return user_data
    

def watch_movie(user_data,title):
    watched_movie = None
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            watched_movie = movie
            break
    if watched_movie:
        user_data["watchlist"].remove(watched_movie)
        user_data["watched"].append(watched_movie)
    return user_data

        
        
# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    movies = user_data["watched"]
    average_rating = 0.0
    sum = 0
    for movie in movies:
        sum += movie["rating"]
        average_rating = sum/len(movies)

    return average_rating

def get_most_watched_genre(user_data):
    movies = user_data["watched"]
    if len(movies) < 1:
        return None
    genre_count = {}
    for movie in movies:
        genre = movie["genre"]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1
    popular_genre = max(genre_count, key=genre_count.get)
    return popular_genre




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

