# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------

def create_movie(title, genre, rating):
    movie_dict = {}
    if title and genre and rating:
        movie_dict.update({"title": title})
        movie_dict.update({"genre": genre})
        movie_dict.update({"rating": rating})
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
    for movie_dict in user_data["watchlist"]:
        if movie_dict["title"] == title:
            user_data["watched"].append(movie_dict)
            user_data["watchlist"].remove(movie_dict)
            return user_data
    return user_data
    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_list = []
    rating_total = 0
    
    for movie in user_data["watched"]:
        if len(user_data["watched"]) == 0:
            movie["rating"] = 0.0
        rating_list.append(movie['rating'])
    
    for rating in rating_list:
        rating_total += rating
    
    if len(rating_list) == 0:
        return 0.0
    else:
        final_rating = rating_total / len(rating_list)
        return final_rating 

def get_most_watched_genre(user_data):
    genre_dict = {}
    if user_data["watched"] == []:
        return None
    for movie_dict in user_data["watched"]:
        if movie_dict["genre"] in genre_dict:
            genre_dict[movie_dict["genre"]] += 1
        else:
            genre_dict[movie_dict["genre"]] = 1
    best_genre = max(genre_dict, key=genre_dict.get)
    return best_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    user_watched_list = []
    friends_movie_list = []
    unique_user_watched = []
    for i in range(len(user_data["friends"])):
        for movie in user_data["friends"][i]["watched"]:
            friends_movie_list.append(movie)

    for i in range(len(user_data["watched"])):
        movie = user_data["watched"][i]
        user_watched_list.append(movie)
        
    for movie in user_watched_list:
        if movie not in friends_movie_list:
            unique_user_watched.append(movie)

    return unique_user_watched    
    
def get_friends_unique_watched(user_data):
    user_watched_list = []
    friends_movie_list = []
    friends_unique_watched = []
    result = {}
    new_list = []
    for i in range(len(user_data["friends"])):
        for movie in user_data["friends"][i]["watched"]:
            friends_movie_list.append(movie)

    for i in range(len(user_data["watched"])):
        movie = user_data["watched"][i]
        user_watched_list.append(movie)

    for movie in friends_movie_list:
        if movie not in user_watched_list and movie not in friends_unique_watched:
            friends_unique_watched.append(movie)
    
    # for movie in friends_unique_watched:
    #     for key, value in movie.items():
    #         if value not in result.values():
    #             result[key] = value
    #             new_list.append(result)

    
    return friends_unique_watched



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

