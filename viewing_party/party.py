# ------------- WAVE 1 --------------------
from curses import keyname
from re import A

'''
Create movie within dictionary with title, genre, rating as key.
'''

def create_movie(title, genre, rating):   
    movie = {}
    if not title or not genre or not rating:
        return None
    else:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie

'''
Add movie to watched in user_data.
'''

def add_to_watched(user_data, movie):  
    user_data["watched"].append(movie)
    return user_data

'''
Add movie to watchlist in user_data.
'''

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

'''
Remove movie from watchlist and add to watched if title matches element in watchlist; 
Otherwise return user_data.
'''

def watch_movie (user_data, title):    
    for movie in user_data["watchlist"]:
        if title in movie["title"]:
        #remove from list, can also use list.pop(list.index(movie))
            user_data["watchlist"].remove(movie)                
        #add_to_watched(user_data, title)
            user_data["watched"].append(movie)
            return user_data
    else:
        return user_data   


# ------------- WAVE 2 --------------------

'''
Calculate avg. rating of all movie in wached list from user_data.
'''

def get_watched_avg_rating(user_data):
    
    sum_rating = 0.0
    watched_length = len(user_data["watched"])
    # access movie rating - user_data["watched"][0]["rating"] 
    if watched_length > 0:
        for movie in user_data["watched"]:
            sum_rating += movie["rating"]
        return sum_rating / watched_length
    else:
        return 0.0

'''
Get movie name of most watched genre from user_data.
'''

def get_most_watched_genre(user_data):
    # access movie genre - user_data["watched"][0]["genre"] 
    
    # create dict {}, genre : count, add to count if exsit, add key pair if non exsit; 
    # get max value from dict and return the key
    # if "watched" is empty, return None
    genre_count = { }
    watched_length = len(user_data["watched"])
    if watched_length > 0:
        for movie in user_data["watched"]:
            # or append to a set of genre??
            # if genre do not exsit in genre_count as dictionary key
            if movie["genre"] not in genre_count.keys():
                #add key value pair
                genre_count[movie["genre"]] = 1
            else:    
                # key: add +1 to value
                genre_count[movie["genre"]] += 1       
        #get max from genre_count
        return max(genre_count, key=genre_count.get)
    else:
        return None 


# ------------- WAVE 3 -------------------- 
# HELPER FUNCTION!
# set options???
'''
Return a list that determines which movies the user has watched but none of their friends have watched.
'''

def get_unique_watched(user_data):
     
    # access user movie - user_data["watched"]["title"]
    # user_data["friends"][i]["watched"] -> list of movie
    # list of dictionary to save user's unique movies
    user_unique_watched =[ ] 
    # get movies from all friends 
    all_friends_movies = [ ]
    
    for i in range (0, len(user_data["friends"])):
        all_friends_movies.extend(user_data["friends"][i]["watched"])
    
    for movie in user_data["watched"]:
        # if user movie title in friend's, continue?
        if movie in all_friends_movies:
            continue
        # else (not in friends), append 
        else:
            user_unique_watched.append(movie)
    return user_unique_watched
    

'''
Return a list that determines which movies one of the friends watched but user didnt.
'''

def get_friends_unique_watched(user_data):

    # get unique movies from friends
    friends_unique_movies = []
    # get movies from all friends 
    all_friends_movies = []
    for i in range (0, len(user_data["friends"])):
        all_friends_movies.extend(user_data["friends"][i]["watched"])
    for friend_movie in all_friends_movies:
            # if friend movie title in user, continue
            if friend_movie in user_data["watched"]:
                continue
        # else (not in user), append 
            else:
            #elif friend_movie not in user_data["friends"] and friends_unique_movies: ?? why doesnt work
                if friend_movie not in friends_unique_movies:
                    friends_unique_movies.append(friend_movie)
    return friends_unique_movies    

# ------------- WAVE 4 --------------------

'''
Get a list of recs_movie, on top of condition from friends_unique_movies in Wave 3, check if user has matching subscription.
'''

def get_available_recs(user_data):
    recs_movie = []
    friends_unique_movies = get_friends_unique_watched(user_data)
    for i in range (len(friends_unique_movies)):
        if friends_unique_movies[i]["host"] in user_data["subscriptions"]:
            recs_movie.append(friends_unique_movies[i])        
    return recs_movie       

# ------------- WAVE 5 --------------------

'''
Get a list of recs_movie, on top of condition from friends_unique_movies() in Wave 3, check if genre matches max genre using Wave 2.
'''

def get_new_rec_by_genre(user_data):
    recs_movie = []
    max_genre_movie = get_most_watched_genre(user_data)
    friends_unique_movies = get_friends_unique_watched(user_data)
    for i in range(len(friends_unique_movies)):
        if friends_unique_movies[i]["genre"] == max_genre_movie:
            recs_movie.append(friends_unique_movies[i]) 
    return recs_movie

'''
Get a list of recs_movie, on top of condition from get_unique_watched() in Wave 3, check if movie in user favorites list.
'''

def get_rec_from_favorites(user_data):
    recs_movie =[]
    user_unique_watched = get_unique_watched(user_data)
    for i in range(len(user_unique_watched)):
        if user_unique_watched[i] in user_data["favorites"]:
            recs_movie.append(user_unique_watched[i]) 
    return recs_movie
