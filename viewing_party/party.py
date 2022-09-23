# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    new_dict = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    return new_dict

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    movie_index = None
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]["title"] == title:
            movie_index = i

    if movie_index is not None:
        cur_movie = user_data["watchlist"][movie_index]
        del user_data["watchlist"][movie_index]
        user_data["watched"].append(cur_movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_sum = 0
    watched_list = user_data["watched"]
    for data in watched_list:
        rating_sum += data["rating"]
    rating_average = rating_sum / len("rating")
    return rating_average

def get_most_watched_genre(user_data):
    most_watched_dict = {}
    watched_list = user_data["watched"]
    if watched_list == []:
        return None
    for data in watched_list:
        if data["genre"] not in most_watched_dict:
            most_watched_dict[data["genre"]] = 1
        else:
            most_watched_dict[data["genre"]] += 1
    print(most_watched_dict)
    return max(most_watched_dict, key=most_watched_dict.get)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_watched_friends_unwatched_list = []
    for movie in user_data["watched"]:
        friend_watched_movie = False
        for friend in user_data["friends"]:
            if movie in friend["watched"]:
                friend_watched_movie = True
                break
        if not friend_watched_movie:
            user_watched_friends_unwatched_list.append(movie)
    
    return user_watched_friends_unwatched_list

def get_friends_unique_watched(user_data):
    friend_dict = {}
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_dict[movie["title"]] = movie

    friends_unique_watched = []
    for _, movie in friend_dict.items():
        if movie not in user_data["watched"]:
            friends_unique_watched.append(movie)
    return friends_unique_watched
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friend_dict = {}
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_dict[movie["title"]] = movie

    rec_list = []
    for _, movie in friend_dict.items():
        if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
            rec_list.append(movie)

    return rec_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    genre_counts = {}
    for movie in user_data["watched"]:
        if movie["genre"] not in genre_counts:
            genre_counts[movie["genre"]] = 0
        genre_counts[movie["genre"]] += 1
    max_genre_count = 0
    most_frequent_genre = None
    for genre, count in genre_counts.items():
        if count > max_genre_count:
            max_genre_count = count
            most_frequent_genre = genre 

    friend_dict = {}
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_dict[movie["title"]] = movie

    rec_list = []
    for _, movie in friend_dict.items():
        if movie not in user_data["watched"] and movie["genre"] == most_frequent_genre:
            rec_list.append(movie)

    return rec_list

def get_rec_from_favorites(user_data):
    friend_set = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_set.add(movie["title"])
    rec_list = []
    for movie in user_data["favorites"]:
        if movie["title"] not in friend_set:
            rec_list.append(movie)
    return rec_list