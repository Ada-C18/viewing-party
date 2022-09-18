# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # check to see if parameters are true
    # conditional for each paramter 
    # add parameters to a dictionary if true
    # create a dictionary
    # append to dictionary if true, NONE if false
    # return dictionary

    movie = {}
    if title == None or genre == None or rating == None:
        return None
    else:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie

def add_to_watched(user_data, movie):
    watched =[]
    watched.append(movie)
    user_data["watched"] = watched

    return user_data

def add_to_watchlist(user_data, movie):
    watchlist = []
    watchlist.append(movie)
    user_data["watchlist"] = watchlist

    return user_data

def watch_movie(user_data, title):
# need to see if the title is in the usersdata
# if movie in WATCHLIST then remove the movie from watchlist and add to watched, return
# if movie not in watchlist, return
    # for i in user_data['watchlist'][i]:
    for i in range(len(user_data['watchlist'])):
        if user_data['watchlist'][i]['title'] == title:
            user_data['watched'].append(user_data['watchlist'][i])
            user_data['watchlist'].remove(user_data['watchlist'][i])
            # user_data['watched'].append(user_data['watchlist'][i])
            return user_data
        
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def average(lst):
    return sum(lst) / len(lst)

def get_watched_avg_rating(user_data):
    rating_list = []
    for watched_list in user_data.values():
        for movie in watched_list:
            rating_list.append(movie['rating'])
    

    if rating_list:
        return average(rating_list)
    else:
        return 0.0

def get_most_watched_genre(user_data):
    most_watched_genre_dict = {}
    for watched_list in user_data.values():
        for movie in watched_list:
            genre = movie['genre']
            if genre not in most_watched_genre_dict:
                most_watched_genre_dict[genre] = 1
            else:
                most_watched_genre_dict[genre] += 1
    # max_val = list(most_watched_genre_dict.values())
    # max_key = list(most_watched_genre_dict.keys())
    # most_watched_genre = max_key[max_val.index(max(max_val))]

    if most_watched_genre_dict:
        max_val = list(most_watched_genre_dict.values())
        max_key = list(most_watched_genre_dict.keys())
        return max_key[max_val.index(max(max_val))]
    else:
        return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

