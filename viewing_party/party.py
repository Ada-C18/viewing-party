# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {
        "title" : title,
        "genre" : genre,
        "rating": rating
    }

    if new_movie["title"] and new_movie["genre"] and new_movie["rating"]:
         return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data = {
        "watched" : [movie]
    }
    return user_data
    
def add_to_watchlist(user_data, movie):
    user_data = {
        "watchlist" : [movie]
    }
    return user_data

def watch_movie(user_data, title):
    # watchlist = user_data["watchlist"]
    for movie in user_data["watchlist"]:
    # if the title is in a movie in the user's watchlist:
        if title  == movie["title"]:
            print(f"debug: title in movie dict")
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            # return the user_data

    print(f"debug: title not in movie dict")
    return user_data
        
        
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    average_rating = 0.0
    sum_ratings = 0
    # The average rating of an empty watched list is 0.0
    if user_data["watched"] == []:
        average_rating = 0.0
        return average_rating

    # Calculate the average rating of all movies in the watched list
    for movie in range(len(user_data["watched"])):
        sum_ratings += user_data["watched"][movie]["rating"]

    average_rating = sum_ratings / len(user_data["watched"])

    return average_rating
    



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
