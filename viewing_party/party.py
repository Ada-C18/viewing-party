# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    else:
        movie = {}
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
    return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    movie = next((item for item in user_data["watchlist"] if item["title"] == movie_title), None)
    if movie:
        add_to_watched(user_data, movie)
        user_data["watchlist"].remove(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_total = 0
    number_of_ratings = len(user_data["watched"])
    for i in range(number_of_ratings):
        rating_total += user_data["watched"][i]["rating"]
    if number_of_ratings > 0:
        return rating_total / number_of_ratings
    else:
        return 0

def get_most_watched_genre(user_data):
    watch_frequency = {}
    most_watched_rate = 0
    watched_list = user_data["watched"]
    if len(watched_list) < 1:
        return None
    for i in range(len(watched_list)):
        genre = user_data["watched"][i]["genre"]
        if  genre not in watch_frequency:
            watch_frequency[genre] = 1
        else:
            watch_frequency[genre] += 1
    for value in watch_frequency.values():
        if value > most_watched_rate:
            most_watched_rate = value
    most_watched = list(watch_frequency.keys())[list(watch_frequency.values()).index(most_watched_rate)]
    return most_watched


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    friends_list = []
    user_list = []
    unique_list = []
    for i in range(len(user_data["friends"])):
        for movie in user_data["friends"][i]["watched"]:
            friends_list.append(movie)
    for movie in user_data["watched"]:
        user_list.append(movie)
    for movie in user_list:
        if movie not in friends_list:
            unique_list.append(movie)
    return unique_list

def get_friends_unique_watched(user_data):
    friends_list = []
    user_list = []
    unique_list = []
    for i in range(len(user_data["friends"])):
        for movie in user_data["friends"][i]["watched"]:
            if movie not in friends_list:
                friends_list.append(movie)
    for movie in user_data["watched"]:
        user_list.append(movie)
    for movie in friends_list:
        if movie not in user_list:
            unique_list.append(movie)
    return unique_list


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recs= []
    movies = get_friends_unique_watched(user_data)
    for movie in movies:
        if movie["host"] in user_data["subscriptions"]:
            recs.append(movie)
    return recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recs = []
    fav_genre = get_most_watched_genre(user_data)
    movies = get_friends_unique_watched(user_data)
    for movie in movies:
        if movie["genre"] == fav_genre:
            recs.append(movie)
    return recs
