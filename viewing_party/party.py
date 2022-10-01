# ------------- WAVE 1 --------------------

#from tests.test_constants import MOVIE_TITLE_1


def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None: 
        return None
    
    movie = {
        'title': title,
        'genre': genre, 
        'rating': rating,

    }
    return movie

def add_to_watched(user_data, movie):
    #user_data["title"] = movie
    user_data["watched"].append(movie)
    return user_data
    
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):

    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):

    rating_sum = 0 #4.8,8.8

    if len(user_data["watched"]) == 0:
        return 0

    for movie in user_data["watched"]:
        rating_sum += (movie["rating"])

    average_rating = rating_sum / len(user_data["watched"])
#averge rating 0.8
    return average_rating

        
def get_most_watched_genre(user_data):
    genre = {}
    if user_data["watched"] == []:
        return None

    for movie in user_data["watched"]:
        current_movie_genre = movie["genre"]
        if current_movie_genre not in genre:
            genre[current_movie_genre] = 1
        else:
            genre[current_movie_genre] += 1
    
    most_views = 0
    most_viewed_genre = ""
    for x in genre:
        if genre[x] > most_views:
            most_views = genre[x]
            most_viewed_genre = x
    return most_viewed_genre





# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friend_movie_common = []
    unique_movies = []
    # user_movie_list = []

    for i in range (len(user_data["friends"])):

        for j in range (len(user_data["friends"][i]["watched"])):
            friend_movie = user_data["friends"][i]["watched"][j]
            if friend_movie in user_data["watched"]:
                friend_movie_common.append(friend_movie)
            # if user_data["watched"] not in friend_movie:
    for l in range(len(user_data["watched"])):
        if user_data["watched"][l] not in friend_movie_common:
            unique_movies.append(user_data["watched"][l])

    return unique_movies

def get_friends_unique_watched(user_data):
    friend_unique_list = []

    for i in range (len(user_data["friends"])):

        for j in range (len(user_data["friends"][i]["watched"])):
            friend_movie = user_data["friends"][i]["watched"][j]
            if friend_movie not in user_data["watched"] and friend_movie not in friend_unique_list:
                friend_unique_list.append(friend_movie)
    return friend_unique_list



        
    




# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# 1. Create a function named `get_available_recs`. This function should...
# - take one parameter: `user_data`

def get_available_recs(user_data):
    friends_unique_movies = get_friends_unique_watched(user_data)
    rec_movies = []
    for movies in friends_unique_movies:
        if movies['host'] in user_data['subscriptions'] and movies not in user_data["watched"]:
            rec_movies.append(movies)
            
    return rec_movies



        
        #friends movies - user movie and host in user sub= rec movies
        
    

# def get_friend_movie_list(user_data):
#     friend_movie_list = []
#     for i in range(len(user_data["friends"])):
#         for j in range (len(user_data["friends"][i]["watched"])):
#             friend_movie = user_data["friends"][i]["watched"][j]
#             friend_movie_list.append(friend_movie) 
            
            
# def get_user_movie_list(user_data):
#     user_movie_list = []
#     for i in range (len(user_data["watched"])):
#         user_movie = user_data["watched"][i]
#         user_movie_list += user_movie_list.append(user_movie) 

# def get_available_recs(user_data):
#     recommended_movies = []
#     for movie in get_friend_movie_list(user_data):
#         if movie not in get_user_movie_list(user_data) and get_friend_movie_list["host"] == user_data["subscriptions"]:
#             recommended_movies.append(movie)

            #if movie not in user_movie_list and in friend_movie_list:
            #if user_data["subscriptions"] == friend_movie_list["host"]:
#user_data ---- subscriptions (list of strings (streaming service))
#friend---- friends ----watched list - movie - host
#   - `user_data` will have a field `"subscriptions"`. The value of `"subscriptions"` is a list of strings
#     - This represents the names of streaming services that the user has access to
#     - Each friend in `"friends"` has a watched list. Each movie in the watched list has a `"host"`,
#  which is a string that says what streaming service it's hosted on
# - Determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"host"` of the movie is a service that is in the user's `"subscriptions"`
# - Return the list of recommended movies
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    rec_list = []
    user_genre = get_most_watched_genre(user_data)
    friends_unique_movies = get_friends_unique_watched(user_data)

    for movies in friends_unique_movies:
        if movies['genre'] == user_genre:
            rec_list.append(movies)
    
    return rec_list

def get_rec_from_favorites(user_data):
    fav_rec_list = []
    friends_unique_movies = get_friends_unique_watched(user_data)

    for movie in get_unique_watched(user_data):
        if movie not in friends_unique_movies:
            fav_rec_list.append(movie)
    print(fav_rec_list)
    return fav_rec_list
    

    




    #friends watched - user watched and genre == user_genre

