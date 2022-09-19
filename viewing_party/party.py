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

#note: there's got to be a better way to do this
def get_most_watched_genre(user_data):
    # get and store list of all genre values
    genre_total_list = []
    for movie in user_data["watched"]:
        genre_total_list.append(movie["genre"])
    # create set of genres (1 instance of each)
   # print(genre_total_list)
    genres = set(genre_total_list)
    #print(genres)
    # create dictionary of most frequent genres
    genre_frequencies = {}
    for genre in genres:
        for item in genre_total_list:
            if genre == item:
                try:
                    genre_frequencies[genre] += 1
                except KeyError: 
                    genre_frequencies[genre] = 1
    #print(genre_frequencies)
    # identify genre with highest frequency count
    most_popular_genre = None
    max_frequency = 0
    for genre, frequency in genre_frequencies.items():
        if frequency > max_frequency:
            most_popular_genre = genre
            max_frequency = frequency
    #print(most_popular_genre)
    return most_popular_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    # start with list of all movies user has watched
    movie_list = list(user_data["watched"])
    unique_movies = list(movie_list)
    friends = list(user_data["friends"])
    # compare against list of friend's watched moviews
    for my_movie in movie_list:
        #for friend in friends:
        for friend in friends:
            for friend_movie in friend["watched"]:
                if my_movie == friend_movie:
                    try:
                        unique_movies.remove(my_movie)
                    except ValueError: # handle a movie that's already been removed (necessary?)
                        continue
    return unique_movies

def get_friends_unique_watched(user_data):
    friend_movies = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.append(movie)
    unique_friend_movies = list(friend_movies)

    # remove movies shared between "me" and friends
    for my_movie in user_data["watched"]:
        for movie in friend_movies:
            if my_movie == movie:
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
    friend_movies = []
    
    for friend in user_data["friends"]:
        friend_movies += friend["watched"]

    non_unique_movies = list(friend_movies)
    unique_movies = get_friends_unique_watched(user_data)
    for movie in unique_movies:
        for friend_movie in friend_movies:
            if movie == friend_movies:
                non_unique_movies.remove(movie)
    

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

