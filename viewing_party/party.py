# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title is None or genre is None or rating is None:
        return None
    else:
        movie_dict = {'genre': genre, 'rating': rating, 'title': title}
        return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"] += [movie]
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] += [movie]
    return user_data

def watch_movie(user_data, title):
    movie_index = 0

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data = add_to_watched(user_data, movie)
            user_data["watchlist"].pop(movie_index)
        
        movie_index += 1
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) == 0:
        return 0.0
    else:
        ratings_total = 0
        ratings_count = 0
        for movie in user_data["watched"]:
            ratings_total += movie["rating"]
            ratings_count +=1

        return ratings_total / ratings_count

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    else:
        genre_count = {}
        for movie in user_data["watched"]:
            if movie["genre"] in genre_count:
                genre_count[movie["genre"]] += 1
            else:
                genre_count[movie["genre"]] = 1

        return max(genre_count, key=genre_count.get)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique_watched = user_data["watched"].copy()

    for friend in user_data["friends"]:
        for user_movie in user_data["watched"]:
            if user_movie in friend["watched"] and user_movie in unique_watched:
                unique_watched.remove(user_movie)
    return unique_watched


def get_friends_unique_watched(user_data):
    friends_unique_watched = []

    for friend in user_data["friends"]:
        for friend_movie in friend["watched"]:
            if friend_movie not in user_data["watched"] and friend_movie not in friends_unique_watched:
                friends_unique_watched.append(friend_movie)
    
    return friends_unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

#def get_available_recs(user_data):
    #pass

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

