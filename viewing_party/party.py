# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    dict_movie={
        "title": title,
        "genre": genre,
        "rating": rating
    }
    for key in dict_movie:
        if not dict_movie[key]:
            return None
    return dict_movie
def add_to_watched(the_user_data, movie_watched):
    the_user_data["watched"].append(movie_watched)
    return the_user_data

def add_to_watchlist(the_user_d, movie_to_watch):
    the_user_d["watchlist"].append(movie_to_watch)
    return the_user_d
def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
            if movie["title"] == title:
                user_data["watched"].append(movie)
                i  = user_data["watchlist"].index(movie)
                user_data["watchlist"].pop(i)
                return user_data
    else:
        return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user):

    sum_rating = 0.0
    if not user["watched"]:
            return sum_rating
    for movie in user["watched"]:
        sum_rating += movie["rating"]
        
    return sum_rating / len(user["watched"])
            
def get_most_watched_genre(user):
    dict_most_genre = {}
    most_genre_val = 0

    most_genre = []
    if not user["watched"]:
        return None
    for movie in user["watched"]:
        
        if movie["genre"] not in dict_most_genre:
            dict_most_genre[movie["genre"]] = 1
        else:
            dict_most_genre[movie["genre"]] +=1
    for genre, val in dict_most_genre.items():
        if val > most_genre_val:
            most_genre_val = val
    for genre in dict_most_genre:
        if dict_most_genre[genre] == most_genre_val:
            most_genre.append(genre)
    return ''.join(most_genre)
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    #first I want to access the dictionary and the "watched" list
    list_compare = []
    list_friends = friend_list_of_user(user_data)
    for movie in user_data["watched"]:
        if movie not in list_friends:
            list_compare.append(movie)
    return list_compare
def friend_list_of_user(user_data):
    list_friends = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in list_friends:
                list_friends.append(movie)
    return list_friends

        
def get_friends_unique_watched(user_data):
    list_compare = []
    list_friends = friend_list_of_user(user_data)
    for movie in list_friends:
        if movie not in user_data["watched"]:
            list_compare.append(movie)
    return list_compare
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user):
    recommended_list = []
    movies_unique = get_friends_unique_watched(user)
    for movie in movies_unique:
        if movie["host"] in user["subscriptions"]:
            recommended_list.append(movie)
    return recommended_list
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user):
    user_most_freq_genre = get_most_watched_genre(user)
    list_recommened_movies = get_friends_unique_watched(user)
    list_rec_by_genre = []
    for movie in list_recommened_movies:
        if movie["genre"] == user_most_freq_genre:
            list_rec_by_genre.append(movie)
    return list_rec_by_genre

def get_rec_from_favorites(user):
    user_unique = get_unique_watched(user)
    list_rec_from_fav = []
    for movie in user_unique:
        if movie in user["favorites"]:
            list_rec_from_fav.append(movie)
    return list_rec_from_fav
