# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # make a dictionary with keys: 'title': title, 'genre': genre, 'rating': rating)
    movie = {}

    if title and genre and rating:
        movie['title'] = title
        movie['genre'] = genre
        movie['rating'] = rating
    else:
        return None
    return movie

def add_to_watched(user_data, movie):
    # add movie dict to value at key watched
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, movie):
    watchlist = user_data['watchlist']
    watched = user_data['watched']
    # print(watchlist)
    # print(watched)
    
    for movie in watchlist:
            watchlist.remove(movie)
            watched.append(movie)
    # print(watchlist)
    # print(watched)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):
    watched_list = user_data['watched']
    average_rating_sum = 0.0

    if len(watched_list) < 1:
        average_rating = 0.0
    else:
        for movie in watched_list:
            average_rating_sum += movie['rating']
            average_rating = average_rating_sum / len(watched_list)
    return average_rating


def get_most_watched_genre(user_data):
    watched_list = user_data['watched']

    frequency = {}

    if len(watched_list) < 1:
        return None
    else:
        for movie in watched_list:
            genre = movie['genre']
            # print(genre)
            if genre in frequency:
                frequency[genre] += 1
            else:
                frequency[genre] = 1
        # print(frequency)
        most_watched_genre = max(frequency, key = frequency.get)
        # get the largest value at the KEY "genre"
        # print(most_watched_genre)
        return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):

    friend_list = []
    user_list =[]
    movie_list = []

    friends = user_data['friends']
    for friend in friends:
        for movie in friend['watched']:
            friend_list.append(movie)

    for movie in user_data['watched']:
        user_list.append(movie)
    
    for movie in user_list:
        if movie not in friend_list:
            movie_list.append(movie)
    
    # print(movie_list)
    return movie_list

def get_friends_unique_watched(user_data):

    friend_list = []
    user_list =[]
    movie_list = []

    friends = user_data['friends']
    for friend in friends:
        for movie in friend['watched']:
            friend_list.append(movie)

    for movie in user_data['watched']:
        user_list.append(movie)
    
    for movie in friend_list:
        if movie not in user_list:
            if movie in movie_list:
                continue
            else:
                movie_list.append(movie)
    
    return movie_list

        

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):

    user_subs = user_data['subscriptions']
    user_watched = user_data['watched']

    friends = user_data['friends']
    friends_watched = []

    for friend in friends:
        for movie in friend['watched']:
            friends_watched.append(movie)

    user_not_watched = []
    for movie in friends_watched:
        if movie not in user_watched:
            user_not_watched.append(movie)

    recommendations = []
    for movie in user_not_watched:
        if movie['host'] in user_subs:
            recommendations.append(movie)
    
    return recommendations



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

