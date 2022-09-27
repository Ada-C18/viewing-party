# ------------- WAVE 1 --------------------

from pickle import FALSE


def create_movie(title, genre, rating):
    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
    information = [title, genre, rating]
    if None in information:
        return None
    else:
        return new_movie
    
def add_to_watched(user_data, movie):

    user_data = {}
    user_data["watched"] = [movie]
    
    return user_data

def add_to_watchlist(user_data,movie):
    user_data = {}
    user_data["watchlist"] = [movie]

    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    
            return user_data    
    return user_data    
# -----------------------------------------

# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    average_rating = 0
    list_sum = []
    for i in user_data["watched"]:
        if i["rating"] == 0:
            return 0.0
        if i["rating"]:
            list_sum.append(i["rating"])
        average_rating = sum(list_sum) / len(user_data["watched"])
    return average_rating

def get_most_watched_genre(user_data):
    # loop through movies in watched and take out the most popular genre
    # add to dict and use a counter 
    genre_dict = {}

    if len(user_data["watched"]) == 0:
        return None
    else:
        for movie in user_data["watched"]:
            genre = movie["genre"]
            if genre not in genre_dict:
                genre_dict[genre] = 1
            else:
                genre_dict[genre] += 1

    #loop through genre_dict and have 2 variables (count,genre)
    most_genre_count = 0
    most_genre = ""
    for genre, genre_times in genre_dict.items():
        if genre_times > most_genre_count:
            most_genre = genre
            most_genre_count = genre_times


    return most_genre
        
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def  get_unique_watched(user_data):
    unique_list = []
    friends_watched = get_friends_watched(user_data)
    for i in user_data["watched"]:
        if i not in friends_watched or i not in unique_list:
            unique_list.append(i)
    print(unique_list)
    return unique_list

def get_friends_watched(user_data):
    friends_watched = []
    for friend in user_data["friends"]:
        for movies in friend.values():
            for movie in movies:
                friends_watched.append(movie)
    return friends_watched

def get_friends_unique_watched(user_data):
    friends_watched = get_friends_watched(user_data)
    friends_unique = []
    for movie in friends_watched:
        if movie not in user_data["watched"] or movie not in friends_unique:
            friends_unique.append(movie) 
    return friends_unique       
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

