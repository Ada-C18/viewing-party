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
def get_unique_watched(user_data):
    # create a list of movies watched by the user
    # create a list of movies watched by the friends
    # compare list of movies by user to movies by friend
    # return list of movies only watched by user
    # create a new unique list of movies watched by user
    user_movie_list = user_watched_list(user_data)
    friends_movie_list = friends_watched_list(user_data)
    unique_movie_list = []

    for movie in user_movie_list:
        if movie not in friends_movie_list:
            unique_movie_list.append(movie)
    return unique_movie_list

def get_friends_unique_watched(user_data):
    user_movie_list = user_watched_list(user_data)
    friends_movie_list = friends_watched_list(user_data)
    friends_unique_movie_list = []

    for movie in friends_movie_list:
        # print("********************")
        # print("movie", movie)
        if movie not in user_movie_list:
            if movie not in friends_unique_movie_list:
                friends_unique_movie_list.append(movie)
        # print("UNIQUE LIST:", friends_unique_movie_list)
        # print("*******************")
    return friends_unique_movie_list
    
# HELPER FUNCTION
def user_watched_list(user_data):
    user_watched_list = []
    for movie in user_data["watched"]:
        user_watched_list.append(movie)
    return user_watched_list

# HELPER FUNCTION
def friends_watched_list(user_data):
    friends_watched_list = []
    for friend_movie_dict in user_data["friends"]:
        for movie_dict in friend_movie_dict["watched"]:
            for value in movie_dict.items():
                if value not in friends_watched_list:
                    friends_watched_list.append(movie_dict)
    return friends_watched_list
    # return friends_watched_list
    # for i in range(len(user_data["friends"])): # i to signifiy variable of the watched_list for friends
    #     friends_watched_dict = i
    #     for movie in friends_watched_dict["watched"]:
    #         friends_watched_list.append(movie)
    # for movie in user_data["friends"]["watched"]:
       
  





        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

