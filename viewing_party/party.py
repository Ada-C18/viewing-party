# ------------- WAVE 1 --------------------

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
    user_data = {}
    watched_list= []
    watched_list.append(movie)
    user_data["watched"] = watched_list
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {}
    watch_list= []
    watch_list.append(movie)
    user_data["watchlist"] = watch_list
    return user_data

def watch_movie (user_data, title):
    if title in user_data["watchlist"][-1]['title']:
        user_data["watched"].append(user_data["watchlist"][-1])
        user_data["watchlist"].remove(user_data["watchlist"][-1])
    return user_data
        
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):

    movie_ratings = []

    for movie in user_data["watched"]:
        movie_ratings.append(movie["rating"])
    if len(movie_ratings)==0:
        return 0.0
    else:
        average = sum(movie_ratings)/len(movie_ratings)
    
    return average

def get_most_watched_genre(user_data):
    movie_genre = []
    popular_genre={}

    if len(user_data["watched"]) >0:
    
        for movie in user_data["watched"]:
            popular_genre[movie["genre"]]=0
            movie_genre.append(movie["genre"])

        for genre in movie_genre:
            if genre in popular_genre:
                popular_genre[genre]+=1

        most_popular_genre = max(popular_genre, key=popular_genre.get)

        return most_popular_genre
        
    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def helper_function_friend (user_data):
    friend_list =[]

    for friend_data in user_data["friends"]:
        for friend in friend_data["watched"]:
            friend_list.append(friend)
    return friend_list

def get_unique_watched(user_data):
    user_list = []
    friend_list =[]

    user_watched = user_data["watched"]
    for movie in user_watched:
        user_list.append(movie)

    friend_data = helper_function_friend(user_data)
    
    for movie in friend_data:
        if movie in user_list:
            user_list.remove(movie)
    return user_list  


def get_friends_unique_watched(user_data):
    user_list = []
    unique_list = []

    user_watched = user_data["watched"]
    for movie in user_watched:
        user_list.append(movie)

    friend_data = helper_function_friend(user_data)

    for movie in friend_data:
        if movie not in user_list and movie not in unique_list :
            unique_list.append(movie)
    return unique_list



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):
    
    recommendation_list = []

    #passing in last function as a helper function :) 
    friend_unique_watched = get_friends_unique_watched(user_data)

    for movie_host in friend_unique_watched:
        if movie_host["host"] in user_data["subscriptions"]:
            recommendation_list.append(movie_host)
    return recommendation_list
    

# -----------------------------------------
# ------------- WAVE 5--------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    
    genre_list = []
    max_genre = get_most_watched_genre(user_data)  
    friend_unique_watched = get_friends_unique_watched(user_data)

    for movie in friend_unique_watched:
        if movie["genre"] == max_genre: 
            genre_list.append(movie)
    return genre_list


def get_rec_from_favorites(user_data): 

    user_list = []
    recommended_list = []

    user_watched = user_data["watched"]
    for movie in user_watched:
        user_list.append(movie)

    friend_data = helper_function_friend(user_data)

    for movie in user_data["favorites"]:
        if movie not in friend_data:
            recommended_list.append(movie)
    return recommended_list




