# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {}
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict
    return None


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    for movie in watchlist:
        if title == movie["title"]:
            # will remove it from same list in location in memory
            watchlist.remove(movie)
            user_data["watched"].append(movie)
            break
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_total = 0
    watched_lst = user_data["watched"]
    watched_lst_length = len(watched_lst)

    if watched_lst_length == 0:
        return 0.0

    for movie in watched_lst:
        rating_total += movie["rating"]
    return rating_total / watched_lst_length


def get_most_watched_genre(user_data):
    user_watched_lst = user_data["watched"]
    genre_dict = {}

    for movie in user_watched_lst:
        genre = movie["genre"]
        if genre in genre_dict:
            genre_dict[genre] += 1
        else:
            genre_dict[genre] = 1
    
    most_freq_genre = (None, 0)
    for genre in genre_dict:
        genre_count = genre_dict[genre]
        if genre_count > most_freq_genre[1]:
            most_freq_genre = (genre, genre_count)

    return most_freq_genre[0]


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    watched_lst = user_data["watched"]
    friends_lst = user_data["friends"]
    unique_watched_lst = []

    for movie in watched_lst:
        if not one_friend_has_seen(movie, friends_lst):
            unique_watched_lst.append(movie)

    return unique_watched_lst

    # Another Solution
    # for movie in watched_lst:
    #     seen_movie = False
    #     for friend in friends_lst:
    #         if movie in friend["watched"]:
    #             seen_movie = True
        
    #     if seen_movie == False:
    #         unique_watched_lst.append(movie)


def get_friends_unique_watched(user_data):
    user_watched_lst = user_data["watched"]
    friends_lst = user_data["friends"]

    user_not_watched = []

    for friend in friends_lst:
        for movie in friend["watched"]:
            if movie not in user_watched_lst and movie not in user_not_watched:
                user_not_watched.append(movie)

    return user_not_watched


#  Helper to check if movie watched by at least one friend 
def one_friend_has_seen(movie, friendList): 
    for friend in friendList:
        if movie in friend["watched"]:
            return True
    return False
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    user_watched_lst = user_data["watched"]
    friends_lst = user_data["friends"]
    subscriptions = user_data["subscriptions"]
    
    recommended_movies = []

    for friend in friends_lst:
        for movie in friend["watched"]:
            if movie not in user_watched_lst and movie["host"] in subscriptions and movie not in recommended_movies:
                recommended_movies.append(movie)

    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    user_watched_lst = user_data["watched"]
    friends_lst = user_data["friends"]

    recommended_movies = []
    most_freq_genre = get_most_watched_genre(user_data)

    for friend in friends_lst:
        for movie in friend["watched"]:
            if movie not in user_watched_lst and movie["genre"] == most_freq_genre and movie not in recommended_movies:
                recommended_movies.append(movie)

    return recommended_movies


def get_rec_from_favorites(user_data):
    friends_lst = user_data["friends"]
    users_favorites = user_data["favorites"]

    rec_from_favorites = list(users_favorites)

    for friend in friends_lst:
        for movie in friend["watched"]:
            if movie in rec_from_favorites:
                rec_from_favorites.remove(movie)

    return rec_from_favorites