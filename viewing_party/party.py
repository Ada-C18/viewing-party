# ------------- WAVE 1 --------------------

# 1.1
def create_movie(title, genre, rating):
    if title and genre and (type(rating) == int or type(rating) == float):
        movie_dict = {
                "title": title,
                "genre": genre,
                "rating": rating
            }
        return movie_dict
    else:
        return None

# 1.2
def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


# 1.3
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data
    

# 1.4
def watch_movie(user_data, title):
    watchlist_list = user_data["watchlist"]
    watched_list = user_data["watched"]

    for movie in watchlist_list:
        if movie["title"] == title:
            watchlist_list.remove(movie)
            watched_list.append(movie)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# 2.1
def get_watched_avg_rating(user_data):
    user_data["watched"]  
    # find average of ratings in watched list - The average rating of an empty watched list is 0.0
    # return average_rating 






# 2.2
# def get_most_watched_genre(user_data):
#     user_data["watched"]
#     # Determine which genre(is a string) is most frequently occurring in the watched list
#     # return the genre that is the most frequently watched
#     # If the value of "watched" is an empty list, get_most_watched_genre should return None.






# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# # 3.1
# def get_unique_watched(user_data):
#     user_data["watched"]


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

