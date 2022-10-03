# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}
    if title and genre and rating:
        movie['title'] = title
        movie['genre'] = genre
        movie['rating'] = rating
        return movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    watchlist = []
    watchlist.append(movie)
    user_data["watchlist"] = watchlist
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            break         
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_sum = 0
    average_rating = 0
    if user_data["watched"]:
        for movie in user_data["watched"]:
            rating_sum += movie["rating"]
        average_rating = rating_sum/ len(user_data["watched"])
    return average_rating


def get_most_watched_genre(user_data):
    watched_genres = {}
    most_watched_count = 0

    if not user_data["watched"]:
        return None

    for movie in user_data["watched"]:
        if movie["genre"] not in watched_genres:
            watched_genres[(movie["genre"])] = 1
        else:
            watched_genres[(movie["genre"])] += 1
    
    for genre, count in watched_genres.items():
        if count > most_watched_count:
            most_watched_count = count
            most_watched_genre = genre

    return most_watched_genre


    



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):

    unique_watched = []
    user_watched_movies = user_data['watched']
    friends_watched_movies = []

    for friend in user_data['friends']:
        for movie in friend['watched']:
            friends_watched_movies.append(movie)

    for movie in user_watched_movies:
        if movie not in friends_watched_movies:
            unique_watched.append(movie)
    
    return unique_watched


def get_friends_unique_watched(user_data):
    unique_watched = []
    user_watched_movies = user_data['watched']
    friends_watched_movies = []

    for friend in user_data['friends']:
        for movie in friend['watched']:
            friends_watched_movies.append(movie)

    for movie in friends_watched_movies:
        if movie not in user_watched_movies and movie not in unique_watched:
            unique_watched.append(movie)

    return unique_watched

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies = []
    host_list = user_data['subscriptions']
    friends_watched = get_friends_unique_watched(user_data)

    for movie in friends_watched:
        if movie['host'] in host_list:
            recommended_movies.append(movie)

    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    recommended_movies = []
    friends_watched = get_friends_unique_watched(user_data)
    favorite_genre = get_most_watched_genre(user_data)
    
    if favorite_genre and friends_watched:
        for movie in friends_watched:
            if movie['genre'] in favorite_genre:
                recommended_movies.append(movie)

    return recommended_movies


def get_rec_from_favorites(user_data):
    recommendations = []
    user_watched = get_unique_watched(user_data)
    
    for movie in user_data['favorites']:
        if movie in user_watched:
            recommendations.append(movie)

    return recommendations