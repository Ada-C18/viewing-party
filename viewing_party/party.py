# ------------- WAVE 1 --------------------

from enum import unique


def create_movie(title, genre, rating):
    my_dict = {}

    if not bool(title) or not bool(genre) or not bool(rating):
        return None
    else:
        my_dict["title"] = title
        my_dict["genre"] = genre
        my_dict["rating"] = rating
        
    return my_dict

def add_to_watched(user_data, movie):
    watched_movies_list = user_data.get('watched')
    watched_movies_list.append(movie)
    user_data["watched"] = watched_movies_list
    
    return user_data
    
def add_to_watchlist(user_data, movie):
    watchlist_movies_list = user_data.get('watchlist')
    watchlist_movies_list.append(movie)
    user_data["watchlist"] = watchlist_movies_list
    return user_data
    
def watch_movie(user_data, title):
    watchlist_movies = user_data.get('watchlist')
    for movie in watchlist_movies:
        if movie["title"] == title:
            watchlist_movies.remove(movie)
            updated_user_data = add_to_watched(user_data, movie)
            return updated_user_data
    return user_data


#  --------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched_list = user_data.get("watched")
    if not bool(watched_list):
        return 0.0
    rating_sum = 0.0
    for movie in watched_list:
        rating_sum += movie["rating"]
        
    average_rating = rating_sum/len(watched_list)
    return average_rating


def get_most_watched_genre(user_data):
    watched_list = user_data.get("watched")
    if not bool(watched_list):
        return None
    genre_dict = {}
    for movie in watched_list:
        genre = movie.get("genre")
        if genre in genre_dict:
            count = genre_dict[genre]
            count += 1
            genre_dict[genre] = count
        else:
            genre_dict[genre] = 1
    most_frequent_genre = ""
    most_frequent_genre_count = 0
    for genre in genre_dict:
        if genre_dict[genre] > most_frequent_genre_count:
            most_frequent_genre_count = genre_dict[genre]
            most_frequent_genre = genre
    return most_frequent_genre
            
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique_watched_list = []
    for my_movie in user_data.get("watched"):
        is_movie_unique = True
        friends = user_data.get("friends")
        for friend in friends:
            friend_watched_list = friend.get("watched")
            for friend_movie in friend_watched_list:
                if my_movie["title"] == friend_movie["title"]:
                    is_movie_unique = False
        if is_movie_unique == True:
            unique_watched_list.append(my_movie)
    return unique_watched_list
                    
def get_friends_unique_watched(user_data):
    friends_unique_watched = []
    friends_watched_list = []
    for movie in user_data["watched"]:
        if movie not in friends_watched_list:
            friends_watched_list.append(movie)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched_list and movie not in friends_unique_watched:
                friends_unique_watched.append(movie)
            
    return friends_unique_watched
    
    
    
    


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies = []
    host_list =[]
    friends_watched = get_friends_unique_watched(user_data)
    for host in user_data["subscriptions"]:
        host_list.append(host)
    for friend in friends_watched:
        # friend_watched_movie_list = friend.get("watched")
        if friend["host"] in host_list:
            recommended_movies.append(friend)
    return recommended_movies         
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    reccom_list  = []
    my_genre = get_most_watched_genre(user_data)
    friends_watched = get_friends_unique_watched(user_data)
    for movie in friends_watched:
        if movie["genre"] == my_genre:
            reccom_list.append(movie)
    return reccom_list

def get_rec_from_favorites(user_data):
    recs_list = []
    users_unique_movie = get_unique_watched(user_data)
    my_favorites = user_data.get("favorites")
    for movie in my_favorites:
        for friends_movie in users_unique_movie:
            if movie["title"] == friends_movie["title"]:
                recs_list.append(movie)
    return recs_list
    
