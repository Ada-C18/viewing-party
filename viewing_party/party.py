# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None

    movie_dict = {}
    movie_dict["title"] = title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating

    return movie_dict

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
    list_of_ratings = []
    for movie in user_data["watched"]:
        list_of_ratings.append(movie["rating"])

    sum = 0
    for num in list_of_ratings:
        sum += num

    try:
        avg = sum / len(list_of_ratings)
    except ZeroDivisionError:
        avg = 0
    
    return avg

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None

    genre_dict = {}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in genre_dict.keys():
            genre_dict[genre] += 1
        else:
            genre_dict[genre] = 1

    largest_count = max(genre_dict.values())

    for (genre, count) in genre_dict.items():
        if largest_count == count:
            return genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_movies_user_watched(user_data):

    movies_user_watched = []
    for movie in user_data["watched"]:
        movies_user_watched.append(movie["title"])
    return movies_user_watched

def get_movies_friends_watched(user_data):
    movies_friends_watched = []
    friend_data = user_data["friends"]
    for friend in friend_data:
        for movie in friend["watched"]:
            movies_friends_watched.append(movie["title"])
    
    return movies_friends_watched

def get_unique_watched(user_data):

    watched_by_user = get_movies_user_watched(user_data)
    watched_by_friends = get_movies_friends_watched(user_data)

    unique_watched_titles = []
    for my_movie in watched_by_user:
        if my_movie not in watched_by_friends:
                unique_watched_titles.append(my_movie)

    unique_watched_dicts = []
    for title in unique_watched_titles:
        for movie in user_data["watched"]:
            if title == movie["title"]:
                unique_watched_dicts.append(movie)

    return unique_watched_dicts
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

