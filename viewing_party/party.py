# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    movie = {
        "title": title,
        "genre": genre,
        "rating":rating
    }
    return movie

def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    #user_data["watched"].append(user_data["watchlist"][1]
    #user_data["watchlist"].popuser_data["watchlist"][0])
    list_of_movies = user_data["watchlist"]
    for i in range(len(list_of_movies)):
        if list_of_movies[i]["title"]==title: 
            user_data["watched"].append(list_of_movies[i])
            user_data["watchlist"].remove(list_of_movies[i])
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    average = 0
    sum = 0
    list_of_movies = user_data["watched"]

    if len(list_of_movies) == 0:
        return 0

    for i in range(len(list_of_movies)):
        sum += list_of_movies[i]["rating"]

    average = sum / len(list_of_movies)
    return average


def get_most_watched_genre(user_data):
    list_of_movies = user_data["watched"]

    if len(list_of_movies) == 0:
        return None
    
    counter_dict ={}
    for i in range(len(list_of_movies)):
        if list_of_movies[i]["genre"] not in counter_dict:
            counter_dict[list_of_movies[i]["genre"]] = 1
        else:
            counter_dict[list_of_movies[i]["genre"]] += 1

    popular_genre = max(counter_dict, key = counter_dict.get)
    return popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    pass
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------