# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie = {}
    if title and genre and rating: 
        movie["title"] = title
        movie["genre"] = genre 
        movie["rating"] = rating 
        return movie


def add_to_watched(user_data, movie):
    user_data = {}
    user_data["watched"] = [movie]
    return user_data


def add_to_watchlist(user_data, movie):
    user_data = {}
    user_data["watchlist"] = [movie]
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:    
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data['watched'].append(movie)
            # return user_data
        
    return user_data  
# # -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_list = []
    for i in range(len(user_data["watched"])):
        rating_list.append(user_data["watched"][i]["rating"])
    # if len(rating_list) != 0:
    if rating_list:
        average = sum(rating_list)/len(rating_list)
    else:
        average = 0.0
    return average 


def get_most_watched_genre(user_data):
    genre_list = []
    for i in range(len(user_data["watched"])):
        genre_list.append(user_data["watched"][i]["genre"])
    if genre_list: 
        for genre in genre_list:
            popular_genre = max(set(genre_list), key = genre_list.count)
    else: 
        popular_genre = None 
    return popular_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data): 
    friends_watched_list = []
    unique_watched_list = []
    friends = user_data["friends"]
    # maybe get rid of this variable later.. don't think you need it!! 
    user_watched = user_data["watched"]
    
    for friend in friends:
        for movie in friend["watched"]:
            friends_watched_list.append(movie["title"])
    
    for movie in user_watched:
        if movie["title"] not in friends_watched_list:  
            unique_watched_list.append(movie)
    
    return unique_watched_list


def get_friends_unique_watched(user_data):
    friends_unique_watched_list = []
    user_list = []
    friends_unique = []
    friends = user_data["friends"]
    user_watched = user_data["watched"]

    for movie in user_watched:
        user_list.append(movie["title"])
    
    for friend in friends:
        for movie in friend["watched"]:
            if movie["title"] not in user_list: 
                friends_unique_watched_list.append(movie)
    
    for i in range(len(friends_unique_watched_list)):
        if friends_unique_watched_list[i] not in friends_unique_watched_list[i + 1:]:
            friends_unique.append(friends_unique_watched_list[i])

    return friends_unique
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friend_recs = []
    final_recs = []
    user_watched_list = [movies for movies in user_data["watched"]]
    
    for movie in user_data["friends"]:
        for title in movie["watched"]:
            if title not in user_watched_list:
                if title not in friend_recs:
                    friend_recs.append(title)
    
    for movie in friend_recs:
        if movie["host"] in user_data["subscriptions"]:
            final_recs.append(movie)
    
    return final_recs
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

