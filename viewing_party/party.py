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

    for items in user_data["watchlist"]:
        if title in user_data["watchlist"]:
            user_data["watched"].append(user_data["watchlist"][0])
            user_data["watchlist"].pop(0)
        return user_data

# def add_to_watched(user_data, movie):
#     movies_watched = []
#     updated_data = []

#     for items in len(user_data)["movie"]:
#         if movie not in user_data:
#             user_data["watched"].append(updated_data[movies_watched])
#         return updated_data

        



# make a dictionary with these keys above
#title:title, genre:genre, rating:rating

#-----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


#THIS TEST PASSED AND THEN STOPPED PASSING_ I"M NOT SURE WHY< BUT I DID NOT HAVE TIME TO FIX IT
def get_watched_avg_rating(user_data):
    ratings = []
    ratings_sum = 0
    if(len(user_data["watched"])) is 0:
        ratings_average = 0.0
    else:
        for i in range(len(user_data["watched"])):
            ratings.append((user_data["watched"][i]["rating"]))
            i+=1
        for rating in ratings:
            ratings_sum += rating
    ratings_average = ratings_sum / len(ratings)
    return ratings_average

def get_watched_avg_rating(user_data):
    ratings = []
    ratings_sum = 0
    if(len(user_data["watched"])) is 0:
        ratings_average = 0.0
    return ratings_average

def get_most_watched_genre(user_data):
    genre_list = []
    genre_dictionary = {}

    if (len(user_data["watched"])) is 0:
        popular_genre = None
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


def get_unique_watched(user_data):


    watched = user_data["watched"]
    friends = user_data["friends"]
    unique_movies = []
    # movies_user_watched = watched(user_data)
    # movies_friend_watched = friends(user_data)


    watched.set(watched)
    friends.set(friends)

    for movie in watched:
        if movie == (movie["title"], movie["genre"]):
            unique_movies.append(movie)

        return unique_movies

def get_unique_friends_watched(user_data):
    friends_unique_movies = []

    friends_unique_movies



        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):



    

def get_rec_from_favorites(user_data):

