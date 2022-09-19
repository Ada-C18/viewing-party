# ------------- WAVE 1 --------------------
# I re-download it

def create_movie(title, genre, rating):
    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating

    if movie_dict["title"] == None or movie_dict["genre"] == None or movie_dict["rating"] == None:
        return None
       
    return movie_dict

def add_to_watched(user_data, movie_dict):
    # "watched" is the key, the whole movie_dict as a value thta 
    # append into the user_data which is also a dictionary
    user_data["watched"].append(movie_dict)
    return user_data


def add_to_watchlist(user_data, movie_dict):
    user_data["watchlist"].append(movie_dict)
    return user_data


def watch_movie(user_data, title):  # this one can still improve
    # get the values from the user_data's "watchlist" key, and put them into a list
    watch_list = user_data["watchlist"]
    watch_list_size = len(watch_list)
    for i in range(watch_list_size):
        # try to use for movie in watch_list
        if watch_list[i]["title"] == title:
            movie = watch_list[i]
            add_to_watched(user_data, movie)
            watch_list.remove(movie) 
            return user_data
    return user_data



    




    



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

