# ------------- WAVE 1 --------------------

from distutils.file_util import move_file


def create_movie(title, genre, rating):

    movie = {"title" : title,
    "genre" : genre, 
    "rating" : rating}

# if three attributes are truthy, i.e. we have all any truthy values for all attribues
    if title and genre and rating:
        return movie
# otherwise, it's not movie. return none
    else:
        return None 

def add_to_watched(user_data, movie):

# insert movie (in dict) in the watched (in list) in user_data (in dict)
# exception: if no watched list (poor baby), create an empty one.

    if not user_data["watched"]:
        user_data["watched"] = [] 

    user_data["watched"].append(movie)

    return user_data

def add_to_watchlist(user_data, movie):

# insert movie (in dict) in the watchlist (in list) in user_data (in dict)
# exception: if no watchlist (poor baby), create an empty one.

    if not user_data["watchlist"]:
        user_data["watchlist"] = [] 

    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):
    
    movies_watchlist = user_data["watchlist"] # in list

    for movie in movies_watchlist:
        if title in movie["title"]:
            # a removed & added list is reflected to user_data dict because dict is mutable
            movies_watchlist.remove(movie) 
            add_to_watched(user_data, movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
# (1) extract each movie from a list and get each rating
# (2) sum up rating during loop
# exception: empty watched (poor!), return 0.0

    watched_list = user_data["watched"]
    rating_sum = 0.0
    n = len(watched_list)
    if n == 0:
        rating_avg = 0.0
    else:
        for movie in watched_list:
            rating = movie["rating"]
            rating_sum += rating
        rating_avg = rating_sum/n
    return rating_avg

def get_most_watched_genre(user_data):
# (1) extract each movie from a list and get each genre
# (2-0) genres in dict
# (2-1) new genre: create key & set value 1 
# (2-2) ex-genre: value +1 
# (3) find key corresponing max value ! assume no multiple keys :p
# exception: empty watched (poor!), return None

    watched_list = user_data["watched"]
    
    if watched_list == []:
        return None
    else:
        genres = {}
        for movie in watched_list:
            genre = movie["genre"] 
            if not genre in genres:
                genres[genre] = 1
            else:
                genres[genre] += 1 
        max_genre = max(genres, key=genres.get)
        return max_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
# (1) watched list of user
# (2) friend's list
# (3) compare two lists
# (4) return user's unique list (elements in dict!) 

    titles_user = []
    titles_friends = []
    watched_list = user_data["watched"]
    friends_list = user_data["friends"]

    # movie titles of user
    for movie in watched_list:
        title = movie["title"]
        titles_user.append(title) 

    # friend in dict
    for friend in friends_list: 
        movie_list_each_friend = friend["watched"]
        for movie in movie_list_each_friend:
            title = movie["title"]
            titles_friends.append(title)

    # compare 
    movie_set_user = set(titles_user)
    movie_set_friends = set(titles_friends)
    unique_movie_title_user = movie_set_user - movie_set_friends

    # list of unique movies (in dict)
    unique_movie_user = []
    for movie in watched_list:
        title = movie["title"]
        if title in unique_movie_title_user:
            unique_movie_user.append(movie)

    return unique_movie_user

def get_friends_unique_watched(user_data):
# (1) watched list of user
# (2) friend's list
# (3) compare two lists
# (4) return frieds' unique list (elements in dict!) 
    titles_user = []
    titles_friends = []
    watched_list = user_data["watched"]
    friends_list = user_data["friends"]

    # movie titles of user
    for movie in watched_list:
        title = movie["title"]
        titles_user.append(title) 

    # friend in dict
    for friend in friends_list: 
        movie_list_each_friend = friend["watched"]
        for movie in movie_list_each_friend:
            title = movie["title"]
            titles_friends.append(title)
        
    # compare 
    movie_set_user = set(titles_user)
    movie_set_friends = set(titles_friends)
    unique_movie_title_friends = movie_set_friends - movie_set_user

    # list of unique movies (in dict)
    unique_movie_friends = []
    for friend in friends_list: 
        movie_list_each_friend = friend["watched"]
        for movie in movie_list_each_friend:
            title = movie["title"]
            # avoid duplicate!
            if title in unique_movie_title_friends and not movie in unique_movie_friends:
                print(title)
                unique_movie_friends.append(movie)
        
    return unique_movie_friends

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    pass

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    pass

