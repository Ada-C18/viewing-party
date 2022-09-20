# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {
        "title" : title,
        "genre" : genre,
        "rating": rating
    }

    if new_movie["title"] and new_movie["genre"] and new_movie["rating"]:
         return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data = {
        "watched" : [movie]
    }
    return user_data
    
def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist" : [movie]
    }
    return user_data

def watch_movie(user_data, title):
    # watchlist = user_data["watchlist"]
    for movie in user_data["watchlist"]:
    # if the title is in a movie in the user's watchlist:
        if title  == movie["title"]:
            print(f"debug: title in movie dict")
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            # return the user_data

    print(f"debug: title not in movie dict")
    return user_data
        
        
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    average_rating = 0.0
    sum_ratings = 0
    # The average rating of an empty watched list is 0.0
    if user_data["watched"] == []:
        average_rating = 0.0
        return average_rating

    # Calculate the average rating of all movies in the watched list
    for movie in range(len(user_data["watched"])):
        sum_ratings += user_data["watched"][movie]["rating"]

    average_rating = sum_ratings / len(user_data["watched"])

    return average_rating
    
def get_most_watched_genre(user_data):
    if user_data["watched"] == []:
        return None

    movie_genre_list = []
    for movie_genre in range(len(user_data["watched"])):
        movie_genre_list.append(user_data["watched"][movie_genre]["genre"])

    print(max(set(movie_genre_list), key = movie_genre_list.count), movie_genre_list)
    
    return(max(set(movie_genre_list), key = movie_genre_list.count))

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    # what movies has the user watched?
    user_data_movies_list = user_data["watched"]
    print(f"user data movie list {user_data_movies_list}\n")
    unique_user_data_movies_list = []
    friends_movies_1_title_list = []
    friends_movies_2_title_list = []
    
    # what movies has the user's friends watched?
    friends_movie_1_list = user_data["friends"][0]["watched"]
    friends_movie_2_list = user_data["friends"][1]["watched"]
    # print(f"friend 1 movie list: {friends_movie_1_list} \n")
    # print(f"friend 2 movie list: {friends_movie_2_list} \n")
            
    for movie in range(len(friends_movie_1_list)):
        title_f1 = friends_movie_1_list[movie]["title"]
        friends_movies_1_title_list.append(title_f1)
    # print(f"friend1 movie titles list: {friends_movies_1_title_list}")

    for movie in range(len(friends_movie_2_list)):
        title_f2 = friends_movie_2_list[movie]["title"]
        friends_movies_2_title_list.append(title_f2)
    # print(f"friend2 movie titles list: {friends_movies_2_title_list}")
    
    friends_movie_list = friends_movies_1_title_list + friends_movies_2_title_list
    friends_unique_movie_set = set(friends_movie_list)
    friends_unique_movie_list = list(friends_unique_movie_set)

    for movie in range(len(user_data_movies_list)):
        if not user_data_movies_list[movie]["title"] in friends_unique_movie_list:
            unique_user_data_movies_list.append(user_data_movies_list[movie])


    # print(f"debug:user data's unique list of movies: {unique_user_data_movies_list}")
    # return a list of dictionaries that represents the list of movies 
    return unique_user_data_movies_list



def get_friends_unique_watched(user_data):
    # what movies has the user watched?
    # what movies has the user's friends watched?
    # Determine which movies at least one of the user's friends have watched, but the user has not watched.
    # return a list of dictionaries that represents the list of movies 
    ...
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
