# ------------- WAVE 1 --------------------

from enum import unique


def create_movie(title, genre, rating):
    dict = {}
    if title and genre and rating:
        dict['title'] = title
        dict['genre'] = genre
        dict['rating'] = rating
        return dict
    else:
        return None

def add_to_watched(user_data, movie):
    #user_data = {'watched': []}
    #movie = {'title': "Title A", "genre": "Horror", "rating": 3.5}
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    #user_data = {'watchlist': []}
    #movie = {"title": "Title A", "genre": "Horror", "rating": 3.5}
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    #user_data = {"watchlist": [], "watched": []}
    #title = ""
    watchlist = user_data['watchlist']
    for watchlist_movie in watchlist:
        if title == watchlist_movie['title']:
            movie = watchlist_movie
            result = add_to_watched(user_data, movie)
            print('Result:', result)
            user_data['watchlist'].remove(watchlist_movie)
            
            return result
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    avg_rating = 0.0
    rating_sum = 0.0
    watched = user_data['watched']
    if len(watched) != 0:
        for movie in watched:
            rating_sum += movie['rating']
        avg_rating = rating_sum/len(watched)
    return avg_rating

def get_most_watched_genre(user_data):
    genre_counter = {}
    watched = user_data['watched']
    most = ''
    if len(watched) != 0:
        for movie in watched:
            if movie['genre'] in genre_counter.keys():
                genre_counter[movie['genre']] += 1
            else:
                genre_counter[movie['genre']] = 0
        most = max(genre_counter, key = genre_counter.get)
        return most

    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friends_watched = []
    friends_movies = user_data['friends']
    user_unique = []
    for watched_list in friends_movies:
        for friend_movie in watched_list['watched']:
            friends_watched.append(friend_movie['title'])
    # print('Friend Watched:', friends_watched, '\n')
    for user_movie in user_data['watched']:
        if user_movie['title'] not in friends_watched:
            user_unique.append(user_movie)
    # print('User:', user_data['watched'], '\n')
    # print('User Unique: ', user_unique)
    return user_unique


def get_friends_unique_watched(user_data):
    #user_data = {"watched": [{"title"}], "friends": [{"watched": ["title"]}]}
    unique_movies = []
    unique_movies_titles = []
    watched_movies = []
    friends_movies = user_data['friends']
    # print('Friends:', friends_movies)
    
    #go through friends watched list
        #if friends watched list movie title is a title that does not exists in personal watched list
            #add that dict to unique_movies

    for user_movie in user_data['watched']:
        watched_movies.append(user_movie['title'])
    #print('Watched Movies: ', watched_movies, '\n')
    for watched_list in friends_movies:
        for friend_movie in watched_list['watched']:
            #print('friend_movie:', friend_movie)
            if friend_movie['title'] not in watched_movies:
                if friend_movie['title'] not in unique_movies_titles:
                    unique_movies.append(friend_movie)
                    unique_movies_titles.append(friend_movie['title'])
    # print('Unique Movies:', unique_movies)
    # print('Unique Movie Titles:', unique_movies_titles)
    return unique_movies
    #return unique_movies
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    movie_recs = []
    subscriptions = user_data['subscriptions']
    watched_movies = []
    for user_movie in user_data['watched']:
        watched_movies.append(user_movie['title'])
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie['title'] not in watched_movies:
                if movie['host'] in user_data['subscriptions']:
                    movie_recs.append(movie)
    return movie_recs
    #user_data = {"friends": [{"watched": ["title"]}], 'subscriptions': ['', ''], watched}


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    fav_genre = get_most_watched_genre(user_data)
    movie_recs = []
    watched_movies = []
    for user_movie in user_data['watched']:
        watched_movies.append(user_movie['title'])
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie['title'] not in watched_movies:
                if movie['genre'] == fav_genre:
                    movie_recs.append(movie)
    return movie_recs

def get_rec_from_favorites(user_data):
    friends_watched = []
    friends_movies = user_data['friends']
    movie_recs = []
    fav_movies = []
    for watched_list in friends_movies:
        for friend_movie in watched_list['watched']:
            friends_watched.append(friend_movie['title'])
    for fav_movie in user_data['favorites']:
        fav_movies.append(fav_movie['title'])
    for movie in user_data['watched']:
        if movie['title'] in fav_movies and movie['title'] not in friends_watched:
            movie_recs.append(movie)
    return movie_recs

