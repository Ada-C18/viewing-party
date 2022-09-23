# ------------- WAVE 1 --------------------

from lzma import MODE_FAST

def create_movie(title, genre, rating):
    # check to see if parameters are true
    # conditional for each paramter 
    # add parameters to a dictionary if true
    # create a dictionary
    # append to dictionary if true, NONE if false
    # return dictionary

    movie = {}
    if title == None or genre == None or rating == None:
        return None
    else:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie

def add_to_watched(user_data, movie):
    watched =[]
    watched.append(movie)
    user_data["watched"] = watched

    return user_data

def add_to_watchlist(user_data, movie):
    watchlist = []
    watchlist.append(movie)
    user_data["watchlist"] = watchlist

    return user_data

def watch_movie(user_data, title):
    # need to see if the title is in the usersdata
    # if movie in WATCHLIST then remove the movie from watchlist 
    # and add to watched, return
    # if movie not in watchlist, return
    for i in range(len(user_data['watchlist'])):
        if user_data['watchlist'][i]['title'] == title:
            user_data['watched'].append(user_data['watchlist'][i])
            user_data['watchlist'].remove(user_data['watchlist'][i])
            return user_data
        
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def average(lst):
    return sum(lst) / len(lst)

def get_watched_avg_rating(user_data):
    rating_list = []
    watched_list = user_data["watched"]
    for movie in watched_list:
        rating_list.append(movie['rating'])

    if rating_list:
        return average(rating_list)
    else:
        return 0.0

def get_most_watched_genre(user_data):
    most_watched_genre_dict = {}
    watched_movies_list = user_data["watched"]
    for movie in watched_movies_list:
        genre = movie["genre"]
        if genre not in most_watched_genre_dict:
            most_watched_genre_dict[genre] = 1
        else:
            most_watched_genre_dict[genre] += 1

    if most_watched_genre_dict:
        max_val = list(most_watched_genre_dict.values())
        max_key = list(most_watched_genre_dict.keys())
        return max_key[max_val.index(max(max_val))]
    else:
        return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    # create a list of movies watched by the user
    # create a list of movies watched by the friends
    # compare list of movies by user to movies by friend
    # return list of movies only watched by user
    # create a new unique list of movies watched by user
    user_movie_list = user_watched_list(user_data)
    friends_movie_list = friends_watched_list(user_data)
    unique_movie_list = []

    for movie in user_movie_list:
        if movie not in friends_movie_list:
            unique_movie_list.append(movie)
    return unique_movie_list

def get_friends_unique_watched(user_data):
    user_movie_list = user_watched_list(user_data)
    friends_movie_list = friends_watched_list(user_data)
    friends_unique_movie_list = []

    for movie in friends_movie_list:
        if movie not in user_movie_list:
            if movie not in friends_unique_movie_list:
                friends_unique_movie_list.append(movie)
    return friends_unique_movie_list
    
# HELPER FUNCTION
def user_watched_list(user_data):
    user_watched_list = []
    for movie in user_data["watched"]:
        user_watched_list.append(movie)
    return user_watched_list

# HELPER FUNCTION
def friends_watched_list(user_data):
    friends_watched_list = []
    for friend_movie_dict in user_data["friends"]:
        for movie_dict in friend_movie_dict["watched"]:
            for value in movie_dict.items():
                if value not in friends_watched_list:
                    friends_watched_list.append(movie_dict)
    return friends_watched_list
    

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    new_movies = get_friends_unique_watched(user_data)
    recommendations = []
    subscriptions = user_data["subscriptions"]
    for movie in new_movies:
        host = movie["host"]
        if host in subscriptions:
            recommendations.append(movie)
    return recommendations
    


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    recommendations_genre_based = []
    new_movies = get_friends_unique_watched(user_data)
    this_is_most = get_most_watched_genre(user_data)
    for movie in new_movies:
        if movie["genre"] == this_is_most:
            recommendations_genre_based.append(movie) 
    return recommendations_genre_based

def get_rec_from_favorites(user_data):
    friends_watched = friends_watched_list(user_data)
    user_favorites = user_data["favorites"]
    recommendations_favorites_based = []
    for movie in user_favorites:
        if movie not in friends_watched:
            recommendations_favorites_based.append(movie)
    return recommendations_favorites_based