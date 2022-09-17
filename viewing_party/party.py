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
    max_watched_genre = max(watched_genre_dict, key = watched_genre_dict.get)
    
    return max_watched_genre
        




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

