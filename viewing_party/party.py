# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        new_movie = {}
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie
    if not title or not genre or not rating:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
    return user_data
        

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# my own work
def get_watched_avg_rating(user_data):
    count = 0
    average_rating = 0

    for i in range(len(user_data["watched"])):
        count += (user_data["watched"][i]["rating"])
        average_rating = count/len(user_data["watched"])
    return average_rating

def get_most_watched_genre(user_data):
    for i in range(len(user_data["watched"])):
        popular_genre = []
        if popular_genre == []:
            return None

"""
# THIS IS THE WORK OF A GROUP
def get_watched_avg_rating(user_data):
    sum = 0
    average = 0

    for i in range(len(user_data["watched"])):
        sum += (user_data["watched"][i]["rating"]) 
        average = sum/len(user_data["watched"])
    return average

def get_most_watched_genre(user_data):
    index = 0
    genres = []
    least_popular = []
    most_popular = []
    if user_data == {"watched":[]}:
        return None
    else:
        for movie in user_data["watched"]:
            index +=1
            genres.append(user_data["watched"][index-1]["genre"])
        for item in genres:
            if item not in least_popular:
                least_popular.append(item)
            else:
                most_popular.append(item)
        return (most_popular[0])
"""

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
'''
def get_unique_watched(user_data):
    # user data = dict("watched" & "friends")
    #Create a set of movies friends have watched

    # first attemp using a set
   
    friend_set = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_set.add(movie["title"])

    unique_list = []

    # 
    for movie in user_data["watched"]:
        if movie["title"] not in friend_set:
            unique_list.append(movie)

    return unique_list 
'''

    # second attempt using a list
# part 1
def get_unique_watched(user_data): # get a list of the movies that user has seen, and friend still has to see

    unique = []
    total_movies_list = [] # the addition of user movies and friend movies
    users_movies = []
    friends_movies = []

    for movie in user_data["watched"]:
        users_movies.append(movie) # the new value of user_movies

    for movie in user_data["friends"]: # iterating and get the dict of the friends
        for item in movie["watched"]: # iterate to the to the list of movies the friend has seen
            friends_movies.append(item) # new value of friends_movies

    total_movies_list = users_movies + friends_movies # add the new values of user_movies & friends_movies
#                                                       to total_movies_list (both user + friends)
    for item in total_movies_list: # iterate through total_movies_list
        if item not in friends_movies: # if the movie is not in the friend's movie list
            unique.append(item) # we add it to the list of the user_data["watched"]
    return unique

 # part 2   
def get_friends_unique_watched(user_data):
    # will need to access watched inside user_data
    user_movies= []
    friends_movies = []
    # create a new list left_to_watch
    left_to_watch = []
    
    # and compare it to friends["watched"]
    for movie in user_data["watched"]:
        user_movies.append(movie) #user_movies has a list of the movies the user has seen

    for movie in user_data["friends"]: # reaching into the list of dictionaries
        for item in movie["watched"]:
            friends_movies.append(item) # this is now a list of the friend's movies

    for item in friends_movies: # iterate through the list of friend's movies
        if item not in user_movies: # if movie in friends["watched"] is not in user_data["watched"]
            if item not in left_to_watch:
                left_to_watch.append(item)
    return left_to_watch
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    user_movies = []
    friends_movies = []
    unique = []

    for movie in user_data["watched"]: # this is to help create the user watch list
        user_movies.append(movie) #user_movies has a list of the movies the user has seen

    for movie in user_data["friends"]: # reaching into the list of dictionaries
        for item in movie["watched"]:
            friends_movies.append(item) # this is now a list of the friend's movies

    for item in friends_movies: # we are accesing the list we created of movies watched by friends
        if item not in user_movies: # it the friends movie is not in the movies the user has seen
            if item not in unique: # if that movie is also not in our list of unique movies, we add to unique
                if item["host"] in user_data["subscriptions"]: # if streaming service is in subscription
                    unique.append(item) # if streaming service is found, add to unique

    return unique


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    user_movies = []
    friends_movies = []
    most_genre = []
    recommended_movies = []

    for movie in user_data["watched"]: # this is to help create the user watch list
        user_movies.append(movie) #user_movies has a list of the movies the user has seen
        most_genre.append(movie["genre"]) # to get to the genre

    if len(user_movies) == 0:
        return friends_movies # if the list of user is completely empty

    max(set(most_genre), key=most_genre.count) # will get the most watched genre, will 
    # shorten the list to only one

    for movie in user_data["friends"]: # reaching into the list of dictionaries
        for item in movie["watched"]:
            friends_movies.append(item) # this is now a list of the friend's movies

    for item in friends_movies: # we are accesing the list we created of movies watched by friends
        if item not in user_movies: # it the friends movie is not in the movies the user has seen
            if item not in most_genre: # if that movie is also not in our list of unique movies, we add to unique
                if item["host"] in user_data["subscriptions"]: # if streaming service is in subscription
                    if most_genre[0] in item["genre"]: # if the most popular genre is in the friends dict list
                        recommended_movies.append(item) # if streaming service is found, add to recommended movies
    return recommended_movies

def get_rec_from_favorites(user_data):
    recommended_movies = []
    user_movies = []
    friend_movies = []

    for movie in user_data["watched"]: # this will add to the user movie list
        user_movies.append(movie)
 
    if len(user_movies) == 0:
        return friend_movies # if the list of user is completely empty

    for movie in user_data["friends"]: # this will add to the friend movies
        for item in movie["watched"]:
            friend_movies.append(item)

    for item in user_data["favorites"]: # this accesses favorites in the user data
        if item not in friend_movies: # if that favorite is not in friends movies
            recommended_movies.append(item) # append the item to the recommended movies
    return recommended_movies

    

                


