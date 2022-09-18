# ------------- WAVE 1 --------------------
#added a comment to test commit
from tests.test_constants import MOVIE_TITLE_1

def create_movie(title, genre, rating):
    new_movie = {}
    if not title  or not genre or not rating:
        return None
    else:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    return new_movie

def add_to_watched(user_data, movie):
    user_data  = {"watched": [movie]}
    return user_data

def add_to_watchlist(user_data, movie):
    user_data  = {"watchlist": [movie]}
    return user_data

def watch_movie(user_data, title):
    # initialize variable watch_list that equal dictionary "user_data" with key "watchlist"
    watch_list = user_data["watchlist"]
    for movie in watch_list:
        if movie["title"] == title:
            # if title of movie from watchlist equal title of watched movie,
            # than remove that movie from watchlist, return it's value to variable "watched_movie" 
            # and add to watched list
            watched_movie = watch_list.pop(watch_list.index(movie))
            user_data["watched"].append(watched_movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    
    # initialize variables average_rating, rating_sum and movies_count
    average_rating = 0.0
    rating_sum = 0
    movies_count = 0
    
    # if movie not in watched list, return average_rating = 0.0
    # otherwise calculate sum, count of rating and average rating
    if not watched_list:
        return average_rating
    else:
        for movie in watched_list:
            rating_sum += movie["rating"]
            movies_count += 1
    average_rating = rating_sum / movies_count
        
    return average_rating

def get_most_watched_genre(user_data):
    watched_list = user_data["watched"]
    if not watched_list:
        return None
    else:
        # initialize dict and loop though movies in watched list 
        watched_genre_dict = {}
        for movie in watched_list:
            genre_name = movie["genre"]
            
            # add each new genre name as key and assign value 1
            # if key with genre name is already exist, increment by 1
            if genre_name not in watched_genre_dict:
                watched_genre_dict[genre_name] = 1
            else:
                watched_genre_dict[genre_name] += 1
    
    # use get method and max function to return dictionary key with max value
    most_watched_genre = max(watched_genre_dict, key = watched_genre_dict.get)
    
    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# create helper function to get unique movies for user
def get_user_watched_list(user_data):
    user_watched_movies_list = user_data["watched"]
    return user_watched_movies_list

# create helper function to get unique movies for all friends
def get_all_friends_unique_watched_list(user_data):
    friends_unique_watched_list = []
    friends_list = user_data["friends"]
   
    for friend in friends_list:
        for movie in friend["watched"]:
            if movie not in friends_unique_watched_list:
                friends_unique_watched_list.append(movie) 
    return friends_unique_watched_list  

# create function to get list of movies that user has watched, 
# but none of their friends have watched.
def get_unique_watched(user_data): 
    user_unique_list = []
    user_only_unique_list = get_user_watched_list(user_data)
    all_friends_unique_list = get_all_friends_unique_watched_list(user_data)

    for movie in user_only_unique_list:
        if movie not in all_friends_unique_list:
            user_unique_list.append(movie)  
    return user_unique_list  

# create function to get list of movies at least one of the user's friends
# have watched, but the user has not watched.
def get_friends_unique_watched(user_data):
    friends_unique_list = []
    user_unique_list = get_user_watched_list(user_data)
    all_friends_unique_list = get_all_friends_unique_watched_list(user_data)

    for movie in all_friends_unique_list:
        if movie not in user_unique_list:
            friends_unique_list.append(movie)  
    print(friends_unique_list)
    return friends_unique_list
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# create function to return list of recommended movies
def get_available_recs(user_data):
    recommended_movies = []
    user_subcribtion_list = user_data["subscriptions"]
    # initialize a variable with return value of function 
    # get_friends_unique_watched
    user_has_not_watched_movies = get_friends_unique_watched(user_data)
       
    # loop though list of the movies which user has not watched;
    # add a movie to the recommended if the user that subcription to the host of the movie
    for movie in user_has_not_watched_movies:
        for subcribton in user_subcribtion_list:
            if movie["host"] == subcribton:
                recommended_movies.append(movie)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommended_movies_by_genre = []
    most_popular_wached_genre = get_most_watched_genre(user_data)
    # initialize a variable with return value of function 
    # get_friends_unique_watched
    user_has_not_watched_movies = get_friends_unique_watched(user_data)
    
    # loop though list of movies which the user has not watched;
    # add a movie to the recommended if the "genre" of the movie is the same 
    # as the user's most frequent genre
    for movie in user_has_not_watched_movies:
        if most_popular_wached_genre == movie["genre"]:
                recommended_movies_by_genre.append(movie)
    
    return recommended_movies_by_genre
    

