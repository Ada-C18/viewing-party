# ------------- WAVE 1 --------------------

from enum import unique
from os import waitstatus_to_exitcode


def create_movie(title, genre, rating):
    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating

    if movie_dict["title"] == None or movie_dict["genre"] == None or movie_dict["rating"] == None:
        return None
       
    return movie_dict

def add_to_watched(user_data, movie_dict):
    # "watched" is the key, the whole movie_dict as a value thta 
    # append into the user_data which is also a dictionary
    user_data["watched"].append(movie_dict)
    return user_data


def add_to_watchlist(user_data, movie_dict):
    user_data["watchlist"].append(movie_dict)
    return user_data


def watch_movie(user_data, title):  # this one can still improve
    # get the values from the user_data's "watchlist" key, and put them into a list
    watch_list = user_data["watchlist"]
    watch_list_size = len(watch_list)
    for i in range(watch_list_size):
        # try to use for movie in watch_list
        if watch_list[i]["title"] == title:
            movie = watch_list[i]
            add_to_watched(user_data, movie)
            watch_list.remove(movie) 
            return user_data
    return user_data




# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_list = []
    ratings_sum = 0
    watch_list = user_data["watched"]
    # access the list inside the dict
    if len(watch_list) == 0:   # check if the list is empty
        return 0.0
    else: 
        for i in range(len(watch_list)):    
            rating_list.append(watch_list[i]["rating"])
            # a list contains elements, each elements as a key-value pair
            # watch_list[i]["rating"] only access the value from the key names "rating"
    for rate in rating_list:
        # access every rate inside the rating list
        ratings_sum += rate
        # add the rates together
    average = ratings_sum/len(rating_list)
    return average
    
    
def get_most_watched_genre(user_data):
    popular_genre = []
    genre_list = user_data["watched"]
    # print(genre_list)
    if len(genre_list) == 0:
        return None
    else:
       for j in range (len(genre_list)):
            popular_genre.append(genre_list[j]["genre"])
            # print(popular_genre)
    return max(set(popular_genre), key = popular_genre.count)




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    # firstly tried to use set and .difference() method
    friends_list = []
    unique_list = []
    # not_unique_list = []
    friend_watched = user_data["friends"]
    user_watched = user_data["watched"]

    for val in friend_watched:
        for movie in val["watched"]:
            friends_list.append(movie["title"])
    for title in user_watched:
        # if title["title"] not in friends_list:
        #     unique_list.append(title)
        # if title["title"] not in user_watched:
        #     not_unique_list.append(title)
        if title["title"] not in friends_list and\
        title["title"] not in user_watched:
            unique_list.append(title)
    return unique_list   


def get_friends_unique_watched(user_data):
    user_watched_list = []
    friends_unique_movies = []
    friend_watched = user_data["friends"]
    user_watched = user_data["watched"]

    for title in user_watched:
        user_watched_list.append(title["title"])
    for watched in friend_watched: 
        for title in watched["watched"]:
            if title["title"] not in user_watched_list and \
            title not in friends_unique_movies:
                friends_unique_movies.append(title)
    return friends_unique_movies   




        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    """ use helper function from get_friends_unique_watched """

    recommended_movie = []
    # host_list = []
    # result_list = []
    subscriptions_list = user_data["subscriptions"]
    # print(subscriptions_list)
    # friends_watched_list = user_data["friends"]
    
    # access the value in "host"
    # for watched in friends_watched_list:
    #     for title in watched["watched"]:
    #         # access the list [{'title': ,'genre': ,'rating': ,'host' ,}]
    #         result_list.append(title) 
    # for i in range(len(result_list)):  
    #     # read every element in list, and only get the values from "host"
    #     host_list.append(result_list[i]["host"])
    # print(host_list)

    friens_unique_watched = get_friends_unique_watched(user_data)
    # print(friends_watched_list)
    for i in range(len(friens_unique_watched)):
        # host_list.append(friens_unique_watched[i]["host"])
        if friens_unique_watched[i]["host"] in subscriptions_list:
        # if host_list in subscriptions_list:
            recommended_movie.append(friens_unique_watched[i])
        
    # for movie in get_friends_unique_watched(user_data):
    #     # print(movie)
    #     # read every movie from the helper function
    #     if host_list in subscriptions_list:
    #         # use if statament to access the host only in user's subscriptions
    #         recommended_movie.append(movie)
    return recommended_movie       
      
    




# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    ''' 
    use helper function from get_most_watched_genre(user_data) 
    and get_friends_unique_watched()
    '''
    recommended_movie = []
    popular_genre = get_most_watched_genre(user_data)
    # .split()
    # print(type(popular_genre))
    friends_unique_watched = get_friends_unique_watched(user_data)
    for i in range(len(friends_unique_watched)):
        # print(friens_unique_watched[i]["genre"])
        if friends_unique_watched[i]["genre"] == popular_genre:
            recommended_movie.append(friends_unique_watched[i])
    return recommended_movie


def get_rec_from_favorites(user_data):
    ''' 
    use the helper function get_unique_watched(user_data)
    to get the the movie list that none of the user's friends 
    have watched it 
    '''
    recommended_movie_by_favorite = []
    user_favorite_movies = user_data["favorites"]
    friends_not_watched = get_unique_watched(user_data)
    
    for movie in friends_not_watched:
        for title in user_favorite_movies:
            if movie == title:
               recommended_movie_by_favorite.append(movie) 
    return recommended_movie_by_favorite