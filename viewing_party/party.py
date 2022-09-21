# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    if not title or not genre or not rating:
        return None
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
    return new_movie


def add_to_watched(user_data, movie):
    movies_watched_list = user_data["watched"]
    movies_watched_list.append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    movies_to_watch_list = user_data["watchlist"]
    movies_to_watch_list.append(movie)
    return user_data


def watch_movie(user_data, title):
    movies_to_watch_list = user_data["watchlist"]
    movies_watched_list = user_data["watched"]

    i = 0
    for movie in movies_to_watch_list:
        if movie["title"] == title:
            movies_watched_list.append(movie)
            del movies_to_watch_list[i]
        i+=1
    print(user_data)    
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    rating_sum = 0
    rating_counter = 0
    movies_watched_list = user_data["watched"]

    for movie in movies_watched_list:
        rating_sum += movie["rating"]
        rating_counter += 1

    if len(movies_watched_list) == 0:
        avg_rating = 0.0 
    else:
        avg_rating = rating_sum / rating_counter
        
    return avg_rating

def get_most_watched_genre(user_data):
    movies_watched_list = user_data["watched"]
    genre_frequency_map = {}
    max_frequency = 0
    popular_genre = None

    for movie in movies_watched_list:
        genre = movie["genre"]
        if genre not in genre_frequency_map:
            genre_frequency_map[genre] = 1
        else:
            genre_frequency_map[genre] += 1
    
    for genre, frequency in genre_frequency_map.items():
        if frequency > max_frequency:
            max_frequency = frequency
            popular_genre = genre
            
    return popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_watched_list = user_data["watched"]
    friends_list = user_data["friends"]
    unique_movies_watched = []
    
    for user_movie in user_watched_list:
        unique_movies_watched.append(user_movie)
    
    for friend in friends_list:
        for friend_movie in friend["watched"]:
            if friend_movie in unique_movies_watched:
                index_for_del = unique_movies_watched.index(friend_movie)
                del unique_movies_watched[index_for_del]
            
    return unique_movies_watched


def get_friends_unique_watched(user_data):
    user_watched_list = user_data["watched"]
    friends_list = user_data["friends"]
    friends_unique_movies_watched = []

    for friend in friends_list:
        for friend_movie in friend["watched"]:
            if friend_movie not in user_watched_list:
                if friend_movie not in friends_unique_movies_watched:
                    friends_unique_movies_watched.append(friend_movie)

    return friends_unique_movies_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    potential_recs = get_friends_unique_watched(user_data)
    recommendations = []
    user_subscriptions = user_data["subscriptions"]

    for rec in potential_recs:
        if rec["host"] in user_subscriptions:
            recommendations.append(rec)
    
    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    potential_recs = get_friends_unique_watched(user_data)
    popular_genre = get_most_watched_genre(user_data)
    recommendations = []

    for rec in potential_recs:
        if rec["genre"] == popular_genre:
            recommendations.append(rec)
    
    return recommendations


def get_rec_from_favorites(user_data):
    potential_recs = get_unique_watched(user_data)
    user_favorites = user_data["favorites"]
    recommendations = []

    for rec in potential_recs:
        if rec in user_favorites:
            recommendations.append(rec)
    
    return recommendations
