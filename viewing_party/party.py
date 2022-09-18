# ------------- WAVE 1 --------------------

# from imp import new_module
# from turtle import title


from os import remove


def create_movie(title, genre, rating):
    new_movie = {"title": title,
            "genre": genre,
            "rating": rating}
    
    if new_movie["genre"] == None:
        return None
    if new_movie["rating"] == None:
        return None
    if new_movie["title"] == None:
        return None
    return new_movie

def add_to_watched(user_data, movie):
    user_data = {}
    user_data["watched"] = [movie]
    return user_data

def add_to_watchlist(user_data, movie):
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


def get_watched_avg_rating(user_data):
    # user_data = {}

    for i in user_data["watched"]:
        print(i["rating"])

    # return sum(user_data["watched"].values())/len(user_data["watched"].values())   

# ua = {"watched": 
#               [{"title": "movie_1", 
#                  "genre": "horror,
#                   "rating": 1.0} ,
#                      {"title": "movie_2", 
#                  "genre": "horror,
#                   "rating": 4.0}  ]
#              "watch_list":
                    {"title": "movie_1", 
#                  "genre": "horror,
#                   "rating": 4.0} 
# }

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