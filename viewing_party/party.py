def create_movie(title, genre, rating):
    new_movie = {
        "title": title, 
        "genre": genre, 
        "rating": rating
    }
    if not title or not genre or not rating:
        new_movie = None
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie_to_watch):
    for i in range(len(user_data["watchlist"])):
        if movie_to_watch in user_data["watchlist"][i]["title"]:
            del user_data["watchlist"][i]
            user_data["watched"].append(movie_to_watch)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):

    total_rating = 0
    count = len(user_data["watched"])
    if user_data["watched"]:
        for i in range(count):
            total_rating += user_data["watched"][i]["rating"]
        return total_rating/count
    else:
        return 0

def get_most_watched_genre(user_data):
    rating = {}
    if not user_data["watched"]:
        return None
    else:
        for i in range(len(user_data["watched"])):
            genre_name = user_data["watched"][i]["genre"]
            if genre_name not in rating:
                rating[genre_name] = 1
            else: 
                rating[genre_name] += 1
            popular = [(value, key) for key, value in rating.items()]
        return max(popular)[1]

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_friend_watched_movies(user_data):
    friends_watched_movies = []
    for friens_dict in user_data["friends"]: 
        # print(f"{item=}") 
        for friend_list in friens_dict["watched"]:
            friends_watched_movies.append(friend_list)
    return friends_watched_movies

def get_unique_watched(user_data):
    my_unique_movies = []
    friends_watched_movies = get_friend_watched_movies(user_data)
    # .append() seems more efficient
    for my_movie in user_data["watched"]:
        if my_movie not in friends_watched_movies:
            my_unique_movies.append(my_movie)
    return my_unique_movies
    # .remove() method:
    # for my_movie in user_data["watched"]:
    #     my_unique_movies.append(my_movie)
    # # print(f"{my_unique_movies=}")
    # for item in friends_watched_movies:
    #     if item in my_unique_movies:
    #         my_unique_movies.remove(item)
    # # print(f"{my_unique_movies=}")
    # return my_unique_movies
    
def get_friends_unique_watched(user_data): 
    friends_watched_movies = get_friend_watched_movies(user_data)
    my_watched_movies = user_data["watched"]
    friends_unique_movies = []

    for friends_item in friends_watched_movies: 
        # print(f"{item=}") 
        if friends_item not in friends_unique_movies and friends_item not in my_watched_movies:
            friends_unique_movies.append(friends_item)
    return friends_unique_movies
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friends_unique_movies = get_friends_unique_watched(user_data)
    my_host = user_data["subscriptions"]
    my_available_movies = []
    for friends_item in friends_unique_movies:
        if friends_item["host"] in my_host:
            my_available_movies.append(friends_item)
    return my_available_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    friends_unique_movies = get_friends_unique_watched(user_data)
    my_watched_movies = user_data["watched"]
    my_genre = {}
    recommended_movies = [] 
    for my_movie in my_watched_movies:
        if my_movie["genre"] not in my_genre:
            my_genre[my_movie["genre"]] = 1
        else: 
            my_genre[my_movie["genre"]] += 1
    if len(my_watched_movies) >0 and len(my_genre) > 0:
        my_freq_genre = max(my_genre, key = my_genre.get)
        for movies in friends_unique_movies:
            if movies["genre"] == my_freq_genre:
                recommended_movies.append(movies)
        return recommended_movies
    else:
        return recommended_movies

def get_rec_from_favorites(user_data):
    my_favorites_movies = user_data["favorites"]
    friends_watched_movies = get_friend_watched_movies(user_data)
    recommended_movies = []

    for my_favorites_item in my_favorites_movies:
        if my_favorites_item not in friends_watched_movies:
            recommended_movies.append(my_favorites_item)
    return recommended_movies




