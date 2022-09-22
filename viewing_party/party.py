# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    return {"title": title, "genre": genre, "rating": rating}

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_sum = 0
    counter = 0
    try:
        for movie in user_data["watched"]:
            rating_sum += movie["rating"]
            counter += 1
        return rating_sum / counter
    except ZeroDivisionError:
        return 0

def get_most_watched_genre(user_data):
    # get and store list of all genre values
    genre_total_list = []
    for movie in user_data["watched"]:
        genre_total_list.append(movie["genre"])
    # create dictionary of most frequent genres
    genre_frequencies = {}
    for genre in genre_total_list:
        try:
            genre_frequencies[genre] += 1
        except KeyError: 
            genre_frequencies[genre] = 1
    # identify genre with highest frequency count
    most_popular_genre = None
    max_frequency = 0
    for genre, frequency in genre_frequencies.items():
        if frequency > max_frequency:
            most_popular_genre = genre
            max_frequency = frequency
    return most_popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    # start with list of all movies user has watched
    movie_list = list(user_data["watched"])
    unique_movies = list(movie_list)
    # compare against list of friend's watched movies
    friends = list(user_data["friends"])
    for friend in friends:
        for friend_movie in friend["watched"]:
            if friend_movie in movie_list:
                try:
                    unique_movies.remove(friend_movie)
                #handle a movie that's already been removed
                except ValueError: 
                    continue
    return unique_movies

def get_friends_unique_watched(user_data):
    #create list of movies friends have watched
    friend_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.append(movie)
    unique_friend_movies = list(friend_movies)
    # remove movies shared between user and friends
    for movie in friend_movies:
        if movie in user_data["watched"]:
            try:
                unique_friend_movies.remove(movie)
            except ValueError:
                continue
    # remove duplicates from unique_movie_list
    truely_unique_friend_movies = []
    for movie in unique_friend_movies:
        if not movie in truely_unique_friend_movies:
            truely_unique_friend_movies.append(movie)
    return truely_unique_friend_movies

def friends_not_unique_movies(user_data):
    # find movies all friends have seen
    friend_movies = []   
    for friend in user_data["friends"]:
        friend_movies += friend["watched"]
    non_unique_movies = list(friend_movies)
    # find all unique friend movies
    unique_movies = get_friends_unique_watched(user_data)
   # remove unique movies from friend watch list
    for movie in friend_movies:
        if movie in unique_movies:
            non_unique_movies.remove(movie)
    return non_unique_movies  

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    friend_movies = get_friends_unique_watched(user_data)
    recommended_movies = []
    for movie in friend_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recs_by_genre =[]
    fave_genre = get_most_watched_genre(user_data)
    friend_movies = get_friends_unique_watched(user_data)
    for movie in friend_movies:
        if movie["genre"] == fave_genre:
            recs_by_genre.append(movie)
    return recs_by_genre

def get_rec_from_favorites(user_data):
    rec_favorites = []
    friends_watched = friends_not_unique_movies(user_data)
    for movie in user_data["favorites"]:
        if not movie in friends_watched:
            rec_favorites.append(movie)      
    return rec_favorites