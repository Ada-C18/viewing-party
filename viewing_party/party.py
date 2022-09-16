# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    info = [title, genre, rating]
    for movie_info in info:
        if movie_info == None:
            return None
        
    new_movie = {"title": title , "genre": genre , "rating": rating}
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"] = [movie]
    return user_data 

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]
    return user_data 

def watch_movie(user_data, movie):
    for movies in user_data["watchlist"]:
        for label,info in movies.items():
            if label == "title":
                if movie == info:
                    watched_movie = user_data["watchlist"].pop(user_data["watchlist"].index(movies))
                    user_data["watched"].append(watched_movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_watched):
    #putting ratings in a list
    ratings = []
    if user_watched["watched"]:
        for movies in user_watched["watched"]:
            for label,info in movies.items():
                if label == "rating":
                    ratings.append(info)
    else:
        return 0
    #calculating average rating
    total = 0
    for rating in ratings:
        total += rating
    average_rating = total / len(ratings)

    return average_rating

def get_most_watched_genre(user_watched):
    #creating a dictionary to link genre to frequency it appears in watched
    genre_popularity = {}
    if user_watched["watched"]:
        for movies in user_watched["watched"]:
                for label,info in movies.items():
                    if label == "genre":
                        if info in genre_popularity:
                            genre_popularity[info] = genre_popularity[info] + 1
                        else:
                            genre_popularity[info] = 1
        #calculating the max of the values and returning the genre
        most_popular = max(genre_popularity, key=genre_popularity.get)
        return most_popular



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_watched_data):
    #comparing friends movies to user movies and creating a list of duplicates
    user_duplicate_movies = []
    for movies_watched in user_watched_data["watched"]:
        for friends_info in user_watched_data["friends"]:
            for friend,friend_movies in friends_info.items():
                if movies_watched in friend_movies:
                    user_duplicate_movies.append(movies_watched)
    #comparing user movies to duplicates and creating a list of unique movies
    user_unique_movies = []
    for movies_watched in user_watched_data["watched"]:
        if movies_watched not in user_duplicate_movies:
            user_unique_movies.append(movies_watched)
    return user_unique_movies

def get_friends_unique_watched(user_watched_data):
    #comparing friends movies to user movies and adding 
    #unique entries to list
    friend_unique_movies = []
    for friends in user_watched_data["friends"]:
        for friend, friends_movies in friends.items():
            for movies in friends_movies:
                if movies not in user_watched_data["watched"]:
                    friend_unique_movies.append(movies)
    friend_unique_movies_no_duplicates=[]
    #removing the duplicate entry
    for i in range(len(friend_unique_movies)): 
        if friend_unique_movies[i] not in friend_unique_movies[i + 1:]: 
            friend_unique_movies_no_duplicates.append(friend_unique_movies[i])
    return friend_unique_movies_no_duplicates

                    

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

