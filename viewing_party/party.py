# ------------- WAVE 1 --------------------

# 1.1
def create_movie(title, genre, rating):
    if title and genre and (type(rating) == int or type(rating) == float):
        movie_dict = {
                "title": title,
                "genre": genre,
                "rating": rating
            }
        return movie_dict
    else:
        return None

# 1.2
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


# 1.3
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data
    

# 1.4
def watch_movie(user_data, title):
    watchlist_list = user_data["watchlist"]
    watched_list = user_data["watched"]

    for movie in watchlist_list:
        if movie["title"] == title:
            watchlist_list.remove(movie)
            watched_list.append(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# 2.1
def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    if len(watched_list) == 0:
        return 0.0

    average_rating = 0.0
    for movie in watched_list:
        movie_rating = movie["rating"]
        average_rating += movie_rating
    average_rating /= len(watched_list)
    return average_rating 


# 2.2
def get_most_watched_genre(user_data):
    watched_list = user_data["watched"]
    if len(watched_list) == 0:
        return None
    
    most_watched_genre = None
    most_watched_count = 0
    genre_count = {}
    for watched_movie in watched_list:
        genre = watched_movie["genre"]
        if genre in genre_count:
            genre_count[genre] += 1
        else:
            genre_count[genre] = 1

        if most_watched_count < genre_count[genre]:
            most_watched_count = genre_count[genre]
            most_watched_genre = genre

    return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# # 3.1

def get_unique_watched(user_data):
    user_watched = user_data["watched"]
    user_friends = user_data["friends"]

    unique_watched = []
    all_friends_titles = []

    for friend in user_friends:
        for watched_movie in friend["watched"]:
            all_friends_titles.append(watched_movie["title"])

    for user_movie in user_watched:
        if user_movie["title"] not in all_friends_titles:
            unique_watched.append(user_movie)

    return unique_watched

# 3.2 
#         
def get_friends_unique_watched(user_data):
    user_watched = user_data["watched"]
    user_movie_titles = []
    for user_movie in user_watched:
        user_movie_titles.append(user_movie["title"])

    user_not_watched = []
    user_friends = user_data["friends"]
    
    for friend in user_friends:
        friend_watched = friend["watched"]
        for friend_movie in friend_watched:
            if friend_movie["title"] not in user_movie_titles and friend_movie not in user_not_watched:
                user_not_watched.append(friend_movie)
    return user_not_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# 4.1 

def get_available_recs(user_data):
    friend_recs = get_friends_unique_watched(user_data)
    available_recs = []
    for rec in friend_recs:
        if rec["host"] in user_data["subscriptions"]:
            available_recs.append(rec)
    return available_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# 5.1
def get_new_rec_by_genre(user_data):
    user_most_watched_genre =  get_most_watched_genre(user_data)
    rec_movies = []

    for movie in get_friends_unique_watched(user_data):
        if user_most_watched_genre == movie["genre"]:
            rec_movies.append(movie)
    return rec_movies

# 5.2
# def get_rec_from_favorites(user_data):
    

