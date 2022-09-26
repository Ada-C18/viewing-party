# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if  title and genre and rating:
        return {'title': title, 'genre': genre, 'rating': rating}
    else:
        return None

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie) 
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data['watchlist']:
        if movie['title'] == title:
            user_data['watched'].append(movie)
            i = user_data['watchlist'].index(movie)
            user_data['watchlist'].pop(i)
    return user_data
    
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum_for_avg = 0
    count = len(user_data['watched'])
    if count:
        for movie in user_data['watched']:
            sum_for_avg += movie['rating']
        return sum_for_avg/count
    else:
        return 0.0

def get_most_watched_genre(user_data):
    genre_freq ={}
    if user_data['watched']:
        for movie in user_data['watched']:
            genre = movie['genre']
            if genre in genre_freq:
                genre_freq[genre] += 1
            else:
                genre_freq[genre] = 1
    else: return None
    max_genre = max(genre_freq, key=genre_freq.get)
    return max_genre



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_watched = []
    friends_watched_titles = list(set([movie['title'] for friend in user_data['friends'] for movie in friend['watched']]))
    for movie in user_data['watched']:
        if movie['title'] not in friends_watched_titles:
            unique_watched.append(movie)
    return unique_watched

def get_friends_unique_watched(user_data):
    unique_watched = []
    user_watched = [movie['title'] for movie in user_data['watched']]
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie['title'] not in user_watched:
                unique_watched.append(movie)
    #removes duplicate dictionaries from unique watched
    unique_watched = [dict(t) for t in {tuple(movie.items()) for movie in unique_watched}] 
    return unique_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    available_recs = []
    users_host_list = user_data['subscriptions']
    unique_watched = get_friends_unique_watched(user_data)
    for movie in unique_watched:
        if movie['host'] in users_host_list:
            available_recs.append(movie)
    return available_recs
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recs_by_genre = []
    top_genre = get_most_watched_genre(user_data)
    unfiltered_recs = get_friends_unique_watched(user_data)
    for movie in unfiltered_recs:
        if movie['genre'] == top_genre:
            recs_by_genre.append(movie)
    return recs_by_genre

def get_rec_from_favorites(user_data):
    favorites = list(user_data['favorites'])
    recs =[]
    friends_with_duplicates = [movie for friend in user_data['friends'] for movie in friend['watched']]
    friends = [dict(t) for t in {tuple(movie.items()) for movie in friends_with_duplicates}]
    for movie in favorites:
        if movie not in friends:
            recs.append(movie)
    return recs