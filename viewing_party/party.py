# ------------- WAVE 1 --------------------

# from imp import new_module
# from turtle import title
# from os import remove

from codecs import unicode_escape_decode


def create_movie(title, genre, rating):
    new_movie = {"title": title,
            "genre": genre,
            "rating": rating}
    
    if new_movie["genre"] == None:
        return None
    if new_movie["rating"] == None:
        return None
    if new_movie["title"] == None:
        return None
    return new_movie

def add_to_watched(user_data, movie):
    user_data = {}
    user_data["watched"] = [movie]
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {}
    user_data["watchlist"] = [movie]
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            return user_data            
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating = []
    sum = 0.0

    if not user_data["watched"]:
        return sum
    for i in user_data["watched"]: #4.0, 4.8
        if i["rating"] != None: 
            sum += i["rating"] #4.0 + 4.8 = 8.8 
            rating.append(i["rating"]) #[4.0, 4.8]          
    return sum/len(rating)


def get_most_watched_genre(user_data): 
    fav_genre = []
    counter = 0
    top_genre = fav_genre

    for i in user_data["watched"]:
        fav_genre.append(i["genre"])
    
    for genre in fav_genre:
        curr_freq = fav_genre.count(genre)
        if(curr_freq > counter):
            counter = curr_freq
            top_genre = genre
            return top_genre
        elif fav_genre == []:
            return None


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    list_of_movies = []
    all_friend_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in all_friend_movies:
                all_friend_movies.append(movie)

    for movie in user_data["watched"]:
        if movie not in all_friend_movies:
            list_of_movies.append(movie)
    return list_of_movies    
    
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
    friends_movies = get_friends_unique_watched(user_data)
    user_subscriptions = []
    list_of_recommendations = []

    for user in user_data["subscriptions"]:
        user_subscriptions.append(user)
    for item in friends_movies:
        if item["host"] in user_subscriptions:
            list_of_recommendations.append(item)
    return list_of_recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    fave_user_genre = get_most_watched_genre(user_data)
    recommended_list = []
    unique_watched = get_friends_unique_watched(user_data)
    

    if not user_data["watched"]:
        return recommended_list
    for movie in unique_watched:
        if movie["genre"] in fave_user_genre:
            recommended_list.append(movie)
    return recommended_list

def get_rec_from_favorites(user_data):
    list_of_movie_recs = []
    friend_watch_list = []
    
    for movie in user_data["friends"]:
        for item in movie["watched"]:
            friend_watch_list.append(item)

    for movie in user_data["favorites"]:
        if movie not in friend_watch_list:
            list_of_movie_recs.append(movie)
    return list_of_movie_recs 



