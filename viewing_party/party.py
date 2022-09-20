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

def get_watched_avg_rating(user_data):
    sum = 0
    average = 0

    for i in range(len(user_data["watched"])):
        sum += (user_data["watched"][i]["rating"])
        average = sum/len(user_data["watched"])
    return average

def get_most_watched_genre(user_data):
    # if user_data == {"watched": []}:
    #     return None
    # else:
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

def get_unique_watched(user_data):

    unique = []
    not_unique = []
    total_movies_list = []
    users_movies = []
    friends_movies = []

    for movie in user_data["watched"]:
        users_movies.append(movie)

    for movie in user_data["friends"]:
        for item in movie["watched"]:
            friends_movies.append(item)

    total_movies_list = users_movies + friends_movies

    for item in total_movies_list:
        if item not in friends_movies:
            unique.append(item)
        else:
            not_unique.append(item)
    return unique
    
# def get_friends_unique_watched(user_data):
    # will need to access watched inside user_data
    # user_list = []
    
    # and compare it to friends["watched"]
    # create a new list left_to_watch
    # left_to_watch = []
    # if movie in friends["watched"] is not in user_data["watched"]
    # we append to a list left_to_watch

    # returning a list of what the user_data["watched"] has not seen

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------