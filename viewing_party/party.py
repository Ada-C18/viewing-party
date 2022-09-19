# ------------- WAVE 1 --------------------

from re import M


def create_movie(title, genre, rating):

    # return None if not filled out
    if title == None or genre == None or rating == None:
        return None

    # create movie dictionary
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    return movie

# add watched to list
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

# test adds move to user watchlist
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# moves movie from watchlist to empty watched
def watch_movie(user_data, title):
    watchlist= user_data["watchlist"]
    for i in range(len(watchlist)):
        if watchlist[i]["title"]== title:
            user_data["watched"].append(watchlist[i])
            del watchlist[i]
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# calculates average rating
def get_watched_avg_rating(user_data):
    all_rating = []
    watched = user_data["watched"]
    for movie in watched:
        all_rating.append(movie["rating"])

# if rating list is empty return 0
    if len(all_rating) == 0:
        average_rating = 0.0
    else:
        average_rating = sum(all_rating) / (len(all_rating))
    return average_rating


# most viewed genre
def get_most_watched_genre(user_data):
    all_genre = []
    watched = user_data["watched"]
    for movie in watched:
        all_genre.append(movie["genre"])

# if genre list is empty return None
    if len(all_genre) == 0:
        most_watched_genre = None
    else:
        most_watched_genre = max(all_genre, key=all_genre.count)
    return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# get unique movie from user
def get_unique_watched(user_data):

    my_movie_titles = []
    friend_movie_titles = []

    watched = user_data["watched"]
    friend_watched_1 = user_data["friends"][0]["watched"]
    friend_watched_2 = user_data["friends"][1]["watched"]
    
    
    for movie in watched:
        my_movie_titles.append(movie["title"])
    for movie in friend_watched_1:
        friend_movie_titles.append(movie["title"])
    for movie in friend_watched_2:
        friend_movie_titles.append(movie["title"])
    
    my_movie_titles_set = set(my_movie_titles)
    friend_movie_titles_set = set(friend_movie_titles)
    unique_watched = my_movie_titles_set - friend_movie_titles_set
    
    unique_movie_list = []
    for uniquemovie in watched:
        if uniquemovie["title"] in unique_watched: 
            unique_movie_list.append(uniquemovie)
    return unique_movie_list


# get unique movie from friends
def get_friends_unique_watched(user_data):
    my_movie_titles = []
    friend_movie_titles = []

    watched = user_data["watched"]
    friend_watched_1 = user_data["friends"][0]["watched"]
    friend_watched_2 = user_data["friends"][1]["watched"]
    
    
    for movie in watched:
        my_movie_titles.append(movie["title"])
    for movie in friend_watched_1:
        friend_movie_titles.append(movie["title"])
    for movie in friend_watched_2:
        friend_movie_titles.append(movie["title"])
    
    my_movie_titles_set = set(my_movie_titles)
    friend_movie_titles_set = set(friend_movie_titles)
    unique_watched = friend_movie_titles_set - my_movie_titles_set
    

    unique_movie_list = []
    for uniquemovie in friend_watched_1:
        if uniquemovie["title"] in unique_watched: 
            unique_movie_list.append(uniquemovie)
    for uniquemovie in friend_watched_2:
        if uniquemovie["title"] in unique_watched: 
            unique_movie_list.append(uniquemovie)
    
    # make sure there are no duplicates of friends unique data
    single_unique_movies_list = []
    for single in unique_movie_list:    
        if unique_movie_list.count(single) >= 2:
            if single not in single_unique_movies_list:
                single_unique_movies_list.append(single)
        else:
            single_unique_movies_list.append(single)

    return single_unique_movies_list    
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    movies_for_recs = get_friends_unique_watched(user_data)
    subscriptions_list = []
    for subscription in user_data["subscriptions"]:
        subscriptions_list.append(subscription)

    reccomended_movies = []
    for movie in movies_for_recs:
        if movie["host"] in subscriptions_list:
            reccomended_movies.append(movie)
    return reccomended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# Returns reccomended movies based on genre
def get_new_rec_by_genre(user_data):
    movies_for_rec = get_friends_unique_watched(user_data)
    most_watched_genre = get_most_watched_genre(user_data)
    recommended_movies_by_genre = []

    for movie in movies_for_rec:
        if movie["genre"] == most_watched_genre:
            recommended_movies_by_genre.append(movie)
    return recommended_movies_by_genre

# Returns reccommended movies based on favorites
def get_rec_from_favorites(user_data):
    favorites = user_data["favorites"]
    if len(user_data["friends"]) > 0:
        friend_watched_1 = user_data["friends"][0]["watched"]
        friend_watched_2 = user_data["friends"][1]["watched"]
    recommended_movies_by_favorites = []

    for fav_movie in favorites:
        if len(user_data["friends"]) == 0:
            recommended_movies_by_favorites.append(fav_movie)
        elif fav_movie in favorites and fav_movie not in friend_watched_1 and fav_movie not in friend_watched_2:
            recommended_movies_by_favorites.append(fav_movie)
    return recommended_movies_by_favorites


