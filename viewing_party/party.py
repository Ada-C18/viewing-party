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
    for key in user_data:
        for i in range(len(user_data[key])):
            for category in i:
                if category == "rating":
                    sum += user_data[key][i][category]
    average = sum / 2
    return average

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------