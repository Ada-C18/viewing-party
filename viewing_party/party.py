from pprint import pprint
import re
from unittest.mock import NonCallableMagicMock 
#HELPER FUNCTION
def _get_movies_watched_by_friends(user_data):
    movies_watched_by_friends = []

    for friend in user_data["friends"]: #[{}]
        for friend_movie in friend["watched"]: #{}
            if friend_movie in movies_watched_by_friends:
                continue
            else:
                movies_watched_by_friends.append(friend_movie)

    return movies_watched_by_friends

def _get_movies_not_watched_user(user_data):
    movies_not_watched_user = []
    movies_watched_by_friends = _get_movies_watched_by_friends(user_data) 

    for movie in user_data["watched"]:
        if movie not in movies_watched_by_friends:
            movies_not_watched_user.append(movie)
    return  movies_not_watched_user


# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None 

    return {"title":title, "genre":genre, "rating":rating}


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        watchlist_title = movie["title"]
        if title == watchlist_title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data

    return user_data
# Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify user_data.
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating = 0
    num_of_movies = len(user_data["watched"])
    
    for movie in user_data["watched"]:
        rating += movie["rating"]

    if rating == 0:
        return 0
    else:
        average_rating = rating/num_of_movies
    return average_rating
        
        


def get_most_watched_genre(user_data):
    favorite_genre = ""
    genre_list = []
    genre = ""

    # If the value of "watched" is an empty list, get_most_watched_genre should return None.
    if user_data["watched"] == []:
        return None 

    for movie in user_data["watched"]: #this giving each movie dictionary inside the watched list 
        genre = movie['genre'] #accessing the movie genre and assigning to the genre 
        genre_list.append(genre) #each genre will be added to the genre_list # the congregate of all genres


    favorite_genre = max(set(genre_list), key= genre_list.count) #inside this loop give me the max count of each genre 
    return favorite_genre
        
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_not_watched_movies = []
    movies_watched_by_friends = _get_movies_watched_by_friends(user_data) 

    for movie in user_data["watched"]:
        if movie not in movies_watched_by_friends:
            user_not_watched_movies.append(movie)
    return user_not_watched_movies


def get_friends_unique_watched(user_data):
    recommended_movies = []
    
    movies_watched_by_friends = []
    movies_watched_by_friends = _get_movies_watched_by_friends(user_data) 
    user_watched_movies = user_data["watched"] 

    for friend_movie in movies_watched_by_friends: #user_data = "friends": [{}]
        if friend_movie not in user_watched_movies:# if user_movie not in movies_watched_by_friends
            recommended_movies.append(friend_movie)
    
    # pprint(recommended_movies)
    return recommended_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies = []
    recommended_movies_subscription = []

    #USER INFO
    user_watched_movies = user_data["watched"] #[{}]
    # pprint(user_watched_movies)
    user_not_watched_movies = _get_movies_not_watched_user(user_data) #[{}]
	#USER SUBSCRIPTIONS 
    user_subscriptions = user_data["subscriptions"] #[]
    # print(user_subscriptions)
    movies_watched_by_friends = _get_movies_watched_by_friends(user_data)
    # pprint(movies_watched_by_friends)

    if movies_watched_by_friends == []:
        return None 

    #we want to retrieve the user_watched_movie:
        #and if the movie in movies_watched_by_friends
        #remove the movie and put it in a new list.
    # for movie in user_watched_movies:
    #     if movie not in movies_watched_by_friends:
    #         recommended_movies_subscription.append(movie)
    # print(recommended_movies_subscription)

    for friend_movie in movies_watched_by_friends: #user_data = "friends": [{}]
        if friend_movie not in user_watched_movies:# if user_movie not in movies_watched_by_friends
            recommended_movies.append(friend_movie)
    print(recommended_movies)
    
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    for movie in recommended_movies:
        if movie["host"] in user_subscriptions:
            pprint(recommended_movies_subscription.append(movie))

    return recommended_movies_subscription
            # recommended_movies_subscription.remove(movie["host"])
    # print(recommended_movies_subscription)
    # for movies in movies_watched_by_friends:
    #     movie_host_subscription = movies["host"]
    #     if movie_host_subscription in user_subscriptions:
    #         recommended_movies_subscription.append(movies)
    # pprint(recommended_movies_subscription)


    # return recommended_movies_subscription
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    pass