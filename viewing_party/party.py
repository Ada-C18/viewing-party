# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    #pass
    if title and genre and rating:
        new_movie = {"title": title , "genre": genre, "rating": rating}
        return new_movie
    else: 
        return None 

def add_to_watched(user_data, movie):

    user_data.get("watched").append(movie)
    return user_data

def add_to_watchlist(user_data, movie):

    user_data.get("watchlist").append(movie)
    return user_data

def watch_movie(user_data, title):

    for movie in user_data.get("watchlist"):

        if movie["title"] == title:
            user_data.get("watchlist").remove(movie)
            user_data.get("watched").append(movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):

    if len(user_data.get("watched")) == 0:
        return 0.0

    rating_avergae = 0

    for movie in user_data.get("watched"):
        rating_avergae +=  movie["rating"]

    return rating_avergae / len(user_data.get("watched"))

def get_most_watched_genre(user_data):

    if len(user_data.get("watched")) == 0:
        return None

    popular_genre = {}
    for movie in user_data.get("watched"):
        genre = movie["genre"] 

        if genre not in popular_genre:
            popular_genre[genre] = 1
        else: 
            popular_genre[genre] += 1

    most_count = 0
    most_popular_genre = ""

    for g, value in popular_genre.items():

        if value > most_count:
            most_count = value 
            most_popular_genre = g
            
    return most_popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    unique_watched = []
    friend_movies = []

    for friend in user_data.get("friends"):
        for f_movie in friend.get("watched"):

            if f_movie not in friend_movies:
                friend_movies.append(f_movie)
    
    # trying list comprehension
    unique_watched = [movie
        for movie in user_data.get("watched")
            if movie not in friend_movies]

    return unique_watched

def get_friends_unique_watched(user_data):

    unique_watched = []
    friend_movies = []

    for friend in user_data.get("friends"):
        for f_movie in friend.get("watched"):

            if f_movie not in friend_movies:
                friend_movies.append(f_movie)

    for f_movie in friend_movies:

        if f_movie not in user_data.get("watched"):
            unique_watched.append(f_movie)

    return unique_watched
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):

    recs_movie = []

    friends_movie = get_friends_unique_watched(user_data)

    for movie in friends_movie:
        if movie["host"] in user_data.get("subscriptions"):
            recs_movie.append(movie)
    return recs_movie


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

