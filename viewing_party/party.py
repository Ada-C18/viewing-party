# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    movie = {
        "title": title,
        "genre": genre,
        "rating":rating
    }
    return movie

def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    list_of_movies = user_data["watchlist"]
    for i in range(len(list_of_movies)):
        if list_of_movies[i]["title"]==title:
            add_to_watched(user_data,list_of_movies[i]) 
            #user_data["watched"].append(list_of_movies[i])
            user_data["watchlist"].remove(list_of_movies[i])
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    average = 0
    sum = 0
    list_of_movies = user_data["watched"]

    if len(list_of_movies) == 0:
        return 0

    for i in range(len(list_of_movies)):
        sum += list_of_movies[i]["rating"]

    average = sum / len(list_of_movies)
    return average


def get_most_watched_genre(user_data):
    list_of_movies = user_data["watched"]

    if len(list_of_movies) == 0:
        return None
    
    counter_dict ={}
    for i in range(len(list_of_movies)):
        if list_of_movies[i]["genre"] not in counter_dict:
            counter_dict[list_of_movies[i]["genre"]] = 1
        else:
            counter_dict[list_of_movies[i]["genre"]] += 1

    popular_genre = max(counter_dict, key = counter_dict.get)
    return popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    #user data has a friends list which has dictionaries
    movies_watched = user_data["watched"]
    friends_movies = user_data["friends"]
    unique_movies = []
    for i in range(len(movies_watched)):
        add_to_new_list = True
        for j in range(len(friends_movies)):
            for watched in friends_movies[j]:
                for k in range(len(friends_movies[j][watched])):
                    if movies_watched[i]["title"] == friends_movies[j][watched][k]["title"]:
                        add_to_new_list = False
        if add_to_new_list == True:
            unique_movies.append(movies_watched[i])
    return unique_movies




def get_friends_unique_watched(user_data):
    movies_watched = user_data["watched"]
    friends_movies = user_data["friends"]
    unique_movies = []
 
    for i in range(len(friends_movies)):
        for watched in friends_movies[i]:
            for j in range(len(friends_movies[i][watched])):
                add_to_new_list = True
                for k in range(len(movies_watched)):
                    if movies_watched[k]["title"] == friends_movies[i][watched][j]["title"]:
                        add_to_new_list = False
                if add_to_new_list == True and friends_movies[i][watched][j] not in unique_movies:
                    unique_movies.append(friends_movies[i][watched][j])
    return unique_movies
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    movies_watched= user_data["watched"]
    friends_movies = user_data["friends"]
    sub_options = user_data["subscriptions"]
    avail_recs = []

    for i in range(len(friends_movies)):
        for watched in friends_movies[i]:
            for j in range(len(friends_movies[i][watched])):
                add_to_new_list = True
                for k in range(len(movies_watched)):
                    if movies_watched[k]["title"]== friends_movies[i][watched][j]["title"]:
                        add_to_new_list = False
                if add_to_new_list == True and friends_movies[i][watched][j]["host"] not in sub_options:
                    add_to_new_list = False
                if add_to_new_list == True and friends_movies[i][watched][j] not in avail_recs:
                   avail_recs.append(friends_movies[i][watched][j])
    return avail_recs



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    most_watched_genre = get_most_watched_genre(user_data)
    movies_watched= user_data["watched"]
    friends_movies = user_data["friends"]
    avail_recs = []

    for i in range(len(friends_movies)):
        for watched in friends_movies[i]:
            for j in range(len(friends_movies[i][watched])):
                add_to_new_list = True
                for k in range(len(movies_watched)):
                    if movies_watched[k]["title"]== friends_movies[i][watched][j]["title"]:
                        add_to_new_list = False
                if add_to_new_list == True and friends_movies[i][watched][j]["genre"] != most_watched_genre:
                    add_to_new_list = False
                if add_to_new_list == True and friends_movies[i][watched][j] not in avail_recs:
                   avail_recs.append(friends_movies[i][watched][j])
    return avail_recs

def get_rec_from_favorites(user_data):
    unique_movie = get_unique_watched(user_data)
    #fav_movie_recs =[]
    fav_movies = user_data["favorites"]
    
    # for i in range(len(fav_movies)):
    #     for j in range(len(unique_movie)):
    #         if fav_movies[i]["title"] == unique_movie[j]["title"]:
    #             fav_movie_recs.append(unique_movie[j])
    # return fav_movie_recs

    fav_movie_recs = [unique_movie[j] for i in range(len(fav_movies)) for j in range(len(unique_movie)) if fav_movies[i]["title"] == unique_movie[j]["title"]]
    return fav_movie_recs