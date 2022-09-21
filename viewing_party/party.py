# ------------- WAVE 1 --------------------

from hashlib import new
from re import M
from collections import Counter

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1, USER_DATA_3


def create_movie(title, genre, rating):
    # for i in range(MOVIE_TITLE_1):
    new_movie = {}
    if title != None and genre != None and rating != None:
        new_movie = {
            "title": MOVIE_TITLE_1,
            "genre": GENRE_1,
            "rating": RATING_1
        }
        return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    for i in movie:
        user_data["watched"] = [
            {
                "title": movie["title"],
                "genre": movie["genre"],
                "rating": movie["rating"]
            }
        ]            
    return user_data
    
def add_to_watchlist(user_data, movie):
    for i in movie:
        user_data["watchlist"] = [
            {
                "title": movie["title"],
                "genre": movie["genre"],
                "rating": movie["rating"]
            }
        ]            
    return user_data

def watch_movie(janes_data, MOVIE_TITLE_1):
    for i in range(len(janes_data["watchlist"])):
        if janes_data["watchlist"][i]["title"] == MOVIE_TITLE_1:
            move_from_watchlist_to_watched = {
                    "title": janes_data["watchlist"][i].pop("title"),
                    "genre": janes_data["watchlist"][i].pop("genre"),
                    "rating": janes_data["watchlist"][i].pop("rating")
                }
            janes_data["watched"].append(move_from_watchlist_to_watched)
        else:
            continue
    janes_data["watchlist"] = list(filter(None, janes_data["watchlist"]))        
    return janes_data

def get_watched_avg_rating(janes_data):
    total_of_all_ratings = 0
    average = 0.0
    if len(janes_data["watched"]) > 0:
        for i in range(len(janes_data["watched"])):
            total_of_all_ratings += janes_data["watched"][i]["rating"]
        average = total_of_all_ratings / len(janes_data["watched"])
    return average

# added import from collections to use Counter() in this function
def get_most_watched_genre(janes_data):
    list_of_genres = []
    dict_of_genres = Counter()
    popular_genre = ""
    if len(janes_data["watched"]) != 0:
        for i in range(len(janes_data["watched"])):
                list_of_genres.append(janes_data["watched"][i]["genre"])
        for genre in list_of_genres:
            if genre not in dict_of_genres:
                dict_of_genres[genre] = 0
            dict_of_genres[genre] +=1
        popular_genre = dict_of_genres.most_common(1)[0][0]
        return popular_genre
    else:
        return None
            
def get_unique_watched(amandas_data):
    # function takes in dict of dicts {"watched":[{}],"friends":[{"watched": [{}]}, {"watched": [{}]} }] }
    amandas_movie_list = [] 
    friends_movie_list = []
    unique_movie_list = []
    j = 0 # iterator
    
    # create list of movie titles (strings) for movies amanda has watched
    for movie in amandas_data["watched"]:
        amandas_movie_list.append(movie)
    
    #create list of movie titles (strings) for movies friends have watched
    for friend in amandas_data["friends"]:
        for watched_movies in amandas_data["friends"][j]["watched"]:
            friends_movie_list.append(watched_movies)
        j += 1
    
    for movie in amandas_movie_list:
        if movie not in friends_movie_list:
            unique_movie_list.append(movie)
    
    return(unique_movie_list)

def get_friends_unique_watched(amandas_data):
    # function takes in dict of dicts {"watched":[{}],"friends":[{"watched": [{}]}, {"watched": [{}]} }] }
    amandas_movie_list = [] 
    friends_movie_list = []
    unique_movie_list = []
    j = 0 # iterator
    
    # create list of movie titles (strings) for movies amanda has watched
    for movie in amandas_data["watched"]:
        amandas_movie_list.append(movie)
    
    #create list of movie titles (strings) for movies friends have watched
    for friend in amandas_data["friends"]:
        for watched_movies in amandas_data["friends"][j]["watched"]:
            friends_movie_list.append(watched_movies)
        j += 1
    
    for movie in friends_movie_list:
        if movie not in amandas_movie_list and movie not in unique_movie_list:
            unique_movie_list.append(movie)
        
    return(unique_movie_list)

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

