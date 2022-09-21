import json
from textwrap import indent

# ------------- WAVE 1 --------------------

# Instantiate movie as dictionary if all fields are populated
def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {
            "title" : title,
            "genre" : genre,
            "rating" : rating,
        }
        return movie

# User_data set up as dictonary with the key watched corresponding to a list of movie dictionaries
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

#Watchlist key added as a list of dictionaries within the user_data dictionary
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


# function to remove a movie from the watchlist and add it to the watched list
def watch_movie(user_data, movie_title):

    # remove movie from watchlist 
    for movie in user_data["watchlist"]:
        if movie_title in movie["title"]:
            user_data["watchlist"].remove(movie)
            
    # Add movie to watched (inside of if so that if the movie was not in the watchlist, it will do nothing)
            user_data["watched"].append(movie)
    
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

#Function to calculate the average rating of a users watched movies
def get_watched_avg_rating(user_data):
    average = 0

    for movie in range(len(user_data["watched"])):
        average += user_data["watched"][movie]["rating"]

    # Return 0 if the user has no movies in watched
    if len(user_data["watched"]) > 0:  
        average /= len(user_data["watched"])

    return average

#function to calculate the most popular genre from watched
def get_most_watched_genre(user_data):

    genre_count = {}

    for movie in range(len(user_data["watched"])):
        if not user_data["watched"][movie]["genre"] in genre_count:
            genre_count[user_data["watched"][movie]["genre"]] = 1
        else:
            genre_count[user_data["watched"][movie]["genre"]] += 1

    if user_data["watched"]:
        return max(genre_count, key = genre_count.get)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

#funciton to return unique movies from all friends watched lists

#create set of titles that friends have watched
def friend_watched_set(user_data):
        friend_watched_titles_list = []
        for friends_watched_dict in user_data["friends"]:
            for friends_watched_movies in friends_watched_dict["watched"]:
                friend_watched_titles_list.append(friends_watched_movies['title'])
        friend_watched_titles_set = set(friend_watched_titles_list)
        return friend_watched_titles_set

#create set of titles the user has watched
def user_watched_set(user_data):
    user_watched_titles_list = []
    for user_watched_movie in user_data["watched"]:
       user_watched_titles_list.append(user_watched_movie['title'])
    user_watched_titles_set = set(user_watched_titles_list)
    return user_watched_titles_set

def get_unique_watched(user_data):
    #find the difference between the sets
    movie_titles_unique_to_user = user_watched_set(user_data).difference(friend_watched_set(user_data))

    #iterate through the user_watched list and append the movie dictionary to a list if the movie's title is in the unique to user set.
    unique_to_user_watched = []
    for movie in user_data["watched"]:
        if movie["title"] in movie_titles_unique_to_user:
            unique_to_user_watched.append(movie)

    return unique_to_user_watched

def get_friends_unique_watched(user_data):
    #find the movies unique to friends
    movie_titles_unique_to_friends = friend_watched_set(user_data).difference(user_watched_set(user_data))


    #iterate through friends movies and append the movie dictionary to a list if the movie's title is in movie_titles_unique_to friends set
    unique_to_friends_watched = []

    for friends_watched_dict in user_data["friends"]:
            for friends_watched_movie in friends_watched_dict["watched"]:
                if friends_watched_movie["title"] in movie_titles_unique_to_friends:
                    if friends_watched_movie in unique_to_friends_watched:
                        continue
                    else:
                        unique_to_friends_watched.append(friends_watched_movie)
    
    """""""""
    for title in movie_titles_unique_to_friends:
        for friend in user_data["friends"]:
            for movie_dict in friend["watched"]:
                if title in movie_dict['title']:
                    unique_to_friends_watched.append(friend)
    """""""""

    return unique_to_friends_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
