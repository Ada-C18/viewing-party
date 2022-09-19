# ------------- WAVE 1 --------------------

from sys import breakpointhook


def create_movie(title, genre, rating):
    
    movie = {}
    
    if not title or not genre or not rating:
        return None
    else:    
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
    
    return movie

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data['watchlist']
    watched = user_data['watched']
    i = 0

    for movie in watchlist:        
        if watchlist[i]['title'] == title:
            watchlist.remove(movie)
            watched.append(movie)
            
            user_data['watchlist'] = watchlist
            user_data['watched'] = watched
            return user_data
        else:
            i += 1
    else:
        return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total_rating = 0.0
    avg_rating = 0.0
    watched = user_data['watched']

    if watched:
        for movie in watched:
            total_rating += movie['rating']
        
        avg_rating = total_rating / len(watched)
    
    return avg_rating

def get_most_watched_genre(user_data):
    watched = user_data['watched']
    genre_names = set()
    genre_dict = {}

    # because we don't know the genres that the user has watched, \
    # we have to determine what these are and initialize the dictionary \
    # before we can increment the genres.

    if watched:
        for movie in watched:
            genre_names.add(movie['genre'])
        
        for genre in genre_names:
            genre_dict[genre] = 0
        
        for movie in watched:
            for genre in genre_names:
                if movie['genre'] == genre:
                    genre_dict[genre] += 1
        return max(genre_dict, key = genre_dict.get)

    else:
        return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    watched = user_data['watched']
    friends = user_data['friends']
    title_genre = tuple()
    user_watched = set()
    friend_watched = set()
    user_friend_unique = set()
    unique_movies = []

    # we want to ensure uniqueness by grabbing/comparing both title and genre
    # we want to have a clean comparison by not grabbing rating

    if watched:
        
        for movie in watched:
            title_genre = movie['title'], movie['genre']
            user_watched.add(title_genre)
        
        user_unique_set = user_watched

        if friends:
            for friend in friends:
                for movie in friend['watched']:
                    title_genre = movie['title'], movie['genre']
                    friend_watched.add(title_genre)
                user_friend_unique = user_watched - friend_watched
                user_unique_set = user_unique_set & user_friend_unique

        for movie in watched:
            for entry in user_unique_set:
                if entry == (movie['title'], movie['genre']):
                    unique_movies.append(movie)

    return unique_movies

def get_friends_unique_watched(user_data):
    watched = user_data['watched']
    friends = user_data['friends']
    title_genre = tuple()
    user_watched = set()
    friend_watched = set()
    friend_user_unique = set()
    friends_unique_set = set()
    friends_all_movies = []
    friends_unique_movies = []

    # we want to ensure uniqueness by grabbing/comparing both title and genre
    # we want to have a clean comparison by not grabbing rating

    if len(watched):
        
        for movie in watched:
            title_genre = movie['title'], movie['genre']
            user_watched.add(title_genre)

        if friends:
            for friend in friends:
                for movie in friend['watched']:
                    title_genre = movie['title'], movie['genre']
                    friend_watched.add(title_genre)
                    friends_all_movies.append(movie)
                
                friend_user_unique = friend_watched-user_watched
                friends_unique_set = friends_unique_set | friend_user_unique

        if friends_unique_set:
            for movie in friends_all_movies:
                for entry in friends_unique_set:
                    if entry == (movie['title'], movie['genre']):
                        if movie in friends_unique_movies:
                            continue
                        else:
                            friends_unique_movies.append(movie)

    return friends_unique_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    subscriptions = user_data['subscriptions']
    available_recs = []

    friends_unique = get_friends_unique_watched(user_data)

    if friends_unique:
        for movie in friends_unique:
            if movie['host'] in subscriptions:
                available_recs.append(movie)

    return available_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

