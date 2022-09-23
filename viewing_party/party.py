# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating

        return new_movie

def add_to_watched(user_data, movie):
    '''
    user data is a dictionary containing a key "watched" with value []
    "watched" will be a list of dictionaries the user has watched
    '''
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    user data is dictionary containing value "watchlist with value []
    '''
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, MOVIE_TITLE_1):
    '''
    moves movie from user data dictionary w/ watchlist list using movie title -->
    watched list key in same dictionary (an empty list) 
    '''
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == MOVIE_TITLE_1:
            user_data["watched"].append(user_data["watchlist"].pop(i))

        
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
import collections

def get_watched_avg_rating(user_data):
    ratings = []
    if not user_data["watched"]:
        return 0
    for i in user_data["watched"]:
        ratings.append(i["rating"])
        
    return sum(ratings)/len(ratings)

# user_data = {
#     "watched":[
#         {"title": "Anchorman",
#         "genre": "Comedy",
#         "rating": 3},
#         {"title": "Frankenstein",
#         "genre": "Horror",
#         "rating": 5}
#         ]
#     }

# print(get_watched_avg_rating(user_data))
    
def get_most_watched_genre(user_data):
    genres = []
    for i in user_data["watched"]:
        genres.append(i["genre"])
    counter = collections.Counter(genres)
    genre_frequencies = counter.values()

    for genre,frequency in counter.items():
        if frequency == max(genre_frequencies):
            return genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_movies=[]
    friends_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            # for title in movie["title"]
            friends_watched.append(movie["title"])
            print(movie["title"])
    for i in user_data["watched"]:
            if i["title"] not in friends_watched:
                unique_movies.append(i)

    return unique_movies


def get_friends_unique_watched(user_data):
    user_watched = []
    unique_friend_movies = []
    for i in user_data["watched"]:
        user_watched.append(i["title"])

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            # for title in movie["title"]
            if movie["title"] not in user_watched and movie not in unique_friend_movies:
                unique_friend_movies.append(movie)

    return unique_friend_movies
            
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

'''
add movies to recs if user has not watched it, at least one friend has, "host" is in users "subscriptions

utilize friends unique movies as a helper function to get list of users_unwatched_movies
use the movies in this list to access the host of each movie
append to recs list if the host is in subscriptions list (returned as list of movie dictionaries)
return rec list
'''

def get_available_recs(user_data):
    users_unwatched_movies = get_friends_unique_watched(user_data)
    user_recommended_movies = []

    for movie_dict in users_unwatched_movies:
        if movie_dict["host"] in user_data["subscriptions"]:
            user_recommended_movies.append(movie_dict)

    return user_recommended_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    recommendations_by_genre = []
    favorite_genre = get_most_watched_genre(user_data)

    # for i in user_data["watched"]:
    #     genres.append(i["genre"])
    users_unwatched_movies = get_friends_unique_watched(user_data)
        
    for movie_dict in users_unwatched_movies:
        if movie_dict["genre"] == favorite_genre:
            recommendations_by_genre.append(movie_dict)

    return recommendations_by_genre



def get_rec_from_favorites(user_data):
    would_recommend = []

    for movie in user_data["favorites"]:
        if movie in get_unique_watched(user_data):
            would_recommend.append(movie)

    return would_recommend

    
