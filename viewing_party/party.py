# ------------- WAVE 1 --------------------

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(title, genre, rating):
    new_movie = {}


    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie
    else: 
        return None

    
def add_to_watched(user_data, movie):
    user_data = {"watched": []}
    
    movie = {
        "title": MOVIE_TITLE_1,
        "genre": GENRE_1,
        "rating": RATING_1
    }

    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {"watchlist": []}
    movie = {
    "title": MOVIE_TITLE_1,
    "genre": GENRE_1,
    "rating": RATING_1
    }
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):

    
    for key, value in user_data.items():
        if key == "watchlist":
            for i in value:
                for key, value in i.items():
                    if value == title:
                        user_data["watched"].append(title)
                        user_data["watchlist"].remove(i)
        else:
            return user_data
        
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_total = []

    for i in user_data["watched"]:
        rating_total.append(i["rating"])
    if len(rating_total) != 0:
        return sum(rating_total)/len(rating_total)
    else: 
        return 0.0


def get_most_watched_genre(user_data):
 
    popular_genre = []
    for i in user_data["watched"]:
        popular_genre.append(i["genre"])
    if len(popular_genre) != 0:
        return max(set(popular_genre), key = popular_genre.count)
    else: 
        return None
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friends_movie_list = []
    my_movie_list = []
    third_list = []

    for i in user_data["friends"]:
        for movie in i["watched"]:
            friends_movie_list.append(movie)
    for i in user_data["watched"]:
        my_movie_list.append(i)

    for movie in my_movie_list:
        if movie not in friends_movie_list:
            third_list.append(movie)

    return third_list


def get_friends_unique_watched(user_data):
    friends_movie_list = []
    my_movie_list = []
    third_list = []

    for i in user_data["watched"]:
        my_movie_list.append(i)
    for friend in user_data["friends"]:
        for other in friend["watched"]:
            friends_movie_list.append(other)

    for movie in friends_movie_list:
        if movie not in my_movie_list:
            if movie not in third_list:
                third_list.append(movie)
    return third_list
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    final_list = []
    
    for movie in user_data["friends"]:
        for i in movie["watched"]:
            if i["host"] in user_data["subscriptions"]:
                recommended_movies.append(i)
    for option in recommended_movies:
        if option not in user_data["watched"]:
            final_list.append(option)
    return final_list 
    

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    recommended_movies = []
    genre = []
    final_list = []
    genre_dict = {}

    if user_data["watched"]:
        for i in user_data["watched"]:
            genre.append(i["genre"])
    else:
        return final_list
        

    for i in genre:
        if True:
            if i in genre_dict:
                genre_dict[i] += 1
            else:
                genre_dict[i] = 1
       

    genre_dict_sorted = sorted(genre_dict, key=genre_dict.get, reverse=True)
    most_common_genre = genre_dict_sorted[0]

    for movie in user_data["friends"]:
        for i in movie["watched"]:
            if i["genre"] == most_common_genre:
                recommended_movies.append(i)
    for option in recommended_movies:
        if option not in user_data["watched"]:
            final_list.append(option)
    return final_list

def get_rec_from_favorites(user_data):
    recommended_movies = []
    final_list = []
    for movie in user_data["friends"]:
        for value in movie.values():
            for i in value:
                recommended_movies.append(i)
  
    for favorite in user_data["favorites"]:
        if favorite not in recommended_movies:
            final_list.append(favorite)
    return final_list