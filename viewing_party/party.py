# ------------- WAVE 1 --------------------

def create_movie(movie_title, genre, rating):
    my_movie = {
        "title" : movie_title,
        "genre" : genre,
        "rating" : rating,
    }
    for keys in my_movie:
        if my_movie[keys] == False:
            return None
    
    return my_movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data    

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    title = user_data["watchlist"][0]
    user_data["watched"].append(title)
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
   
    ratings_list = []
    for movie in user_data["watched"]:
        ratings_list.append(movie["rating"])

    if len(user_data["watched"]) == 0:
        avg_rating = 0
    else:
        avg_rating = sum(ratings_list)/len(user_data["watched"])

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
        for friend_movie in user_data["friends"][i]["watched"]:
            all_friends_movies.append(friend_movie)
        i += 1

    friend_titles = []
    for friend_movie in all_friends_movies:
        friend_titles.append(friend_movie["title"])

    friends_not_watched = []
    for user_movie in user_data["watched"]:
        if user_movie["title"] not in friend_titles:
            friends_not_watched.append(user_movie)
    return friends_not_watched

def get_friends_unique_watched(user_data):


    all_friends_movies = []
    i = 0
    for friend in user_data["friends"]:
        for friend_movie in user_data["friends"][i]["watched"]:
            all_friends_movies.append(friend_movie)
        i += 1

    seen = set()
    clean_all_friends_movies = []
    for friends_movie in all_friends_movies:
        t = tuple(friends_movie.items())
        if t not in seen:
            seen.add(t)
            clean_all_friends_movies.append(friends_movie)
    
    user_not_watched = []
    for friends_movies in clean_all_friends_movies:
        if friends_movies not in user_data["watched"]:
            user_not_watched.append(friends_movies)
    return user_not_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    all_friends_movies = []
    i = 0
    for friend in user_data["friends"]:
        for friends_movie in user_data["friends"][i]["watched"]:
            all_friends_movies.append(friends_movie)
        i += 1

    friends_user = []
    for friend_movies in all_friends_movies:
        if friend_movies not in user_data["watched"]:
            friends_user.append(friend_movies)

    recomended_movies = []
    j = 0
    for movie in friends_user:
        for subscription in user_data["subscriptions"]:
            if subscription in friends_user[j]["host"]:
                recomended_movies.append(movie)
        j += 1

    return recomended_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
from collections import Counter

def get_new_rec_by_genre(user_data):

    if len(user_data["watched"]) == 0:
        return []

    user_genre = []   
    for user_movies in user_data["watched"]:
        user_genre.append(user_movies["genre"])
        
        genre_count = Counter(user_genre)
        user_freq_genre = genre_count.most_common(1)[0][0]

    all_friends_movies = []
    i = 0
    for friend in user_data["friends"]:
        for friend_movie in user_data["friends"][i]["watched"]:
            all_friends_movies.append(friend_movie)
        i += 1

    user_not_watched = []
    for friends_movies in all_friends_movies:
        if friends_movies not in user_data["watched"]:
            user_not_watched.append(friends_movies)

    recommended_movies = []
    i = 0
    for movie in user_not_watched:
        if user_freq_genre in user_not_watched[i]["genre"]:
            recommended_movies.append(movie)
        i += 1

    return recommended_movies

def get_rec_from_favorites(user_data):

    i = 0
    for friend in user_data["friends"]:
        if len(user_data["friends"][i]["watched"]) == 0:
            return []
        i += 1

    all_friends_movies = []
    i = 0
    for friend in user_data["friends"]:
        for friend_movie in user_data["friends"][i]["watched"]:
            all_friends_movies.append(friend_movie)
        i += 1

    friend_titles = []
    for friend_movie in all_friends_movies:
        friend_titles.append(friend_movie["title"])

    friends_not_watched = []
    for user_movie in user_data["favorites"]:
        if user_movie["title"] not in friend_titles:
            friends_not_watched.append(user_movie)
    
    return friends_not_watched
