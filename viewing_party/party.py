# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):

    if title and genre and rating:
        dict = {}
        dict["title"] = title
        dict["genre"] = genre
        dict["rating"] = rating
        return dict

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

# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    sum = 0
    average = 0

    for i in range(len(user_data["watched"])):
        sum += user_data["watched"][i]["rating"]
        average = sum  / len(user_data["watched"])

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

# ------------- WAVE 3 --------------------

def get_unique_watched(user_data): 

    # create a set of movies that friends have watched: 
    # friend_set = set()
    # for friend in user_data["friends"]:
    #     for movie in friend["watched"]:
    #         friend_set.add(movie["title"])   # for sets is add

    # #breakpoint() 

    # unique_watched = []
    # for movie in user_data["watched"]:
    #     if movie["title"] not in friend_set:
    #         unique_watched.append(movie)

    # return unique_watched
    unique = []
    combined_movies = [] # users movies and friends movies
    users_movies = []
    friends_movies = []

    for movie in user_data["watched"]:
        users_movies.append(movie)

    for movie in user_data["friends"]:
        for item in movie["watched"]:
            friends_movies.append(item)

    combined_movies = users_movies + friends_movies

    for item in combined_movies:
        if item not in friends_movies:
            unique.append(item)
    return unique
    

#part 2:
def get_friends_unique_watched(user_data):

    # user_movies_list = []
    # for movie in user_data["watched"]:
    #     user_movies_list.append(movie)
    # #print(user_movies_list)
    # print(user_data)

    left_to_watch_by_user = []
    users_movies = []
    friends_movies = []

    for movie in user_data["watched"]:
        users_movies.append(movie)

    for movie in user_data["friends"]:
        for item in movie["watched"]:
            friends_movies.append(item)

    for item in friends_movies:
        if item not in users_movies:
            if item not in left_to_watch_by_user:
                left_to_watch_by_user.append(item)
    return left_to_watch_by_user

    # # friends_movies_list = []
    # # for friends in user_data["friends"]:
    # #     for key in friends["watched"]:
    # #         pass

    # friends_movies_list = user_data["friends"]

#     my_set = ()
#     for movie in user_data["watched"]:

# ------------- WAVE 4 -------------------
# -----------------------------------------

def get_available_recs(user_data):
    
    watched_movies = []

    for movie in user_data["watched"]:
        watched_movies.append(movie["title"])
    #print(watched_movies)    # list with names of movies
    

    recommended = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in watched_movies:
                if movie["host"] in user_data["subscriptions"]:
                    recommended.append(movie)

    return recommended


# ------------- WAVE 5 --------------------

def get_new_rec_by_genre(user_data):

    if len(user_data["watched"]) == 0:
        return user_data["watched"]

    genre_watched_by_user = []
    for movie in user_data["watched"]:
        genre_watched_by_user.append(movie["genre"])

    most_frequent = max(set(genre_watched_by_user), key= genre_watched_by_user.count)

    watched_movies = []
    for movie in user_data["watched"]:
        watched_movies.append(movie["title"])

    recommended_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in watched_movies:
                if movie["genre"] in most_frequent:
                    recommended_movies.append(movie)

    return recommended_movies

# part II
def get_rec_from_favorites(user_data):

    
    friends_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_list.append(movie["title"])

    recommended_movies = []
    for movie in user_data["favorites"]:
        if movie["title"] not in friends_list:
            recommended_movies.append(movie)

    return recommended_movies 

