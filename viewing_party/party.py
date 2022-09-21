# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    if title == None or genre == None or rating == None:
        return None
    else:
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    avg_rating = 0
    for i in range(len(user_data["watched"])):
        avg_rating += user_data["watched"][i]["rating"]
    if len(user_data["watched"]) == 0:
        return avg_rating
    avg_rating /= len(user_data["watched"])
    return avg_rating

def get_most_watched_genre(user_data):
    fav_genre = ""
    genre_dict = {}
    i = 0
    if len(user_data["watched"]) == 0:
        return None
    for key, value in user_data["watched"][i].items():
        if key == "genre":
            if value in genre_dict:
                genre_dict[value] += 1
            else:
                genre_dict[value] = 1
        i += 1
    for key, value in genre_dict.items():
        if value > 0:
            fav_genre = key
    return fav_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

#returns unique movies that user has watched, but friends have not
def get_unique_watched(user_data):
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

#returns what friends have watched, but user has not
def get_friends_unique_watched(user_data):
    unique_watched_list = []

    friend_watched_set = set(get_friends_watched(user_data))
    user_watched_set = set(get_users_watched(user_data))

    unique_set = friend_watched_set - user_watched_set
    
    for i in range(len(user_data["friends"])):
        for watched in user_data["friends"][i]:
            for movie in user_data["friends"][i][watched]:
                    if movie["title"] in unique_set:
                        if movie["title"] not in unique_watched_list:
                            unique_watched_list.append(movie) 

    for x in range(len(unique_watched_list)):
        if unique_watched_list[x-1]["title"] == unique_watched_list[x]["title"]:
            del unique_watched_list[x] 

    return unique_watched_list 

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    available_recs = []
    movies_friends_watched = get_friends_unique_watched(user_data)
    for movie in movies_friends_watched:
        if movie["host"] in user_data["subscriptions"]:
            available_recs.append(movie)
    return available_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

