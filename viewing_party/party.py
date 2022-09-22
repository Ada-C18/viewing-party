# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    """creates and returns a movie (of type dictionary) if all given inputs are truthy, otherwise returns None"""
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
    """adds given movie to the "watchlist" list inside of user_data"""
    user_data["watched"].append(movie)
    return user_data

# -----------------------------------------

def add_to_watchlist(user_data, movie):
    """adds given movie to the "watchlist" list inside of user_data"""
    user_data["watchlist"].append(movie)
    return user_data

# -----------------------------------------

def watch_movie(user_data, title):
    """moves the movie of given title from 'watchlist' to 'watched' list inside of user_data"""

    watchlist = user_data["watchlist"]
    watched = user_data["watched"]
    # watchlist is a list of movie, each movie is of type dictionary
    # to remove given movie from watchlist, iterating over watchlist 
    for movie in watchlist:
        if title in movie.values():
            watched.append(movie) #appending the movie to watched before removing from watchlist
            watchlist.remove(movie) 
   
    return user_data	

# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    """returns average movie rating for watched movies"""
    watched = user_data["watched"]
    #if there are no movies in 'watched' in user_data, returns 0 
    if len(watched) == 0:
        return 0
    sum_ratings = 0
    count = 0

    # computing average rating:
    for movie in watched:
        sum_ratings += movie["rating"]
        count += 1
    return sum_ratings/count
    
# -----------------------------------------

def get_most_watched_genre(user_data):
    """returns the most watched movie genre"""
    watched = user_data["watched"]
    if len(watched) == 0:
        return None
    
    #using a genre dictionary with genre as the key and frequency as value
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
    """returns movies that the user has watched, but none of their friends have watched"""
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
    """returns movies that at least one of the user's friends have watched, but the user has not watched."""
    user_watched_list = user_data["watched"]
    friends_watched_list = []
    
    #making friends_watched_list:
    friends_list=user_data["friends"]
    for friend_data in friends_list:
        watched_list = friend_data["watched"]
        for movie in watched_list:
            if movie not in friends_watched_list:
                friends_watched_list.append(movie)

    #making recommended list of movies to return:
    return_list = []
    for movie in friends_watched_list:
        if movie not in user_watched_list:
            return_list.append(movie)
    return return_list
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    """returns a list of recommended movies based on user's friends' watched list and their availability in user's subscription"""
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
    """returns recommended movies based on user's friends' watched list and user's most watched genre."""
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
    """returns movie recommendations based on user's favorite movies that user's friends haven't watched."""
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
