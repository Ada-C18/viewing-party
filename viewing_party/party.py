# ------------- WAVE 1 --------------------

from codecs import unicode_escape_decode


def create_movie(title, genre, rating):
    new_movie = {
    "title" : title,
    "genre" : genre,
    "rating" : rating
    }
    for key in new_movie:
        if not new_movie[key]:
            return None
        
    return new_movie


def add_to_watched(user_data, movie):
    # this function returns a list of dicts of movies the user watched 
    user_data["watched"] = [movie]
    return user_data


def add_to_watchlist(user_data, movie):
    # This function returns a list of dicts of movies the user wants to watch
    user_data["watchlist"] = [movie]
    return user_data


def watch_movie(user_data, title):
    # This functions checks if the title in movie is the same as the title in user_data watchlist list, 
    # and if yes, it removes it and adds it to the user_data watched list
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
    return user_data    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    avg_rating = 0.0
    if not user_data["watched"]:
        return avg_rating
    for movie in user_data["watched"]:
        avg_rating += movie["rating"]
    return avg_rating / len(user_data["watched"])


def get_most_watched_genre(user_data):
    genre_list = []
    counter = 0
    popular_genre = None
    if len(user_data["watched"]) == 0:
        return None
    else:
        for movie in user_data["watched"]:
            genre_list.append(movie["genre"])

        for item in genre_list:
            freq = genre_list.count(item)
            if freq > counter:
                counter = freq
                popular_genre = item
        return popular_genre
               

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_movies = []
    all_friends_movies = [] 

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in all_friends_movies:
                all_friends_movies.append(movie)

    for movie in user_data["watched"]:
        if movie not in all_friends_movies:
            unique_movies.append(movie)
    return unique_movies


def get_friends_unique_watched(user_data):
    user_movies = []
    unique_friend_movies = []
    for movie in user_data["watched"]:
        if movie not in user_movies:
            user_movies.append(movie)

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_movies and movie not in unique_friend_movies:
                unique_friend_movies.append(movie)
    return unique_friend_movies



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    list_rec_movies = []
    sub_list = []
    unique_watched = get_friends_unique_watched(user_data)
    for sub in user_data["subscriptions"]:
        sub_list.append(sub)
            
    for movie in unique_watched:
        if movie["host"] in sub_list:
            list_rec_movies.append(movie)
                
    return list_rec_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    rec_movies_list = []
    popular_genre = get_most_watched_genre(user_data)
    unique_watched = get_friends_unique_watched(user_data)

    if not user_data["watched"]:
        return rec_movies_list
    for movie in unique_watched:
            if movie["genre"] in popular_genre:
                rec_movies_list.append(movie)
    return rec_movies_list
    
def get_rec_from_favorites(user_data):
    fav_rec_movies = []
    friends_watched = []
    
    for movie in user_data["friends"]:
        for item in movie["watched"]:
            friends_watched.append(item)
    for movie in user_data["favorites"]:
        if movie not in friends_watched:
            fav_rec_movies.append(movie)
        
    return fav_rec_movies


