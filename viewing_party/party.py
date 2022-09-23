# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}
    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating
    for key in new_movie:
        if new_movie[key] == None:
            return new_movie[key]
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in user_data["watchlist"]:
        for key in i:
            if key == "title" and i[key] == title:
                user_data["watched"].append(i)
                user_data["watchlist"].remove(i)
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    total_rating = 0
    if len(user_data["watched"]) == 0:
        return total_rating
    for i in user_data["watched"]:
        total_rating += i["rating"]
    rating_average = total_rating / len(user_data["watched"])
    return rating_average

def get_most_watched_genre(user_data):

    if len(user_data["watched"]) == 0:
        return None
    else:
        genre_list = []
        for i in user_data["watched"]:
            genre_list.append(i["genre"])
        return max(genre_list, key=genre_list.count)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_list = []
    watched_set = set()
    friend_set = set()
    for i in user_data["watched"]:
        watched_set.add(i["title"])
    for i in user_data["friends"]:
        for movie in i["watched"]:
            friend_set.add(movie["title"])
    difference_list = list(watched_set.difference(friend_set))
    for i in difference_list:
        for movie in user_data["watched"]:
            if i == movie["title"]:
                unique_list.append(movie)
    return unique_list

def get_friends_unique_watched(user_data):
    unique_list = []
    friend_set = set()
    user_set = set()
    for i in user_data['friends']:
        for movie in i['watched']:
            friend_set.add(movie['title'])
    for i in user_data["watched"]:
        user_set.add(i["title"])
    difference_list = list(friend_set.difference(user_set))
    for title in difference_list:
        for movie in user_data["friends"]:
            for x in movie["watched"]:
                if title == x["title"] and x not in unique_list:
                    unique_list.append(x)
    
    
    return unique_list
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    rec_list = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie not in user_data['watched'] and movie['host'] in user_data['subscriptions']:
                rec_list.append(movie)
    return rec_list
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    favorite_genre = get_most_watched_genre(user_data)
    rec_list = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie['genre'] == favorite_genre and movie['host'] in user_data['subscriptions'] and movie not in user_data['watched']:
                print(movie)
                rec_list.append(movie)
    return rec_list

def get_rec_from_favorites(user_data):
    rec_list = []
    friend_watched_list = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            friend_watched_list.append(movie)
    for favorite in user_data['favorites']:
        if favorite not in friend_watched_list:
            rec_list.append(favorite)   
    return rec_list