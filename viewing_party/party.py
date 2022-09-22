# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}

    if title == None or genre == None or rating == None:
        return None

    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating

    return new_movie

def add_to_watched(user_data, movie):
    # appends "watched" list value with movie data dict   
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    # appends "watchlist" list value with movie data dict
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    # moves movie data from "watchlist" list value to "watched" dict
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    # store the list of ratings in watched and their total added together
    watched_rating_list = []
    total_rating = 0

    user_data_watched = user_data["watched"]

    if user_data_watched == []:
        return 0.0

    # appends the watched_rating_list with the rating for each movie in the watched list
    for movie in user_data_watched:
        watched_rating_list.append(movie['rating'])

    # adds the ratings together and stores them in total_rating
    for rating in watched_rating_list:
        total_rating += rating

    avg_rating = total_rating / len(watched_rating_list)

    return avg_rating

def get_most_watched_genre(user_data):
    watched_genre_count = {}
    most_watched_genre_total = 0
    most_watched_genre = ""

    user_data_watched = user_data["watched"]

    if user_data_watched == []:
        return None

    for movie in user_data_watched:
        if movie["genre"] in watched_genre_count:
            watched_genre_count[movie["genre"]] += 1
        else:
            watched_genre_count[movie["genre"]] = 1

    for genre in watched_genre_count:
        if watched_genre_count[genre] > most_watched_genre_total:
            most_watched_genre_total = watched_genre_count[genre]
            most_watched_genre = genre

    return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    '''
    collects uniqe movies watched by user comopared to friends and
    stores it in a list, then returns that list
    '''
    unique_watched_list = []

    friend_watched_set = set(get_friends_watched(user_data))
    user_watched_set = set(get_users_watched(user_data))

    unique_set = user_watched_set - friend_watched_set

    for movie in unique_set:
        for i in range(len(user_data["watched"])):
            if user_data["watched"][i]['title'] == movie:
                unique_watched_list.append(user_data["watched"][i])   

    return unique_watched_list
    
    
    
def get_friends_watched(user_data):
    '''
    Stores the titles of the friends 'watched' list from user_data in a list,
    and returns that list
    '''   
    friends_list_of_dict = user_data["friends"]
    friends_watched_list = []

    for i in range(len(friends_list_of_dict)):
        for watched in friends_list_of_dict[i]:
            for movie in friends_list_of_dict[i][watched]:
                friends_watched_list.append(movie['title'])

    return friends_watched_list

def get_users_watched(user_data):
    user_watched_list = user_data["watched"]
    users_watched_movies = []

    for movie in user_watched_list:
        users_watched_movies.append(movie['title'])

    return users_watched_movies

# collect friends unique watched

def get_friends_unique_watched(user_data):
    '''
    collects unique watched movies from friends, stores them in a list,
    and returns the list
    '''
    unique_watched_list = []

    # User Data Watched Sets
    friend_watched_set = set(get_friends_watched(user_data))
    user_watched_set = set(get_users_watched(user_data))

    unique_set = friend_watched_set - user_watched_set

    # User Data Variables
    friends_list_dict = user_data["friends"]


    for i in range(len(friends_list_dict)):
        for friend_movie in friends_list_dict[i]["watched"]:
            if friend_movie["title"] in unique_set and friend_movie not in unique_watched_list:
                unique_watched_list.append(friend_movie) 

    return unique_watched_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    '''
    Returns a list of recommended movies based on what
    the user has a subscription to using user_data as input
    '''
    recommended_movies_list = []

    # User Data Watched Sets
    friend_watched_set = set(get_friends_watched(user_data))
    user_watched_set = set(get_users_watched(user_data))
    
    unique_set = friend_watched_set - user_watched_set

    # User Data Variables
    subscriptions_list = user_data['subscriptions']
    friends_list_dict = user_data["friends"]


    # Pull data for recommended movies from user data
    for i in range(len(friends_list_dict)):
        for friend_movie in friends_list_dict[i]["watched"]:
            if friend_movie["title"] in unique_set and friend_movie['host'] in subscriptions_list and friend_movie not in recommended_movies_list:
                recommended_movies_list.append(friend_movie) 

    return recommended_movies_list


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
# made it to wave 5!! *party emoji*

def get_new_rec_by_genre():
    pass