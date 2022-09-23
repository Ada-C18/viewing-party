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
#----- Extra helper function to get friends_watched_list ----
def get_friends_watched_list(user_data):
    friends_watched_list = []
    for friend in user_data["friends"]:
            for movie in friend["watched"]:
                friends_watched_list.append(movie["title"])
    return friends_watched_list


def get_unique_watched(user_data): 
    friends_watched_list = get_friends_watched_list(user_data)
    unique_watched_list = []
    
    for movie in user_data["watched"]:
        if movie["title"] not in friends_watched_list:  
            unique_watched_list.append(movie)
    
    return unique_watched_list


def get_friends_unique_watched(user_data):
    friends_unique_watched_list = []
    user_list = []
    friends_unique_movies = []
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
            friends_unique_movies.append(friends_unique_watched_list[i])

    return friends_unique_movies
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
def get_new_rec_by_genre(user_data):
    friends_recs = []
    movie_recs_by_genre = []
    favorite_genre = get_most_watched_genre(user_data)
    user_watched_list = [movies for movies in user_data["watched"]]
    
    for movie in user_data["friends"]:
        for title in movie["watched"]:
            if title not in user_watched_list:
                friends_recs.append(title)
    
    for movie in friends_recs:
        if movie["genre"] == favorite_genre:
            movie_recs_by_genre.append(movie)
    
    return movie_recs_by_genre 

def get_rec_from_favorites(user_data):
    friends_watched = []
    recs_from_favs = []
    user_favs = [movies for movies in user_data["favorites"]]
    
    for movies in user_data["friends"]:
        for title in movies["watched"]:
            friends_watched.append(title)
    
    for movie in user_favs: 
        if movie not in friends_watched: 
            recs_from_favs.append(movie)
    
    return recs_from_favs
