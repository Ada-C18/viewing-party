# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    if not title or not genre or not rating:
        return None

    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating

    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watch_list = user_data["watchlist"]
    for i in range(len(watch_list)):
        if title == watch_list[i]["title"]:
            user_data["watched"].append(watch_list[i])
            del watch_list[i]
    
    return user_data




# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    movie_list = user_data["watched"]
    total_rating = 0
    if len(movie_list) == 0:
        return 0
    for movie in movie_list:
        total_rating += movie["rating"]

    return total_rating / len(movie_list)

def get_most_watched_genre(user_data):
    movie_list= user_data["watched"]
    genre_count = {}
    if len(movie_list) == 0:
        return None
    for movie in movie_list:
        genre = movie["genre"]
        if genre not in genre_count:
            genre_count[genre] = 1
        else:
            genre_count[genre] += 1
      
    return max(genre_count, key=genre_count.get)



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    list_watched = (user_data["watched"])
    if list_watched == []:
        return []

    list_friend_1 = user_data["friends"][0]["watched"]
    list_friend_2 = user_data["friends"][1]["watched"]
    list_friends = list_friend_1 + list_friend_2
    unique = [i for i in list_watched if i not in list_friends]

    return unique

def get_friends_unique_watched(user_data):
    list_watched = (user_data["watched"])
    if list_watched == []:
        return []

    list_friend_1 = user_data["friends"][0]["watched"]
    list_friend_2 = user_data["friends"][1]["watched"]
    list_friends = list_friend_1 + list_friend_2
    friends_unique = [i for i in list_friends if i not in list_watched]
    friends_unique = [dict(t) for t in {tuple(d.items()) for d in friends_unique}]

    return friends_unique

    

    
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    rec_list = []
    list_watched = (user_data["watched"])
    if list_watched == []:
        return []

    list_friend_1 = user_data["friends"][0]["watched"]
    list_friend_2 = user_data["friends"][1]["watched"]
    list_friends = list_friend_1 + list_friend_2
    friends_unique = [i for i in list_friends if i not in list_watched]
    friends_unique = [dict(t) for t in {tuple(d.items()) for d in friends_unique}]

    for movie in friends_unique:
        if movie["host"] in user_data["subscriptions"]:
            rec_list.append(movie)
    
    return rec_list





# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    rec_list = []
    genre_count = {}
    list_watched = (user_data["watched"])
    if list_watched == []:
        return []

    for movie in list_watched:
        genre = movie["genre"]
        if genre not in genre_count:
            genre_count[genre] = 1
        else:
            genre_count[genre] += 1  
    most_watched_genre = max(genre_count, key=genre_count.get)

    list_friend_1 = user_data["friends"][0]["watched"]
    list_friend_2 = user_data["friends"][1]["watched"]
    list_friends = list_friend_1 + list_friend_2
    friends_unique = [i for i in list_friends if i not in list_watched]
    friends_unique = [dict(t) for t in {tuple(d.items()) for d in friends_unique}]

    for movie in friends_unique:
        if movie["genre"] == most_watched_genre:
            rec_list.append(movie)
    
    return rec_list


def get_rec_from_favorites(user_data):
    if len(user_data["friends"]) == 0:
        list_friend_1 = []
        list_friend_2 = []
    else:
        list_friend_1 = user_data["friends"][0]["watched"]
        list_friend_2 = user_data["friends"][1]["watched"]
    list_friends = list_friend_1 + list_friend_2
    rec_list = [i for i in user_data["favorites"] if i not in list_friends]
    
    return rec_list

