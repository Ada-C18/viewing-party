# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_dict = {}
    new_dict["title"] = title
    new_dict["genre"] = genre
    new_dict["rating"] = rating
    for key in new_dict:
        if not new_dict[key]:
            return None
    return new_dict


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            i = user_data["watchlist"].index(movie)
            user_data["watchlist"].pop(i)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    rating_list=[]
    for movie in user_data["watched"]:
        if movie["rating"]> 0:
            rating_list.append(movie["rating"])
    
    rating_sum=sum(rating_list)
    ave_rating=rating_sum/len(rating_list)
    
    return ave_rating


# def get_most_watched_genre(user_data):
#     frequent_genre={}
#     for movie in user_data["watched"]:
#         # if genre in frequent_genre:
#             frequent_genre+= 1
#         else:
#             frequent_genre+=1
#         return frequent_genre
#     else:
#         return None


        

# def get_unique_watched(user_data):


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
