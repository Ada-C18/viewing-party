# ------------- WAVE 1 --------------------
#Melissa test

from enum import unique


def create_movie(title, genre, rating):
    if title and genre and rating:
        new_movie = {}
        new_movie["title"]= title
        new_movie["genre"]= genre
        new_movie["rating"]= rating
        
        return new_movie
    
    return None

def add_to_watched(user_data, movie):
    
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    
    for movie in user_data["watchlist"]:
        if movie["title"]== title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)

            return user_data

    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum=0
    avg=0
    length=len(user_data["watched"])
    for i in range(length):
        sum += user_data["watched"][i]["rating"]

        avg = sum/length
    return avg
    


def get_most_watched_genre(user_data):
    
    freq_genre= []

    if len(user_data["watched"])== 0:
        return None 

    for movie in user_data["watched"]:
        freq_genre.append(movie["genre"])

    most_freq_genre= max(set(freq_genre), key=freq_genre.count)
    return most_freq_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    
    # Create set of movies friends have watched
    friend_set = set()
    for friend in user_data['friends']:
        for movie in friend['watched']:
            friend_set.add(movie['title'])
    # Initialize unique_watched list
    unique_watched = []
    # Remove values from unique_watched that have titles in friend_set
    for movie in user_data['watched']:
        if movie["title"] not in friend_set:
            unique_watched.append(movie)

    return unique_watched

def get_friends_unique_watched(user_data):

    watched_movies = set()
    for movie in user_data["watched"]:
        watched_movies.add(movie["title"])

    unique=[]
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in watched_movies and movie not in unique:
                unique.append(movie)
    return unique

    # OLD CODE:

        # watched_movies_list=[]
        # for movie in user_data["watched"]:
        #     watched_movies_list.append(movie["title"])

        # set_watched_movies = set(watched_movies_list)

        # friend_movies_list=[]

        # for friend in user_data["friends"]:
        #     for movie in friend["watched"]:
        #         if movie["title"] not in friend_movies_list:
        #             friend_movies_list.append(movie["title"])

        # set_friends_movies = set(friend_movies_list)

        # unique_friends_movie= set_friends_movies.difference(set_watched_movies)


        # result=[]

        # for friend in user_data["friends"]:
        #     for movie in friend["watched"]:
        #         if movie["title"] in unique_friends_movie:
        #             result.append(movie)

        # return result 


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    watched_movies = set()
    for movie in user_data["watched"]:
        watched_movies.add(movie["title"])

    recommend=[]
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in watched_movies and movie["host"] in user_data['subscriptions']:
                recommend.append(movie)
    return recommend

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    freq_genre = get_most_watched_genre(user_data)

    
    watched_movies = set()
    for movie in user_data["watched"]:
        watched_movies.add(movie["title"])

    recomend_movie=[]
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in watched_movies and movie["genre"] == freq_genre:
                recomend_movie.append(movie)
    return recomend_movie


def get_rec_from_favorites(user_data):

    friend_set = set()
    for friend in user_data['friends']:
        for movie in friend['watched']:
            friend_set.add(movie['title'])


    recomend_movie=[]
    for movie in user_data["favorites"]:
        if movie["title"] not in friend_set:
            recomend_movie.append(movie)

    return recomend_movie 


    
    





