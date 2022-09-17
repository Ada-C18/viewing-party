# ------------- WAVE 1 --------------------

from operator import length_hint


def create_movie(title, genre, rating):
    movie = {}
    # check if the parameters are truthy
    if title and genre and rating :
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie
    else :
        return None


def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data  


def add_to_watchlist(user_data, movie) :
    user_data["watchlist"].append(movie)     
    return user_data


def watch_movie(user_data, title):

    for movie in user_data["watchlist"]:
        if movie["title"] == title :
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            
    return user_data
        






# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum = 0
    average = 0
    length = len(user_data["watched"])
    for i in range(length):
        sum += user_data["watched"][i]["rating"]
        average = sum / length

    return average   


def get_most_watched_genre(user_data):
    genre_dict = {}
    length = len(user_data["watched"])
    if length > 0 :
        for i in range(length):
            genre = user_data["watched"][i]["genre"]
            if genre in genre_dict.keys():
                genre_dict[genre] +=1
            else :
                genre_dict[genre] = 1

        
        genre_list = []
        for k, v in genre_dict.items():
            genre_list.append((v, k))
        genre_list.sort(reverse = True)
        return genre_list[0][1]
    else :
        return None
         


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def converting_list_of_dict_to_set(user_list_of_movies):
    user_set = set()
    length = len(user_list_of_movies)
    for i in range(length):
        user_set.add(user_list_of_movies[i]["title"])
    return user_set


def get_unique_watched(user_data):
    user_watched_set = converting_list_of_dict_to_set(user_data["watched"])
    friends_watched_sets = set()
    length = user_data["friends"]
    user_list_of_uniques = []
    for i in range(len(length)):
        friend_watched_set = converting_list_of_dict_to_set(user_data["friends"][i]["watched"])
        user_watched_set = user_watched_set - friend_watched_set

    for i in range(len(user_data["watched"])):
        if user_data["watched"][i]["title"] in user_watched_set :
            user_list_of_uniques.append(user_data["watched"][i])


    return user_list_of_uniques  



    
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


