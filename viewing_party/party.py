# ------------- WAVE 1 --------------------

from audioop import avg
from email.policy import default
from errno import EDEADLK
from symbol import subscript
from xml.dom.minidom import Element


def create_movie(title, genre, rating):
    #return None for invaild input
    if title == None or genre == None or rating == None:
        return None
    
    # create dict with given input
    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating,
    }

    # return the dict
    return new_movie 

    # add movie dict to watched list
def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return user_data


    # add movie to watchlist
def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

    #  move movie from watchlist to watched
def watch_movie(user_data,title):
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    for movie in watchlist:
        if movie["title"] == title:
            watched.append(movie)
            watchlist.remove(movie)
                
    return user_data
    
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched = user_data["watched"]
    rating_list = []
    for movie in watched:
       rating_list.append(movie["rating"])
    avg = sum(rating_list) / (len(rating_list) or 1)
    return avg

  
 
     

def get_most_watched_genre(user_data):
     watched = user_data["watched"]
     watched_dict = {}
     for movie in watched:
        genre = movie["genre"]

        if movie not in watched:
            return None

        if genre not in watched_dict:
            watched_dict[genre] = 1 
        else: 
            watched_dict[genre] += 1 
               
        most_watched = max(watched_dict)
        return most_watched

        

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_friends_movies(user_data):
    friends_watched_list = []
    friends_watched_list_of_dicts = user_data["friends"]

    for index in range(len(friends_watched_list_of_dicts)):
        for index_2 in range(len(friends_watched_list_of_dicts[index]["watched"])):
            friends_watched_list.append(friends_watched_list_of_dicts[index]["watched"][index_2])

    return friends_watched_list


def get_unique_watched(user_data):
    unique_movies = []
    user_watched_list = user_data["watched"]
    friends_watched_list = get_friends_movies(user_data)

    for index in range(len(user_watched_list)):
        if not user_watched_list[index] in friends_watched_list:
            unique_movies.append(user_watched_list[index])
    
    return unique_movies

def get_friends_unique_watched(user_data):
    not_watched_by_user = []
    friends_watched_list = get_friends_movies(user_data)
    user_watched_list = user_data["watched"]

    for movie in friends_watched_list:
        if not movie in user_watched_list and not movie in not_watched_by_user:
            not_watched_by_user.append(movie)
    
    return not_watched_by_user






# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friends_unique_movies = get_friends_unique_watched(user_data)
    recommended_movies = []
    user_subscriptions = user_data["subscriptions"]

    for movie in friends_unique_movies:
        host = movie["host"]
        if host in user_subscriptions:
            recommended_movies.append(movie)
    return recommended_movies



#Returns a list of all movie titles watched by user
def user_watched_movies(user_data):
    watched_list_of_dicts = user_data["watched"]

    titles_list = []
    for movie_dict in watched_list_of_dicts:
        titles_list.append(movie_dict["title"])

    return titles_list


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -------------------------------------------
def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    friends_unique_list = get_friends_unique_watched(user_data)
    new_rec_genre = []
     
    for movie in friends_unique_list:
        genre = movie["genre"]
        if movie not in friends_unique_list:
            return None
        if genre == most_watched_genre:
            new_rec_genre.append(movie)
    return new_rec_genre



def get_rec_from_favorites(user_data):
    friends_watched_list = []
    friends = user_data["friends"]
  
    for friend in friends:
            for movie in  friend["watched"]:
                friends_watched_list.append(movie)

    recs_for_friends = []

    for movie in user_data["favorites"]:
            if movie not in friends_watched_list:
                recs_for_friends.append(movie)

    return recs_for_friends



