# -----------------------------------------
# ---------- HELPER FUNCTIONS -------------
# -----------------------------------------
def get_watched_list(user_data):
    return user_data['watched']

def get_friends_watched_list(user_data):
    friends_list = user_data['friends']

    friends_watch_list = [dicts['watched'] for dicts in friends_list]
    friends_watch_list = [val for sublist in friends_watch_list for val in sublist]

    return list({movie['title']:movie for movie in friends_watch_list}.values())
# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------
def create_movie(title, genre, rating):
    
    if not title or not genre or not rating:
        return None

    return {'title': title, 'genre': genre, 'rating': rating}

def add_to_watched(user_data, movie):
    user_data_copy = user_data.copy()
    user_data_copy['watched'].append(movie)
    
    return user_data_copy

def add_to_watchlist(user_data, movie):
    user_data_copy = user_data.copy()
    user_data_copy['watchlist'].append(movie)
    
    return user_data_copy

def watch_movie(user_data, title):
    user_data_copy = user_data.copy()
    
    title_list = [dicts["title"] for dicts in user_data["watchlist"]]
    title_list.extend(dicts["title"] for dicts in user_data["watched"])
    
    if title not in title_list:
        return user_data
    user_data_copy["watched"].append(user_data_copy["watchlist"].copy())
    user_data_copy["watchlist"].pop()

    return user_data_copy
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched_list = get_watched_list(user_data)

    try:
        ratings_list = [movie['rating'] for movie in watched_list]
        return sum(ratings_list)/len(ratings_list)

    except ZeroDivisionError:
        return 0

def get_most_watched_genre(user_data):
    watched_list = get_watched_list(user_data)
    genre_list = [movie['genre'] for movie in watched_list]

    return max(genre_list, key = genre_list.count) if genre_list else None
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    watched_list = get_watched_list(user_data)
    friends_list = get_friends_watched_list(user_data)
    
    for movie in friends_list:
        if movie in watched_list:
            watched_list.remove(movie)
            
    return watched_list

def get_friends_unique_watched(user_data):
    watched_list = get_watched_list(user_data)
    friends_list = get_friends_watched_list(user_data)
    
    for movie in watched_list:
        if movie in friends_list:
            friends_list.remove(movie)
            
    return friends_list
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    watched_list = get_watched_list(user_data)
    subscriptions = user_data['subscriptions']
    friends_list = get_friends_watched_list(user_data)

    for movie in watched_list:
        if movie in friends_list:
            friends_list.remove(movie)

    recommendations = []
    for subs in subscriptions:
        recommendations.extend(movie for movie in friends_list if movie['host'] == subs)
        
    return recommendations
#  ----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    watched_list = get_watched_list(user_data)
    friends_list = get_friends_watched_list(user_data)
    
    if not watched_list:
        genre_list = []
        most_watched_genre = None
    else:
        genre_list = [movie['genre'] for movie in watched_list]
        most_watched_genre = max(genre_list, key=genre_list.count)
        
    recommendations = []
    for movie in friends_list:
        if movie['genre'] == most_watched_genre and movie not in recommendations and movie not in watched_list:
            recommendations.append(movie)
            
    return recommendations

def get_rec_from_favorites(user_data):
    user_favorites = user_data['favorites']
    friends_list = get_friends_watched_list(user_data)

    return [movie for movie in user_favorites if movie not in friends_list]