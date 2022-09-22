# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie_dict
    return None

# -----------------------------------------

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

# -----------------------------------------

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# -----------------------------------------

def watch_movie(user_data, title):
    """ if the movie title is in watched, remove it from watch list"""
def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    # watchlist is a list of multiple dictionaries
    for each_dict in watchlist:
        if title in each_dict.values():
            watched.append(each_dict)
            watchlist.remove(each_dict)
   
    return user_data	

# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    watched = user_data["watched"]
    if len(watched) == 0:
        return 0
    sum_ratings = 0
    count = 0
    for movie in watched:
        sum_ratings += movie["rating"]
        count += 1
    return sum_ratings/count
    
# -----------------------------------------

def get_most_watched_genre(user_data):
    watched = user_data["watched"]
    if len(watched) == 0:
        return None
    genre_dict = {}
    max_score = 0
    max_genre = ""
    for movie in watched:
        genre = movie["genre"]
        if genre not in genre_dict.keys():
            genre_dict[genre] = 1
        else:
            genre_dict[genre] += 1
        if genre_dict[genre] > max_score:
            max_score = genre_dict[genre]
            max_genre = genre
    return max_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    user_watched_list = user_data["watched"]
    friends_watched_list = []
    friends_list=user_data["friends"]
    for friend_data in friends_list:
        watched_list = friend_data["watched"]
        friends_watched_list.extend(watched_list)
    
    return_list = []
    for movie in user_watched_list:
        if movie not in friends_watched_list:
            return_list.append(movie)
    return return_list

# -----------------------------------------

def get_friends_unique_watched(user_data):
    user_watched_list = user_data["watched"]
    friends_watched_list = []
    friends_list=user_data["friends"]
    for friend_data in friends_list:
        watched_list = friend_data["watched"]
        for movie in watched_list:
            if movie not in friends_watched_list:
                friends_watched_list.append(movie)
    #print(user_watched_list)
    #print(friends_watched_list)
    
    return_list = []
    for movie in friends_watched_list:
        if movie not in user_watched_list:
            return_list.append(movie)
    return return_list
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    user_watched_list = user_data["watched"]
    friends_list = user_data["friends"]
    friends_watched_list = []
    recommended_movies_list = []

    #making friends_watched_list_of_unique_movies:
    for friend_data in friends_list:
        for movie in friend_data["watched"]:
            if movie not in friends_watched_list:
                friends_watched_list.append(movie)
    
    #making recommended_movies_list:
    for movie in friends_watched_list:
        if movie not in user_watched_list and movie["host"] in user_data["subscriptions"]:
            recommended_movies_list.append(movie)
    
    #return recommended movies_list:
    return recommended_movies_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    
    friends_list = user_data["friends"]
    friends_watched_list = []
    recommended_movies_list = []
    #making friends_watched_list_of_unique_movies:
    for friend_data in friends_list:
        for movie in friend_data["watched"]:
            if movie not in friends_watched_list:
                friends_watched_list.append(movie)

    # making sure friends watched list is not empty before proceeding
    if len(friends_watched_list) == 0 or len(user_data["watched"]) == 0:
        return recommended_movies_list

    #making a dictionary of genres as keys and frequency as values from user watched movies:
    # to find out most watched genres (genre with highest frequency count)
    user_genre_dict = {}
    most_watched_genre_score = 0
    most_watched_genre = ""
    for movie in user_data["watched"]:
        if movie["genre"] not in user_genre_dict.keys():
            user_genre_dict[movie["genre"]] = 1
        else:
            user_genre_dict[movie["genre"]] += 1
        if user_genre_dict[movie["genre"]] > most_watched_genre_score:
            most_watched_genre_score = user_genre_dict[movie["genre"]]
            most_watched_genre = movie["genre"]
    
    #making recommended movies list based on most watched genre:
    for movie in friends_watched_list:
        if movie not in user_data["watched"] and movie["genre"] == most_watched_genre:
            recommended_movies_list.append(movie)
    
    return recommended_movies_list
# -----------------------------------------

def get_rec_from_favorites(user_data):
    favorite_movies_list = user_data["favorites"]

    friends_list = user_data["friends"]
    friends_watched_list = []
    recommended_movies_list = []
    
    #making friends_watched_list_of_unique_movies:
    for friend_data in friends_list:
        for movie in friend_data["watched"]:
            if movie not in friends_watched_list:
                friends_watched_list.append(movie)
    
    # make a recommended list based on user favorites if none of friends have watched it
    for movie in favorite_movies_list:
        if movie not in friends_watched_list:
            recommended_movies_list.append(movie)

    return recommended_movies_list
# -----------------------------------------    
