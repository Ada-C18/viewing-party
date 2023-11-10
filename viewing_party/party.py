# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {"title" :title ,"genre":genre, "rating":rating}
        return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for item in user_data["watchlist"]:
        if item["title"] == title:
            user_data["watchlist"].remove(item)
            user_data["watched"].append(item)
            return user_data
    return user_data 
        
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    avg_rating = 0
    sum_of_rating = 0
    if len(user_data["watched"]) ==0:  
        return 0
    for item in user_data["watched"]:
            sum_of_rating  += item["rating"]
            avg_rating = sum_of_rating /len(user_data["watched"])
    return avg_rating

def get_most_watched_genre(user_data):
    genre_list =[]
    for most_watched in user_data["watched"]:
        genre_list.append(most_watched["genre"])
    if genre_list:
        return max(set(genre_list), key = genre_list.count)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_list =[]
    friends_movie_list=[]
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_movie_list:
                friends_movie_list.append(movie)
    for movie in user_data["watched"]:
        if movie not in friends_movie_list:
            unique_list.append(movie)
    return unique_list

def get_friends_unique_watched(user_data):
    unique_friends_list =[]
    user_movie_list=[]
    for movie in user_data["watched"]:
        if movie not in user_movie_list:
            user_movie_list.append(movie)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_movie_list and movie not in unique_friends_list:
                unique_friends_list.append(movie)
    return unique_friends_list
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movie_list=[]
    unique_watched = get_friends_unique_watched(user_data)
    for movie in unique_watched:
        if movie["host"]in user_data["subscriptions"]:
            recommended_movie_list.append(movie)
    return recommended_movie_list
        
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommended_list = []
    most_watched_genre = get_most_watched_genre(user_data)
    unique_watched = get_friends_unique_watched(user_data)
    
    for movie in unique_watched:
        if movie["genre"] == most_watched_genre:
            recommended_list.append(movie)
    return recommended_list
    
def get_rec_from_favorites(user_data):
    recommended_movie_list = []
    user_unique_movie = get_unique_watched(user_data)
    for user_movie in user_unique_movie:
        if user_movie in user_data["favorites"]:
            recommended_movie_list.append(user_movie)
    return recommended_movie_list