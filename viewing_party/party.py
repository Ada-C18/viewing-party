# ------------- WAVE 1 --------------------

from __future__ import unicode_literals


def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating,
    }
    return movie
def add_to_watched(user_data, movie):
    updated_data = user_data.copy()
    updated_data["watched"].append(movie)
    return updated_data
def add_to_watchlist(user_data, movie):
    updated_data = user_data.copy()
    updated_data["watchlist"].append(movie)
    return updated_data
def watch_movie(user_data, title):
   

    watchlist = user_data["watchlist"] 
    watched =user_data["watched"]
   

    for movie in watchlist:
        if movie["title"] == title:
            watched.append(movie)
            watchlist.remove(movie)
             
    
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    # represents that the user has a list of watched movies 
    if not user_data["watched"]:
        return 0.0
    # Adding if statement for test 2.2 above
    rating_list = []
    for movie in user_data["watched"]:
        if movie["rating"]>0:
            rating_list.append(movie["rating"])
    rating_sum = sum(rating_list)
    avg_rating = rating_sum/len(rating_list)
    
    
    return avg_rating
# 

    # create genre value (what we want going into the dictionary)
    # 
def get_most_watched_genre(user_data):    
    genre_count = {}
    u = user_data["watched"] 
    if len(u)>0:
        for i in range(len(u)):
            genre = user_data["watched"][i]["genre"]
            # if genre is in genre count (if the key is in the dictionary)
            if genre in genre_count:
                genre_count[genre] +=1
            else:
                genre_count[genre] =1
        return max(genre_count, key = genre_count.get)
    
    else:
        return None 






    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_friends_movies(user_data):
    unique_watched = []
    friends_watched_list_of_dicts = user_data["friends"]

    for index in range(len(friends_watched_list_of_dicts)):
        for index_2 in range(len(friends_watched_list_of_dicts[index]["watched"])):
            unique_watched.append(friends_watched_list_of_dicts[index]["watched"][index_2])
    return unique_watched

def get_unique_watched(user_data):
    unique_movies = []
    user_watched_list = user_data["watched"]
    friends_watched_list = get_friends_movies(user_data)

    for index in range(len(user_watched_list)):
        if not user_watched_list[index] in friends_watched_list:
            unique_movies.append(user_watched_list[index])

    return unique_movies
def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    friends_watched_list = get_friends_movies(user_data)
    user_watched_list = user_data["watched"]

    for movie in friends_watched_list:
        if movie not in user_watched_list and movie not in friends_unique_movies:
            friends_unique_movies.append(movie)
        

    return friends_unique_movies

################################################################


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended = []   
    subscriptions = user_data["subscriptions"]
    movies_we_have_watched = user_data["watched"]
    print(subscriptions)
    friends = user_data["friends"]
    # print(user_data["friends"])

    for friend in friends:
        for movie in friend["watched"]:
            print(movie)
            if (movie not in movies_we_have_watched) and (movie["host"] in subscriptions):
                recommended.append(movie)


    return recommended






# def get_friends_unique_watched(user_data)
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


    

def get_new_rec_by_genre(user_data):
    recommended_list = []
    max_genre = get_most_watched_genre(user_data) 
    friends_watched = get_friends_unique_watched(user_data)

    for movie in friends_watched:
        if movie["genre"] == max_genre: 
            recommended_list.append(movie)
    

    return recommended_list

def get_rec_from_favorites(user_data):
    user_favorites = []
    friends_watched = []

    for friends in user_data["friends"]:
        for movie in friends["watched"]:
            friends_watched.append(movie)

    for movie in user_data["favorites"]:
        if movie not in friends_watched:
            user_favorites.append(movie)

    return user_favorites

