# ------------- WAVE 1 --------------------

from enum import unique
from itertools import count

# creates a movie object with a given title, genre, and rating
# parameters: title - title of movie, genre - genre of movie, rating - rating of the movie 
def create_movie(title, genre, rating):
    # we first check if all of our arguments are truthy if not we return None
    if not title or not genre or not rating:
        return None
    # we then create the dictionary with the keys title, genre, and rating corresponding to our given arguments and return
    else:
        movie_details = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie_details

# adds a movie object to a user's watched list
# parameters: user_data - a user's movie information including watched list, movie - movie you have watched
def add_to_watched(user_data, movie):
    # we can append the movie object to the user's watched list
    user_data["watched"].append(movie)
    return user_data

# adds a movie object to a user's want to watch list
# parameters: user_data - a user's movie information including watched list, movie - movie you want to watch
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# moves a movie object from a user's want to watch list to their watched list, different from add_to_watched() which adds a movie object not already in the want to watch list to the watch list
def watch_movie(user_data, title):
    # look for the movie in the want to watch list by looping through and matching the titles
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            # using the add_to_watched() function add the movie object to the watched list 
            add_to_watched(user_data, movie)
            # we can now remove the movie from the user's want to watch list
            user_data["watchlist"].remove(movie)
            # we return here and end the loop
            return user_data
    # the function will not add the move to the watched list if it was not found in the want to watch list
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# calculates a user's average rating for movies from their watched list (let's see how their taste is)
# parameters: user_data - a user's movie information including watched list
# returns float average rating, 0.0 if empty watched list
def get_watched_avg_rating(user_data):
    # set the avg rating to 0 initially, if they have no movies in their watched list this is the default value returned
    average_rating = 0.0
    # make sure that their watched list is not empty because we will later be dividing by the length of it (we dont want a 0 denominator)
    if user_data["watched"]:
        # loop through each movie in the watched list and access its rating, add the rating to the average rating and divide by the length after iterating
        for movie in user_data["watched"]:
            average_rating += movie["rating"]
        average_rating = average_rating / len(user_data["watched"])
    return average_rating

# finds the users most watched movie genre and returns it.
# parameters: user_data - a user's movie information including watched list
# returns string of most watched genre, None if empty watched list
def get_most_watched_genre(user_data):
    # create an empty dictionary that will hold the genres and the their occurences in the watched list
    genre_dict = {}
    # check that the watched list has movies
    if user_data["watched"]:
        # loop through and add each genre to the dictionary, if they already are in the dictionary then increment their dictionary value by 1
        for movie in user_data["watched"]:
            if movie["genre"] in genre_dict:
                genre_dict[movie["genre"]] += 1
            else:
                genre_dict[movie["genre"]] = 1
        # to find the genre with the highest count, initiate a variable for the highest watched genre and its count
        # then loop through the genre dictionary and compare each genre's count to the stored value for count, if it is higher replace the count value with the genre's count value and the genre string with the respective genre
        most_watched_genre = ""
        count_for_genre = 0
        for genre, quantity in genre_dict.items():
            if quantity > count_for_genre:
                count_for_genre = quantity
                most_watched_genre = genre
        return most_watched_genre

    else:
        return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# get a list of movies that you have watched but none of your friends have watched
# parameters: users data
# return list of movies objects
def get_unique_watched(users_data):
    friends_movies_set = []
    users_movies_set = []
    # loop through the friends watched list and add each movie title to the set
    for friend in users_data["friends"]:
        for movie in friend["watched"]:
            friends_movies_set.append(movie["title"])
    # loop through the user's watched list and add each movie title to the set
    for movie in users_data["watched"]:
        users_movies_set.append(movie["title"])
    # turn list to set so we can find the difference between user's and friend's list in O(n) time
    friends_movies_set = set(friends_movies_set)
    users_movies_set = set(users_movies_set)
    unique_movies_titles = users_movies_set - friends_movies_set
    # loop through the movies in the user's watched list and if the movie title is in the set of unique movies, append that movie to a list and return it
    unique_movies = []
    for movie in users_data["watched"]:
        if movie["title"] in unique_movies_titles:
            unique_movies.append(movie)
    return unique_movies

# get a list of movies that you friends have watched but you haven't
# parameters: users data
# return list of movies objects
def get_friends_unique_watched(users_data):
    friends_movies_set = []
    users_movies_set = []
    # loop through the friends watched list and add each movie title to the set
    for friend in users_data["friends"]:
        for movie in friend["watched"]:
            friends_movies_set.append(movie["title"])
    # loop through the user's watched list and add each movie title to the set
    for movie in users_data["watched"]:
        users_movies_set.append(movie["title"])
    # turn list to set so we can find the difference between user's and friend's list in O(n) time
    friends_movies_set = set(friends_movies_set)
    users_movies_set = set(users_movies_set)
    unique_movies_titles = friends_movies_set - users_movies_set
    unique_movies = []
    # loop through the movies in the friends's watched list and if the movie title is in the set of unique movies but not already in the list, append that movie to a list and return it
    for friend in users_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in unique_movies_titles and movie not in unique_movies:
                unique_movies.append(movie)
    return unique_movies
        


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# returns a list of recommended movies based on friends watched, available streaming services, and unwatched movies
# parameters: users_data
# returns a list of movies objects 
def get_available_recs(user_data):
    # use the unique_friends_movies functions to return a list of movies that have been watched by friends but not the user
    unique_friends_movies = get_friends_unique_watched(user_data)
    recommendations = []
    # loop through each movie that friedns have watched but not user and check if the user has access to the host of each movie 
    for movie in unique_friends_movies:
        # append to list if movie can be streamed
        if movie["host"] in user_data["subscriptions"]:
            recommendations.append(movie)
    return recommendations
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# returns a list of recommended movies based on friends watched, most watched genre, and unwatched movies
# parameters: users_data
# returns a list of movies objects 
def get_new_rec_by_genre(user_data):
    # get user's most watched genre by looping through movies and storing their frequencies in a dictionary
    genre_freq = {}
    for movie in user_data["watched"]:
        if movie["genre"] in genre_freq:
            genre_freq[movie["genre"]] += 1
        else:
            genre_freq[movie["genre"]] = 1
    frequency = 0
    genre_saved = ""
    for genre, freq in genre_freq.items():
        if frequency < freq:
            frequency = freq
            genre_saved = genre

    recommended_movies = []
    unique_friends_movies = get_friends_unique_watched(user_data)
    for movie in unique_friends_movies:
        if movie["genre"] == genre_saved:
            recommended_movies.append(movie)
    return recommended_movies

# returns a list of recommended movies for friends based on users favorites and friends' unwatched movies
# parameters: users_data
# returns a list of movies objects 
def get_rec_from_favorites(users_data):
    recommended_movies = []
    # loop through each movie in the favorites list and check that it is not in any of the friends' watched list
    for movie in users_data["favorites"]:
        found = False
        for friend in users_data["friends"]:
            if found == True:
                break
            for friend_movie in friend["watched"]:
                if movie["title"] == friend_movie["title"]:
                    found = True
                    break
    # only add to recommended movies if it was not found in any of the friends' lists
        if found == False:
            recommended_movies.append(movie)
    return recommended_movies
