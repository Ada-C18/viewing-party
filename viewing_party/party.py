# ------------- WAVE 1 --------------------

# 1.1
def create_movie(title, genre, rating):
    if title and genre and rating:
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


# # 1.3
def add_to_watchlist(user_data, movie):
    user_data["watched"].append(movie)
    return user_data
    

# # 1.4
# def watch_movie(user_data, title):
#     user_data: {"watchlist", "watched"},
#     title: ""

# If the title is in a movie in the user's watchlist:
# remove that movie from the watchlist
# add that movie to watched
# return the user_data
# If the title is not a movie in the user's watchlist:
# return the user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

