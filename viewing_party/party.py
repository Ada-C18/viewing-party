# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating): #Wave 1, step 1 done
    movie_dict={}
    if title is None or genre is None or rating is None:
        return None

    movie_dict["title"]=title
    movie_dict["genre"]=genre
    movie_dict["rating"]=rating
    # print(movie_dict["title"])
    return movie_dict
# create_movie('tit','gen',5)

def add_to_watched(user_watched_dict,movie_info):
    user_watched_dict["watched"] = [movie_info]
    return user_watched_dict

def add_to_watchlist(user_watchlist_dict, movie_info):
    user_watchlist_dict["watchlist"] = [movie_info]
    return user_watchlist_dict

def watch_movie(single_user_data,movie_title):    
    list_of_watchlist_movie_info=single_user_data["watchlist"]
    list_of_watched_movie_info=single_user_data["watched"]

    for index,movie_info in enumerate(list_of_watchlist_movie_info):
        if movie_title == movie_info["title"]:
            list_of_watched_movie_info.append(movie_info)
            list_of_watchlist_movie_info.pop(index)
    return single_user_data


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

