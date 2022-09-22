# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    
    return movie    

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    
    for i in range(len(watchlist)):
        if watchlist[i]["title"] == title:
            watched.append(watchlist[i])
            watchlist.remove(watchlist[i])
        
    return user_data
            

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    rating_sum = 0
    average = 0
    count = 0

    for movie in user_data["watched"]:
        rating_sum += movie["rating"]
        count += 1
        
        if count == 0:
            average = 0.0
        else: 
            average = rating_sum / count
        
    return average

def get_most_watched_genre(user_data):
    genre_count = {}
    popular_genre = ""

    for movie in user_data["watched"]:
        if movie["genre"] not in genre_count:
            genre_count[movie["genre"]] = 1
        else:
            genre_count[movie["genre"]] += 1

    for key, value in genre_count.items():
        if value == max(genre_count.values()):
            popular_genre = key
    
    if len(genre_count) == 0:
        popular_genre = None    
        
    return popular_genre


    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    only_user_watched =[]
    
    for movie in user_data["watched"]:
        if movie not in user_data["friends"][0]["watched"] and movie not in user_data["friends"][1]["watched"]:
            only_user_watched.append(movie)
    
    return only_user_watched

def get_friends_unique_watched(user_data):
    only_friends_watched = []
    updated_only_friends_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"]:
                only_friends_watched.append(movie)
            
    for i in only_friends_watched: 
        if i not in updated_only_friends_watched: 
            updated_only_friends_watched.append(i)    
    
    return updated_only_friends_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    # call helper fx
    updated_only_friends_watched = get_friends_unique_watched(user_data)
    rec_list = []
    
    for movie in updated_only_friends_watched:
        if movie not in user_data["watched"]and movie["host"] in user_data["subscriptions"]:
            rec_list.append(movie) 

    return rec_list


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    only_friends_watched = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)
    rec_list = []

    for movie in only_friends_watched:
        if movie not in user_data["watched"] and movie["genre"] == most_watched_genre:
            rec_list.append(movie)        
    
    return rec_list

def get_rec_from_favorites(user_data):
    rec_list = []

    for movie in user_data["favorites"]:
        is_in_watched_list = False
        
        for friend in user_data["friends"]: 
            if movie in friend["watched"]:
                is_in_watched_list = True  
        if is_in_watched_list == False: 
            rec_list.append(movie)
            
    return rec_list