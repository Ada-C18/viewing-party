# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {}
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    rating_sum = 0
    num_watched = len(user_data["watched"])
    if num_watched == 0:
        return 0
    else:
        for movie in user_data["watched"]:
            rating_sum += movie["rating"]
        return rating_sum/num_watched

def get_most_watched_genre(user_data):
    genre_count_dict = {}
    if len(user_data["watched"]) == 0:
        return None
    else: 
        for movie in user_data["watched"]:
            if not movie["genre"] in genre_count_dict:
                genre_count_dict[movie["genre"]] = 1
            else:
                genre_count_dict[movie["genre"]] += 1
    most_watched_genre = max(genre_count_dict, key=genre_count_dict.get)
    return most_watched_genre
        

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique_watched = []
    friends_watched = []


    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)

    for movie in user_data["watched"]:
        if not movie in friends_watched:
            unique_watched.append(movie)

    return unique_watched

def get_friends_unique_watched(user_data):
    friends_unique_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if not movie in user_data["watched"]:
                if not movie in friends_unique_watched:
                    friends_unique_watched.append(movie)
    return friends_unique_watched

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommendations = []
    not_watched = []

    for friend in user_data["friends"]: 
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"] and movie not in recommendations:
                recommendations.append(movie)

    return recommendations


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

