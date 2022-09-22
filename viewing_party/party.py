from collections import Counter


# ------------- WAVE 1 --------------------



def create_movie(title, genre, rating):
    if(isinstance(title, str)) and (isinstance(genre, str)) and isinstance(rating, (int, float)):
        new_movie = {}
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        
        return new_movie
    return None


def add_to_watched(user_data, movie):
    user_data["watched"] = []
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = []
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    if len(user_data["watchlist"]) > 0:
        for data in user_data["watchlist"]:          
            if title == data["title"]:
                user_data["watched"].append(data)
                user_data["watchlist"].remove(data)
                
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) > 0:
        rating = []
        for movie in user_data["watched"]:
            rating.append(movie["rating"])
        average_rating = sum(rating) / len(rating)
        return average_rating
    return 0

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) > 0:
        janes_count = {}
        for data in user_data["watched"]:
            if data["genre"] not in janes_count:
                janes_count[data["genre"]] = 1
            else:
                janes_count[data["genre"]] += 1
        # popular_genre = max(janes_count, key = janes_count.get)
        popular_genre = [key for key, value in janes_count.items() if value == max(janes_count.values())]
        return ", ".join(popular_genre)
    return None
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):

    user_movies_list = []
    friends_movies_list = []
    unique_user_movies = []

    for movie in user_data["watched"]:
        user_movies_list.append(movie)

    for data in user_data["friends"]:
        for movie in data["watched"]:
            if movie not in friends_movies_list:
                friends_movies_list.append(movie)

    for movie in user_data["watched"]:
        if movie not in friends_movies_list:
            unique_user_movies.append(movie)

    return unique_user_movies

def get_friends_unique_watched(user_data):

    user_movies_list = []
    friends_movies_list = []
    unique_friend_movies = []

    for movie in user_data["watched"]:
        user_movies_list.append(movie)

    for data in user_data["friends"]:
        for movie in data["watched"]:
            if movie not in friends_movies_list:
                friends_movies_list.append(movie)

    for movie in friends_movies_list:
        if movie not in user_movies_list:
            if movie not in unique_friend_movies:
                unique_friend_movies.append(movie)

    return unique_friend_movies

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    unique_friend_movies = get_friends_unique_watched(user_data)
    recommendations = []

    for movie in unique_friend_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommendations.append(movie)

    return recommendations
    
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):

    unique_friend_movies = get_friends_unique_watched(user_data)
    user_genre_list = []
    recommendations = []

    for movie in user_data["watched"]:
        user_genre_list.append(movie["genre"])

    user_genre_dict = Counter(user_genre_list)
    
    if len(user_genre_list) == 0:
        user_genre = 0
    else:
        user_genre = user_genre_dict.most_common(1)[0][0]
    
    for movie in unique_friend_movies:
        if movie["genre"] == user_genre:
            recommendations.append(movie)

    return recommendations

def get_rec_from_favorites(user_data):
    recommendations = []
    unique_user_movies = get_unique_watched(user_data)

    for movie in unique_user_movies:
        if movie in user_data["favorites"]:
            recommendations.append(movie)

    return recommendations



