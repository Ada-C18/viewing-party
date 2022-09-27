# ------------- WAVE 1 --------------------
from platform import libc_ver


def create_movie(title, genre, rating):
    new_movie = {}
    if title != None:
        new_movie["title"] = title
        if genre != None:
            new_movie["genre"] = genre
            if rating != None:
                new_movie["rating"] = rating
                return new_movie
            else:
                return None
        else:
            return None
    else:
        return None
            

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if title == user_data["watchlist"][i]["title"]: 
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].pop(i)
            
            return user_data
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) >= 1:
        sum = 0
        for i in range(len(user_data["watched"])):
            sum += user_data["watched"][i]["rating"]
        return sum / len(user_data["watched"])   
    else:
        return 0.0

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) >= 1:
        genre_list = []
        for i in range(len(user_data["watched"])):
            genre_list.append(user_data["watched"][i]["genre"])
        
        counter = 0
        most_frequent_genre = genre_list[0]
        for i in genre_list:
            curr_frequency = genre_list.count(i)
            if(curr_frequency> counter):
                counter = curr_frequency
                most_frequent_genre = i
 
        return most_frequent_genre
    else:
        return None
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    my_movies_watched = []
    for movie in user_data["watched"]:
        my_movies_watched.append(movie)
    
    friend_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.append(movie)

    unique_movies = []

    for movie in my_movies_watched:
        if movie not in friend_movies and movie not in unique_movies:
            unique_movies.append(movie)
        
    return unique_movies

def get_friends_unique_watched(user_data):
    my_movies_watched = []
    for movie in user_data["watched"]:
        my_movies_watched.append(movie)
    
    friend_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.append(movie)

    unique_movies = []

    for movie in friend_movies:
        if movie not in my_movies_watched and movie not in unique_movies:
            unique_movies.append(movie)
        
    return unique_movies
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies = []
    my_movies_watched = []
    for movie in user_data["watched"]:
        my_movies_watched.append(movie)
    
    friend_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.append(movie)
    
    for movie in friend_movies:
        if movie not in my_movies_watched and movie not in recommended_movies:
            if movie["host"] in user_data["subscriptions"]:
                recommended_movies.append(movie)

    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    my_movies_watched = []
    for movie in user_data["watched"]:
        my_movies_watched.append(movie)
    
    friend_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.append(movie)

    recommended_by_genre = []

    user_popular_genre = get_most_watched_genre(user_data)
    for movie in friend_movies:
        if movie["genre"] == user_popular_genre:
            if movie not in my_movies_watched and movie not in recommended_by_genre:
                recommended_by_genre.append(movie)

    return recommended_by_genre

def get_rec_from_favorites(user_data):
    friend_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.append(movie)
    from_favorite_recommendation = []
    for movie in user_data["favorites"]:
        if movie not in friend_movies and movie not in from_favorite_recommendation:
            from_favorite_recommendation.append(movie)
            
    return from_favorite_recommendation
