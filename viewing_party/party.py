# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    '''
    Create a dict containing info about one movie, with "title", "genre", and "rating", as keys, mapped to values passed in as arguments.
    '''
    if not title or not genre or not rating:
        return None

    movie = {}
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating

    return movie

def add_to_watched(user_data, movie):
    '''
    Add a movie to a user's list of watched movies
    '''
    # user_data = {"watched" : []}
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    Add a movie to a user's watchlist
    '''
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    '''
    Move a movie from watchlist to watched
    '''
    
    #I want to find the correct dict entry in watchlist given the value of "title", how do I do that?
    #Iterate over watchlist until watchlist["title"] == movie_title
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            watched_movie = movie
            user_data["watched"].append(watched_movie)
            user_data["watchlist"].remove(watched_movie)
    
    return user_data
    
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    ratings = []
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
    if not ratings:
        return 0
    
    return sum(ratings)/len(ratings)

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    genres = {}
    for movie in user_data["watched"]:
        if movie["genre"] not in genres:
            genres[movie["genre"]] = 1
        else:
            genres[movie["genre"]] += 1
    
    return max(genres, key = genres.get)
         
        
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    #user data is a dict that has two elements: friends (a list) and watched (a list)
    unique_movies = []
    for movie in user_data["watched"]:
        unique_movies.append(movie)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
              if movie in unique_movies:
                  unique_movies.remove(movie)
    return unique_movies
        
def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in friends_unique_movies:
                friends_unique_movies.append(movie)
    return friends_unique_movies
                
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    recs = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie["host"] in user_data["subscriptions"]:
                recs.append(movie)
    return recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    genre_recs = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie["genre"] == get_most_watched_genre(user_data):
                genre_recs.append(movie)
    return genre_recs

def get_rec_from_favorites(user_data):
    fav_recs = []
    for movie in user_data["favorites"]:
        fav_recs.append(movie)
    for friend in user_data["friends"]:
        for movie in fav_recs:
            if movie in friend["watched"]:
                fav_recs.remove(movie)
    return fav_recs

# test_data = {
#     "watchlist": [{"title": "foo",
#                             "genre": "scifi",
#                             "rating": 3}],
#              "watched": [{"title": "bar",
#                           "genre": "fantasy",
#                           "rating": 6}]
#     }

# # watch_movie(test_data, 1)
# get_watched_avg_rating(test_data)
# get_most_watched_genre(test_data)
# get_unique_watched(test_data)
# get_friends_unique_watched(test_data)

# #Wave 3 test data
# test_data = {   'friends': [   {   'watched': [   {   'genre': 'Fantasy',
#                                           'rating': 4.8,
#                                           'title': 'The Lord of the Functions: '
#                                                     'The Fellowship of the '
#                                                     'Function'},
#                                       {   'genre': 'Fantasy',
#                                           'rating': 4.0,
#                                           'title': 'The Lord of the Functions: '
#                                                     'The Return of the Value'},
#                                       {   'genre': 'Fantasy',
#                                           'rating': 4.0,
#                                           'title': 'The Programmer: An '
#                                                     'Unexpected Stack Trace'},
#                                       {   'genre': 'Horror',
#                                           'rating': 3.5,
#                                           'title': 'It Came from the Stack '
#                                                     'Trace'},
#                                         {   'genre': 'Intrigue',
#                                           'rating': 3.0,
#                                           'title': 'Zero Dark Python'}]},
#                     {   'watched': [   {   'genre': 'Fantasy',
#                                           'rating': 4.8,
#                                           'title': 'The Lord of the Functions: '
#                                                     'The Fellowship of the '
#                                                     'Function'},
#                                       {   'genre': 'Action',
#                                           'rating': 2.2,
#                                           'title': 'The JavaScript and the '
#                                                     'React'},
#                                       {   'genre': 'Intrigue',
#                                           'rating': 2.0,
#                                           'title': 'Recursion'},
#                                       {   'genre': 'Intrigue',
#                                           'rating': 3.0,
#                                           'title': 'Zero Dark Python'}]}],
#     'watched': [   {   'genre': 'Fantasy',
#                         'rating': 4.8,
#                         'title': 'The Lord of the Functions: The Fellowship of '
#                                 'the Function'},
#                     {   'genre': 'Fantasy',
#                         'rating': 4.0,
#                         'title': 'The Lord of the Functions: The Two '
#                                 'Parameters'},
#                     {   'genre': 'Fantasy',
#                         'rating': 4.0,
#                         'title': 'The Lord of the Functions: The Return of the '
#                                 'Value'},
#                     {   'genre': 'Action',
#                         'rating': 2.2,
#                         'title': 'The JavaScript and the React'},
#                     {'genre': 'Intrigue', 'rating': 2.0, 'title': 'Recursion'},
#                     {   'genre': 'Intrigue',
#                         'rating': 4.5,
#                         'title': 'Instructor Student TA Manager'}]}

# test_data.keys()
