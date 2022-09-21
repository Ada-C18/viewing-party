# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {
        "title": title, "genre": genre, "rating": rating
    }
    movie_info = [title, genre, rating]
    
    if None in movie_info:
        return None
    else:
        return movie_dict
    
    
def add_to_watched(user_data, movie):
    user_data = {
        "watched": [movie]
    }
    return user_data


def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist": [movie]
    }
    return user_data 


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if len(user_data['watched']) == 0:
        return 0.0 
    
    rating = 0
    movie_rating_list = []
    
    for movie in user_data["watched"]:
        movie_rating = movie["rating"]
        rating += movie_rating 
        movie_rating_list.append(movie["rating"])
        average_rating = rating / len(movie_rating_list)
    return average_rating


def get_most_watched_genre(user_data):
    if len(user_data['watched']) == 0:
        return None
    
    movie_genre_dict = {}
    max_count = 0
    most_watched_genre = ""
    
    for movie in user_data["watched"]:
        movie_genre = movie["genre"]
        
        if movie_genre not in movie_genre_dict:
            movie_genre_dict[movie_genre] = 1
        else:
            movie_genre_dict[movie_genre] += 1
    
    for genre, count in movie_genre_dict.items():
        if count > max_count:
            max_count = count
            most_watched_genre = genre 
    
    return most_watched_genre
    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    friends_watched_list = []    
    unique_list_of_dicts = []
    friends = user_data["friends"]
    user_watched = user_data["watched"]
        
    for friend in friends:
        for movie in friend["watched"]:
            friends_watched_list.append(movie["title"])
                
    for movie in user_watched:
        if movie["title"] not in friends_watched_list:
            unique_list_of_dicts.append(movie)
        
    return unique_list_of_dicts 


def get_friends_unique_watched(user_data):
    friends_watched_list = []
    unique_friends_movies = []
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched_list:
                friends_watched_list.append(movie)
                
    for movie in friends_watched_list:
        if movie not in user_data["watched"]:
            unique_friends_movies.append(movie)
            
    return unique_friends_movies
            

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    user_subscriptions = [] 
    recommended_movies = []
    
    # get user list of subscriptions
    for sub in user_data["subscriptions"]:
        user_subscriptions.append(sub)  
        
    # use unique friend's function, list of movie dicts
    friends_unique = get_friends_unique_watched(user_data)
    for movie in friends_unique:
        if movie["host"] in user_subscriptions:
            recommended_movies.append(movie)
    
    # return list of recommended movies 
    return recommended_movies
                    
    
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    recommended_movies = []
    fav_genre = get_most_watched_genre(user_data)
    
    # unique friend's function, returns list of movie dicts
    friends_unique = get_friends_unique_watched(user_data)
    for movie in friends_unique:
        if movie["genre"] == fav_genre:
            recommended_movies.append(movie)
    
    return recommended_movies 


def get_rec_from_favorites(user_data):
    recommended_movies = []
    user_watched = get_unique_watched(user_data)
    
    # determine users favs
    for movie in user_data['favorites']:
        if movie in user_watched:
            recommended_movies.append(movie)
        
    return recommended_movies

# NEED TO WRITE ASSERT 