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
    for movie in user_data["watchlist"]:
        if title  == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)

    return user_data
        
        
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    average_rating = 0.0
    sum_ratings = 0

    if user_data["watched"] == []:
        average_rating = 0.0
        return average_rating

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
    
    return(max(set(movie_genre_list), key = movie_genre_list.count))

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_data_movies_list = get_user_data_watchlist(user_data)

    friends_movies_titles_list = get_friends_watchlists_titles(user_data)

    unique_user_data_movies_list = []   
    for movie in range(len(user_data_movies_list)):
        if not user_data_movies_list[movie]["title"] in friends_movies_titles_list:
            unique_user_data_movies_list.append(user_data_movies_list[movie])

    return unique_user_data_movies_list


def get_friends_unique_watched(user_data):
    user_data_movies_titles_list = get_user_data_watchlist_titles(user_data)

    friends_movies_list = get_friends_watchlists(user_data)

    friends_unique_movies_list = []

    for movie in range(len(friends_movies_list)):
        if not friends_movies_list[movie]["title"] in user_data_movies_titles_list:
            if friends_movies_list[movie] in friends_unique_movies_list:
                continue
            else:
                friends_unique_movies_list.append(friends_movies_list[movie])

    return friends_unique_movies_list


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    subscriptions = user_data["subscriptions"]
    
    friends_unique_movies_list = get_friends_unique_watched(user_data)

    movie_recommendations_list = []

    for movie in range(len(friends_unique_movies_list)):
        if friends_unique_movies_list[movie]["host"] in subscriptions:
            movie_recommendations_list.append(friends_unique_movies_list[movie])

    return movie_recommendations_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    user_data_movies_titles_list = []
    user_data_movies_list = []

    for i in range(len(user_data["watched"])):
        user_data_movies_titles_list.append(user_data["watched"][i]["title"])
    # print(f"debug:user data movies titles list {user_data_movies_list}\n")

    for i in range(len(user_data["watched"])):
        user_data_movies_list.append(user_data["watched"][i])
    # print(f"debug:user data movies list {user_data_movies_list}\n")

    friends_unique_movies_list = []
    
    friends_movie_1_list = user_data["friends"][0]["watched"]
    friends_movie_2_list = user_data["friends"][1]["watched"]
    # print(f"friend 1 movie list: {friends_movie_1_list} \n")
    # print(f"friend 2 movie list: {friends_movie_2_list} \n")

    friends_total_movie_list = friends_movie_1_list + friends_movie_2_list
    # print(f"debug:friends total movies list: {friends_total_movie_list}\n")

    for movie in range(len(friends_total_movie_list)):
        if not friends_total_movie_list[movie]["title"] in user_data_movies_titles_list:
            if friends_total_movie_list[movie] in friends_unique_movies_list:
                continue
            else:
                friends_unique_movies_list.append(friends_total_movie_list[movie])
    # print(f"debug:friend's unique list of movies: {friends_unique_movies_list}")
    
    genre_list = []
    for movie in range(len(user_data_movies_list)):
        genre = user_data_movies_list[movie]["genre"]
        genre_list.append(genre)
    # print(f"user data genre list: {genre_list}")
    
    movie_recommendations_list = []
    if len(user_data["watched"]) > 0:
        most_watched_genre = max(set(genre_list), key = genre_list.count)
        # print(f"user's most watched genre: {most_watched_genre}")

        # loop through friends unique movies to see if any of them are the most favorite genre
        for movie in range(len(friends_unique_movies_list)):
            if friends_unique_movies_list[movie]["genre"] == most_watched_genre:
                movie_recommendations_list.append(friends_unique_movies_list[movie])

    # print(f"debug: movie recommendations: {movie_recommendations_list}")
    return movie_recommendations_list


def get_rec_from_favorites(user_data):
    user_data_movies_list = user_data["watched"]
    # print(f"debug:user data movies list {user_data_movies_list}\n")
    
    friends_movies_1_title_list = []
    friends_movies_2_title_list = []
    
    if len(user_data["friends"]) > 0:
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
    friends_movie_set = set(friends_movie_list)
    friends_movie_list = list(friends_movie_set)

    unique_user_data_movies_list = []
    for movie in range(len(user_data_movies_list)):
        if not user_data_movies_list[movie]["title"] in friends_movie_list:
            unique_user_data_movies_list.append(user_data_movies_list[movie])
    # print(f"debug:user data's unique list of movies: {unique_user_data_movies_list}\n")
    
    favorites = user_data["favorites"]
    # print(f"debug: user data favorite movies: {favorites}")
    
    movie_recommendations_list = []
    if len(user_data["watched"]) > 0:
        # loop through users unique movies to see if any of them are favorites
        for movie in range(len(unique_user_data_movies_list)):
            if unique_user_data_movies_list[movie] in favorites:
                movie_recommendations_list.append(unique_user_data_movies_list[movie])

    # print(f"debug: movie recommendations: {movie_recommendations_list}")
    return movie_recommendations_list


# -----------------------------------------
# ------------- HELPERS -------------------
# -----------------------------------------
def get_user_data_watchlist(user_data):
    user_data_movies_list = []

    for i in range(len(user_data["watched"])):
        user_data_movies_list.append(user_data["watched"][i])

    return user_data_movies_list

def get_user_data_watchlist_titles(user_data):
    user_data_movies_titles_list = []

    for i in range(len(user_data["watched"])):
        user_data_movies_titles_list.append(user_data["watched"][i]["title"])

    return user_data_movies_titles_list

def get_friends_watchlists(user_data):
    friends_movie_1_list = user_data["friends"][0]["watched"]
    friends_movie_2_list = user_data["friends"][1]["watched"]

    friends_movies_list = friends_movie_1_list + friends_movie_2_list
    return friends_movies_list


def get_friends_watchlists_titles(user_data):
    friends_movies_1_title_list = []
    friends_movies_2_title_list = []
    
    friends_movie_1_list = user_data["friends"][0]["watched"]
    friends_movie_2_list = user_data["friends"][1]["watched"]

    for movie in range(len(friends_movie_1_list)):
        title_f1 = friends_movie_1_list[movie]["title"]
        friends_movies_1_title_list.append(title_f1)

    for movie in range(len(friends_movie_2_list)):
        title_f2 = friends_movie_2_list[movie]["title"]
        friends_movies_2_title_list.append(title_f2)
    
    friends_movies_titles_list = friends_movies_1_title_list + friends_movies_2_title_list
    friends_movies_titles_set = set(friends_movies_titles_list)
    friends_movies_titles_list = list(friends_movies_titles_set)

    return friends_movies_titles_list