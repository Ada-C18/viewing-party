# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None

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
    watchlist = user_data["watchlist"]
    for i in range (len(watchlist)):
        if watchlist[i]["title"] == title:
            user_data["watched"].append(watchlist[i])
            del watchlist[i]
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    rating_sum = 0
    watched_list = user_data["watched"]
    watched_num = len(watched_list)
    for movie in watched_list:
        rating_sum += movie["rating"]
    if watched_num > 0:
        average = rating_sum / watched_num
    else:
        return 0
    return average

def get_most_watched_genre(user_data):
    genre_list = []
    watched_list = user_data["watched"]
    if len(watched_list) == 0:
        return None 
    for movie in watched_list:
        genre_list.append(movie["genre"])
    
    counter = 0
    for i in genre_list:
        curr_frenquency = genre_list.count(i)
        if curr_frenquency > counter:
            counter = curr_frenquency
            popular_genre = i
    return popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_friend_watched_movies(user_data):
    #put all friednds watched list into one list
    friend_watched_movies = []
    for friend_dict in user_data["friends"]:
        for friend_list in friend_dict["watched"]:
            friend_watched_movies.append(friend_list)
    return friend_watched_movies

def get_unique_watched(user_data):
    friend_watched_movies = get_friend_watched_movies(user_data)
    unique_movies = []
    for my_movie in user_data["watched"]:
        if my_movie not in friend_watched_movies:
            unique_movies.append(my_movie)
    return unique_movies

def get_friends_unique_watched(user_data):
    # get a list of friend watched movies by using helper function above 
    friend_watched_movies = get_friend_watched_movies(user_data)
    # get a list of my watched movies
    my_watched_movies = user_data["watched"]
    friends_unique_movies = []
    for friend_movie in friend_watched_movies:
        if friend_movie not in my_watched_movies and friend_movie not in friends_unique_movies:
            friends_unique_movies.append(friend_movie)
    return friends_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friend_unique_watched = get_friends_unique_watched(user_data)
    # print(friend_unique_watched)
    recommendations = []
    for movie in friend_unique_watched:
        if movie["host"] in user_data["subscriptions"]:
            recommendations.append(movie)
    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    friend_unique_movies = get_friends_unique_watched(user_data)
    my_watched_genres = []
    for movie in user_data["watched"]:
        my_watched_genres.append(movie["genre"])
    if len(my_watched_genres) > 0 and len(friend_unique_movies) > 0:
        popular_genre = max(set(my_watched_genres), key=my_watched_genres.count)
        recommendations = []
        for movie in friend_unique_movies:
            if movie["genre"] == popular_genre:
                recommendations.append(movie)
    else:
        recommendations = []
    return recommendations

def get_rec_from_favorites(user_data):
  recommendations = []
  favorite_movies = user_data["favorites"]
  friend_watched_movies = get_friend_watched_movies(user_data)
  for movie in favorite_movies:
    if movie not in friend_watched_movies:
      recommendations.append(movie)
  return recommendations