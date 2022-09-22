# ------------- WAVE 1 --------------------
from pickletools import read_stringnl_noescape


def create_movie(movie_title, genre, rating):
    if not movie_title or not genre or not rating:
        return None
    new_movie = {
        "title" : movie_title,
        "genre": genre,
        "rating" : rating
        }
    return new_movie

def add_to_watched(user_data, movie):

    # Create an empty dictionary with user data
    user_data = {}

    # Create an empty list with watched movies.  Append watched movies.
    watched_list= []
    watched_list.append(movie)

    # They key "watched" in the user_data dictionary is assigned the value of the watched movies.
    user_data["watched"] = watched_list
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {}
    watch_list= []
    watch_list.append(movie)
    user_data["watchlist"] = watch_list
    return user_data

def watch_movie (user_data, title):

    for i in range(len(user_data["watchlist"])):
        if title == user_data["watchlist"][i]["title"]:
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].remove(user_data["watchlist"][i])
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    movie_rating = 0

    for i in range(len(user_data["watched"])):
        movie = user_data["watched"][i]
        temp_rating = movie["rating"]

        movie_rating += temp_rating 
    
    if len(user_data["watched"]) == 0:
        return 0.0

    else:
        return movie_rating / len(user_data["watched"])
        
    
def get_most_watched_genre(user_data):
    list_of_genres = []
    
    for i in range(len(user_data["watched"])):
        movie_genre = user_data["watched"][i]["genre"]
        list_of_genres.append(movie_genre)

    if len(user_data["watched"]) == 0:
        return None  
    else:
        most_watched = max(list_of_genres, key = list_of_genres.count)
        return most_watched 
    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    user_same_list = [] 
    unique_list = []

    for i in range (len(user_data["friends"])): # Loops through each friend list
        for movie in range (len(user_data["friends"][i]["watched"])): # Loops through each friend's nested movie list
            friend_movie = user_data["friends"][i]["watched"][movie]
            if friend_movie in user_data["watched"]:
                user_same_list.append(friend_movie)

    for i in range(len(user_data["watched"])):
        if user_data["watched"][i] not in user_same_list:
            unique_list.append(user_data["watched"][i])

    return unique_list

def get_friends_unique_watched(user_data):

    friends_unique_list = []

    for i in range (len(user_data["friends"])): 
        for movie in range (len(user_data["friends"][i]["watched"])):
            friend_movie = user_data["friends"][i]["watched"][movie]
            if friend_movie not in user_data["watched"] and friend_movie not in friends_unique_list:
                    friends_unique_list.append(friend_movie)

    return friends_unique_list

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):

    recommended_list = []

    for i in range (len(user_data["friends"])): 
        for movie in range (len(user_data["friends"][i]["watched"])): 
                friend_movie = user_data["friends"][i]["watched"][movie]
                friend_host = friend_movie["host"]
                friends_unique_list = get_friends_unique_watched(user_data)

                if friend_host in user_data["subscriptions"] and friend_movie in friends_unique_list:
                    recommended_list.append(user_data["friends"][i]["watched"][movie])
    
    return recommended_list
                    


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    
    recommended_list = []

    if len(user_data["watched"])>0:
        user_genre = user_data["watched"][0]["genre"]

    else:
        user_genre = None 

    for i in range (len(user_data["friends"])): 
        for movie in range (len(user_data["friends"][i]["watched"])): 
            friend_movie = user_data["friends"][i]["watched"][movie]
            friend_genre = friend_movie["genre"]
            friends_unique_list = get_friends_unique_watched(user_data)
    
            if friend_genre == user_genre and friend_movie in friends_unique_list:
                recommended_list.append(user_data["friends"][i]["watched"][movie])
            
    return recommended_list

def get_rec_from_favorites(user_data):

    fav_recs =[]

    for i in range (len(user_data["favorites"])):
        user_unique_list = get_unique_watched(user_data)
        movie = user_data["favorites"][i]
        if movie in user_unique_list:
            fav_recs.append(movie)

    return fav_recs