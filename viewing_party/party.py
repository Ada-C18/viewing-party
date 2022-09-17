# ------------- WAVE 1 --------------------

from multiprocessing.sharedctypes import Value

from tests.test_constants import GENRE_1, MOVIE_TITLE_1, RATING_1


def create_movie(title, genre, rating):
    
    new_movie = {}
    if title and genre and rating:
        new_movie = {
            "title" : title,
            "genre" : genre,
            "rating" : rating
        }
        return new_movie
    return None

def add_to_watched(user_data, movie):
    user_data = {"watched" : [movie]}
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {"watchlist" :[movie]}
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
            return user_data
    return user_data






    # for value in user_data.values():
    #     for item in :
    #         return item 
    #         user_data["watched"].append(title)
    # return user_data
        # if user_data[key][0][item]["title"] == title:
        #     item +=1
        #     user_data[key][1].append(title)
    return user_data
    # for key, value in user_data.items():
    #     for item in user_data[item]["watchlist"]["title"]:
    #         if title in user_data[item]["watchlist"]["title"]:
    #             user_data["watched"].append(item)
    # for key,value in user_data.items():
    #     for 
    #         return title



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

