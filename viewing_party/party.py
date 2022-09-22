# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        new_movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):

    for movie in user_data["watchlist"]:
        if title in movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            
    return user_data
            

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    total_ratings = 0
    number_of_movies = 0

    for movie_dict in user_data["watched"]:
        total_ratings += movie_dict["rating"]
        number_of_movies += 1

    if number_of_movies == 0:
        average_rating = 0.0
    else:
        average_rating = total_ratings/number_of_movies

    return average_rating

# my_data = {"watched": [{"title": "scary movie", "genre": "horror", "rating": "3"}, {"title": "another scary movie", "genre": "horror", "rating": "2"}, {"title": "funny movie", "genre": "comedy", "rating": "5"}]}
def get_most_watched_genre(user_data):
    genre_freq_dict = {}
    
    for movie_dict in user_data["watched"]:

        if movie_dict["genre"] not in genre_freq_dict:
            genre_freq_dict[movie_dict["genre"]] = 1
        else:
            genre_freq_dict[movie_dict["genre"]] += 1
    
    if user_data["watched"] == []:
        max_genre = None
    else:
        max_genre = max(genre_freq_dict, key=genre_freq_dict.get)

    return max_genre
  

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    #put each grouops watched movie titles in a set
    my_watched_set = set()
    friends_watched_set = set()

    for movie_dict in user_data["watched"]:
        my_watched_set.add(movie_dict["title"])
    
    for friends_list in user_data["friends"]:
        for friends_watched_dict, friends_watched_list in friends_list.items():
            for friends_movie_dict in friends_watched_list:
                friends_watched_set.add(friends_movie_dict["title"])

    
#compare sets and output movies in watched that aren't in friends
    user_watched_diffs_titles = my_watched_set.difference(friends_watched_set)
    user_watched_dif_list = []
    for movie_dict in user_data["watched"]:
        if movie_dict["title"] in user_watched_diffs_titles:
            user_watched_dif_list.append(movie_dict)
  
    return user_watched_dif_list

def get_friends_unique_watched(user_data):
    user_movies_list = []
    for movie_info in user_data["watched"]:
        user_movies_list.append(movie_info)
    #make a list of friends movies
    friends_movies_list = []
    for indi_friends_dict in user_data["friends"]:
        for key, friend_list in indi_friends_dict.items():
            for movie_info in friend_list:
                friends_movies_list.append(movie_info)
    #if friend movie not in user movie, add to potential watchlist(unique_friend_movies)
    user_hasnt_watched = [] #list of dictionaries with movie info friends have watched
    potential_movies = []
    
    for movie_info in friends_movies_list:
        if movie_info not in user_movies_list:
            user_hasnt_watched.append(movie_info)
            
    user_hasnt_watched_dict = {}
    for movie in user_hasnt_watched:
        user_hasnt_watched_dict[movie["title"]] = movie
    
    for title, movie in user_hasnt_watched_dict.items():
        potential_movies.append(movie)

    return potential_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recommended_movies_list = []
#1. loop through the friends movies and see which ones the
#user hasn't watched.
    #make a list of user movies
    user_movies_list = []
    for movie_info in user_data["watched"]:
        user_movies_list.append(movie_info)
    #make a list of friends movies
    friends_movies_list = []
    for indi_friends_dict in user_data["friends"]:
        for key, friend_list in indi_friends_dict.items():
            for movie_info in friend_list:
                friends_movies_list.append(movie_info)
    #if friend movie not in user movie, add to potential watchlist(unique_friend_movies)
    user_hasnt_watched = [] #list of dictionaries with movie info friends have watched
    potential_movies = []
    
    for movie_info in friends_movies_list:
        if movie_info not in user_movies_list:
            user_hasnt_watched.append(movie_info)
            
    user_hasnt_watched_dict = {}
    for movie in user_hasnt_watched:
        user_hasnt_watched_dict[movie["title"]] = movie
    
    for title, movie in user_hasnt_watched_dict.items():
        potential_movies.append(movie)

#2. loop through the host of the friends unique movies and
#see which hosts are in the users movies hosts
    for movie in potential_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies_list.append(movie)

    return recommended_movies_list  
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):

#Find the most frequently watched genre in users movies
    freq_genre = get_most_watched_genre(user_data)
# Find movies the user hasn't watched but at least one of their friend's have watched
    unique_friends_movies = get_friends_unique_watched(user_data)

# find which movies in the unique_friends_movies list has the same genre as...
# the users most frequent watched genre
    rec_movies = []    

    for movie in unique_friends_movies:
        if freq_genre in movie["genre"]:
            rec_movies.append(movie)
    return rec_movies
