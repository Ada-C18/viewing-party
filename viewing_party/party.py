#test 
# ------------- WAVE 1 --------------------
#funtion with three parameters
def create_movie(title, genre, rating):
    if title and genre and rating:
        dict = {}
        dict["title"] = title
        dict["genre"] = genre
        dict["rating"] = rating
        # print(dict)
        return dict

    if not title or not genre or not rating:
        # print(dict)
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

def get_friends_unique_watched(user_data):
    unique = []
    users_movies = []
    friends_movies = []
    for movie in user_data["watched"]:
        users_movies.append(movie)

    for movie in user_data["friends"]:
        for item in movie["watched"]:
            friends_movies.append(item)
            
    for item in friends_movies:
        if item not in users_movies:
            if item not in unique:
                unique.append(item)
    
    return unique
# 
# ------------- WAVE 4 -------------

def get_available_recs(user_data):
    unique = []
    users_movies = []
    friends_movies = []
    for movie in user_data["watched"]:
        users_movies.append(movie)

    for movie in user_data["friends"]:
        for item in movie["watched"]:
            friends_movies.append(item)
            
    for item in friends_movies:
        if item not in users_movies:
            if item not in unique:
                if item["host"] in user_data["subscriptions"]:
                    unique.append(item)
    
    return unique

# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    most_genre = []
    unique = []
    users_movies = []
    friends_movies = []
    
    for movie in user_data["watched"]:
        users_movies.append(movie)
        most_genre.append(movie["genre"])

    if len(users_movies) == 0:
        return friends_movies
    the_max = max(set(most_genre), key= most_genre.count)
    for movie in user_data["friends"]:
        for item in movie["watched"]:
            friends_movies.append(item)
            
    for item in friends_movies:
        if item not in users_movies:
            if item not in unique:
                if item["host"] in user_data["subscriptions"]:
                    if most_genre[0] in item["genre"]:
                        unique.append(item)
    
    return unique

def get_rec_from_favorites(user_data):
    unique = []
    users_movies = []
    friends_movies = []
    
    for movie in user_data["watched"]:
        users_movies.append(movie)


    if len(users_movies) == 0:
        return friends_movies

    for movie in user_data["friends"]:
        for item in movie["watched"]:
            friends_movies.append(item)
            
    for item in user_data["favorites"]:
        if item not in friends_movies:
            unique.append(item)
    
    return unique