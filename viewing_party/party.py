# ------------- WAVE 1 --------------------

def create_movie(movie_title, genre, rating):
    my_movie = {
        "title" : movie_title,
        "genre" : genre,
        "rating" : rating,
    }

    return my_movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data    

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, movie):
    user_data["watched"].append(movie)
    user_data["watchlist"] = []

    return user_data

def watched_movie(user_data, movie_to_watch):

    if movie_to_watch in user_data["watchlist"]:
        user_data["watched"].append(movie_to_watch)
        user_data["watchlist"].remove(movie_to_watch)   

    return user_data


        


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    all_ratings = []
    for watch in watched_list:
        all_ratings.append(watch["rating"])
    rating_sum = sum(all_ratings)
    if len(user_data["watched"]) == 0:
        avg_rating = 0
    else:
        avg_rating = rating_sum/len(user_data["watched"])

    return avg_rating


def get_most_watched_genre(user_data):
    genre_list = user_data["watched"]
    all_genres = []
    for genres in genre_list:
        all_genres.append(genres["genre"])
    
    if len(all_genres) == 0:
        return None
    else:
        counter = 0
        num = all_genres[0]
        
        for i in all_genres:
            frequency = all_genres.count(i)
            if frequency > counter:
                counter = frequency
                num = i
        return num
    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    all_friends_movies = []
    i = 0
    for friend in user_data["friends"]:
        for friend_movies in user_data["friends"][i]["watched"]:
            all_friends_movies.append(friend_movies)
        i += 1

    friend_watched = []
    for friend_movie in all_friends_movies:
        friend_watched.append(friend_movie["title"])

    user_not_watched = []
    for user_movie in user_data["watched"]:
        if user_movie["title"] not in friend_watched:
            user_not_watched.append(user_movie)
    return user_not_watched

def get_friends_unique_watched(user_data):
    friend_watched = []

    all_friends_movies = []
    i = 0
    for friend_movies in user_data["friends"]:
        for friend_movies in user_data["friends"][i]["watched"]:
            all_friends_movies.append(friend_movies)
        i += 1

    seen = set()
    clean_all_friends_movies = []
    for friend_movies in all_friends_movies:
        t = tuple(friend_movies.items())
        if t not in seen:
            seen.add(t)
            clean_all_friends_movies.append(friend_movies)

    for friend_movies in clean_all_friends_movies:
        if friend_movies not in user_data["watched"]:
            friend_watched.append(friend_movies)
    return friend_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    all_friends_movies = []
    i = 0
    for friend in user_data["friends"]:
        for friend_movies in user_data["friends"][i]["watched"]:
            all_friends_movies.append(friend_movies)
        i += 1

    friends_watched = []
    for friend_movies in all_friends_movies:
        if friend_movies not in user_data["watched"]:
            friends_watched.append(friend_movies)

    recomended_movies = []
    j = 0
    for movies in friends_watched:
        for subscription in user_data["subscriptions"]:
            if subscription in friends_watched[j]["host"]:
                recomended_movies.append(movies)
        j += 1

    return recomended_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------