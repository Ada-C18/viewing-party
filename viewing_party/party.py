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

    if len(watched):
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

    if len(watched):
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

    if len(watched):
        
        for movie in watched:
            title_genre = movie['title'], movie['genre']
            user_watched.add(title_genre)
        
        user_unique_set = user_watched

        if len(friends):
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


# # the function below creates a list of all movies watched by the user, \
# # where each movie appears only once, even if the movie was watched more than once \
# # by the user, but this was not what the test wanted.

# def get_unique_watched(user_data):
#     watched = user_data['watched']
#     title_genre = tuple()
#     movie_titles_genres = set()
#     initial_set_length = 0
#     new_set_length = 0
#     i = 0
#     index_list = []
#     unique_movies = []

# # sometimes movies that are different have the same title, \
# # so to ensure uniqueness, we don't want to use only titles 

#     if len(watched):
#         for movie in watched:
#             initial_set_length = len(movie_titles_genres)
#             title_genre = movie['title'], movie['genre']
#             movie_titles_genres.add(title_genre)
#             new_set_length = len(movie_titles_genres)

#             if new_set_length > initial_set_length:
#                 index_list.append(i)

#             i += 1

#         for number in index_list:
#             unique_movies.append(watched[number])

#     return unique_movies


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

