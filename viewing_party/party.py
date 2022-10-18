# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
            
    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating
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
            movie_index = user_data["watchlist"].index(movie) 
            user_data["watchlist"].pop(movie_index) 
            user_data["watched"].append(movie)
    
    return user_data 

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data): 

    total = 0
    if len(user_data["watched"]) == 0:
        return total
    for movie in user_data["watched"]:
        total += movie["rating"]
    
    average = total / len(user_data["watched"]) 

    return average

def get_most_watched_genre(user_data): 

    if len(user_data["watched"]) == 0:
            return None

    genre_count = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_count.keys():
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1
    
    max_genre_count = 0
    most_watched_genre = ""
    for genre, count in genre_count.items():
        if count > max_genre_count:
            max_genre_count = count
            most_watched_genre = genre
    
    return most_watched_genre  
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):

    friends_watched_list = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched_list: 
                friends_watched_list.append(movie)
    
    user_unique_movies = []

    for movie in user_data["watched"]: 
        if movie not in friends_watched_list:
            user_unique_movies.append(movie) 
    
    return user_unique_movies 

def get_friends_unique_watched(user_data):

    friends_watched_list = []
    friends_unique_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_watched_list:
                friends_watched_list.append(movie)
            
    for movie in friends_watched_list:
        if movie not in user_data["watched"]: 
            friends_unique_movies.append(movie) 
    
    return friends_unique_movies

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friends_unique_watched = get_friends_unique_watched(user_data)

    friends_recs =[] 

    for movie in friends_unique_watched:
        if movie["host"] in user_data["subscriptions"]:
            friends_recs.append(movie) 

    return friends_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data): 
    
    recs_by_genre = [] 

    fav_genre = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)

    for movie in friends_unique_watched:
        if movie["genre"] == fav_genre: 
            recs_by_genre.append(movie) 

    return recs_by_genre


def get_rec_from_favorites(user_data): 
    
    favs = [] 

    for movie in user_data["favorites"]:
        favs.append(movie)
        
    for movie in user_data["friends"]:
        for movie in movie["watched"]:
            if movie in favs: 
                favs.remove(movie)
    
    return favs 




