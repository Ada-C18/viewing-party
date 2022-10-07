# ------------- WAVE 1 --------------------

#from tkinter.tix import InputOnly

def create_movie(title, genre, rating):

    new_movie = {}
    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"]= genre
        new_movie["rating"]= rating
        return new_movie
    else:
        return None

def add_to_watched(user_data, movie):
    watched_movies = []

    user_data.append(movie)

    return user_data

def add_to_watched_list(user_data, movie):
    watchlist = []

    user_data.append(movie)

    return user_data

def watch_movie(user_data, title):
    updated_data = user_data.copy()

    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            updated_data["watched"].append(movie)
            updated_data["watchlist"].remove(movie)
    return updated_data


# make a dictionary with these keys above
#title:title, genre:genre, rating:rating

#-----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    ratings_sum = 0
    ratings_average = 0
    total_movies = 0
    if user_data["watched"]:
        for movie in user_data["watched"]:
            total_movies += 1
            ratings_sum += movie["rating"]
        ratings_average = ratings_sum/total_movies
    return ratings_average

def get_most_watched_genre(user_data):
    genre_list = []
    genre_dictionary = {}

    if (len(user_data["watched"])) is 0:
        return None
    else: 
        for i in range(len(user_data["watched"])):
            genre_list.append((user_data["watched"][i] ["genre"]))
            i+=1

    for genre in genre_list:
        count = genre_list.count(genre)
        genre_dictionary[genre] = count

    popular_genre = max(genre_dictionary, key=genre_dictionary.get)
    return(popular_genre)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# def get_unique_watched(user_data):


#     watched = user_data["watched"]
#     friends = user_data["friends"]
#     unique_movies = []
#     # movies_user_watched = watched(user_data)
#     # movies_friend_watched = friends(user_data)


#     watched.set(watched)
#     friends.set(friends)

#     for movie in watched:
#         if movie == (movie["title"], movie["genre"]):
#             unique_movies.append(movie)

#         return unique_movies

# def get_unique_friends_watched(user_data):
    # friends_movies = list_friends_movies(user_data)
    # user_not_watched = []
    # for not_watched in friends_movies:
    #     if not_watched not in user_data["watched"] and not_watched not in user_not_watched:
    #         user_not_watched.append(not_watched)
    #     return user_not_watched



        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
                recommended.append(movie)
    return recommended



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


# def get_new_rec_by_genre(user_data):



    

# def get_rec_from_favorites(user_data):

