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
    genre_watched = {}
    most_watched = 0
    most_watched_genre = ""
    
    if len(user_data['watched']) == 0:
        return None
    
    for movie in user_data['watched']:
        genre = movie['genre']
        if genre in genre_watched.keys():
            genre_watched[genre] +=1
        else:
            genre_watched[genre] = 1

    for v in genre_watched.values():
        if v > most_watched:
            most_watched = v
    for k in genre_watched.keys():
        if genre_watched[k] == most_watched:
            most_watched_genre = k 

    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_movies = user_data['watched']
    friends_movies = user_data['friends']
    friend_movies_combined = []
    unique_movies = []
    
    for friend_dict in friends_movies:
        for friend_movie in friend_dict['watched']:
            if friend_movie not in friend_movies_combined:
                friend_movies_combined.append(friend_movie)

    for m in user_movies:
        if m not in friend_movies_combined:
            unique_movies.append(m)
    
    return unique_movies

def get_friends_unique_watched(user_data):
    user_movies = user_data['watched']
    friends_movies = user_data['friends']
    unique_movies = []
    
    for friend_dict in friends_movies:
        for friend_movie in friend_dict['watched']:
            if friend_movie not in user_movies and friend_movie not in unique_movies:
                unique_movies.append(friend_movie)
    
    return unique_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    user_movies = user_data['watched']
    friends_movies = user_data['friends']
    subscriptions = user_data['subscriptions']

    recommended_movies = []

    for friend_dict in friends_movies:
        for friend_movie in friend_dict['watched']:
            if friend_movie not in user_movies and friend_movie['host'] in subscriptions:
                recommended_movies.append(friend_movie)

    return recommended_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)

    user_movies = user_data['watched']
    friends_movies = user_data['friends']

    recommended_movies = []

    for friend_dict in friends_movies:
        for friend_movie in friend_dict['watched']:
            if friend_movie not in user_movies and friend_movie['genre'] == most_watched_genre:
                recommended_movies.append(friend_movie)

    return recommended_movies

def get