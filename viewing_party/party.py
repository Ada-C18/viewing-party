#test 
# ------------- WAVE 1 --------------------
#funtion with three parameters
def create_movie(title, genre, rating):
    if title and genre and rating:
        dict = {}
        dict["title"] = title
        dict["genre"] = genre
        dict["rating"] = rating
    #   print(dict)
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
def get_unique_watched(user_data):
    #creat a set of movies friends have watched:
    friend_set = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_set.add(movie["title"])
    #creat a unique list of movies:
    unique_list = []
    for movie in user_data["watched"]:
        if movie["title"] not in friend_set:
            unique_list.append(movie)
    return unique_list

    


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

