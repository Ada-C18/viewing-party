# ------------- WAVE 1 --------------------
from collections import Counter

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {
            "title" : title,
            "genre" : genre,
            "rating" : rating
        }
        return movie
    else:
        return None

# takes a movie dict and adds it to watched
def add_to_watched(user_data, movie):
    user_data["watched"] = [movie]
    return user_data

# takes a movie dict and adds it to watchlist
def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]
    return user_data

# finds the title of a movie in watchlist, then removes and transfers it to watched
def watch_movie(user_data, title):
    counter = 0
    for movie in user_data["watchlist"]:
        if title in movie["title"]:
            user_data["watched"].append(movie)
            del(user_data["watchlist"][counter])
        # if title in user_data["watchlist"]:
            # how to remove the title from the watchlist
            # movie_seen = user_data["watchlist"].pop(title)
            # movie_seen = user_data.pop("watchlist")
            # user_data["watched"][movie] = [movie_seen]
            return user_data
        counter += 1  
    return user_data     


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    rating = 0
    for movie in user_data["watched"]:
        rating += movie["rating"]
    if rating == 0:
        return 0
    else:
        avg_rating = rating / len(user_data["watched"])
        return avg_rating

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    horror_counter = 0
    fantasy_counter = 0
    action_counter = 0
    intrigue_counter = 0
    for movie in user_data["watched"]:
        if movie["genre"] == "Horror":
            horror_counter += 1
        elif movie["genre"] == "Fantasy":
            fantasy_counter += 1
        elif movie["genre"] == "Action":
            action_counter += 1
        elif movie["genre"] == "Intrigue":
            intrigue_counter += 1
    if horror_counter > fantasy_counter and horror_counter > action_counter and horror_counter > intrigue_counter:
        return "Horror"
    if fantasy_counter > horror_counter and fantasy_counter > action_counter and fantasy_counter > intrigue_counter:
        return "Fantasy"
    if action_counter > horror_counter and action_counter > fantasy_counter and action_counter > intrigue_counter:
        return "Action"
    if intrigue_counter > horror_counter and intrigue_counter > fantasy_counter and intrigue_counter > action_counter:
        return "Intrigue"

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    friend_movies = set()
    user_movies = set()
    unique_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.add(movie["title"])
    for movie in user_data["watched"]:
        user_movies.add(movie["title"])
    unique_titles = user_movies - friend_movies
    for movie in user_data["watched"]:
        if movie["title"] in unique_titles:
            unique_watched.append(movie)
    return unique_watched

def get_friends_unique_watched(user_data):
    friend_movies = set()
    user_movies = set()
    unique_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_movies.add(movie["title"])
    for movie in user_data["watched"]:
        user_movies.add(movie["title"])
    unique_titles = friend_movies - user_movies
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in unique_titles:
                if movie not in unique_watched:
                    unique_watched.append(movie)
    return unique_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recs = []
    friends_movies = get_friends_unique_watched(user_data)
    for movie in friends_movies:
        if movie["host"] in user_data["subscriptions"]:
            recs.append(movie)
    return recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# def get_new_rec_by_genre(user_data):
#     all_recs = get_available_recs(user_data)
#     genre_dict = {}
#     for movie in user_data["watched"]:
#         for genre in movie["genre"]:
#             if genre not in genre_dict:
#                 genre_dict[genre] = 1
#             else:
#                 genre_dict[genre] += 1
#     fav_genre = max(genre_dict)
#         counter = 0
#         # for genre in genre_dict:
#         #     if genre_dict[genre] > 

def get_new_rec_by_genre(user_data):
    rec_by_genre = []
    all_recs = get_available_recs(user_data)
    genre_list = list()
    try:
        for movie in user_data["watched"]:
            genre_list.append(movie["genre"])
        fav_genre = max(set(genre_list), key = genre_list.count)
        for movie in all_recs:
            if movie["genre"] == fav_genre:
                rec_by_genre.append(movie)
        return rec_by_genre
    except ValueError:
        return []

user_data = {   'favorites': [   {   'genre': 'Fantasy',
                        'host': 'netflix',
                        'rating': 4.8,
                        'title': 'The Lord of the Functions: The Fellowship '
                                'of the Function'},
                    {   'genre': 'Fantasy',
                        'host': 'netflix',
                        'rating': 4.0,
                        'title': 'The Lord of the Functions: The Two '
                                'Parameters'},
                    {   'genre': 'Intrigue',
                        'host': 'hulu',
                        'rating': 2.0,
                        'title': 'Recursion'},
                    {   'genre': 'Intrigue',
                        'host': 'disney+',
                        'rating': 4.5,
                        'title': 'Instructor Student TA Manager'}],
    'friends': [   {   'watched': [   {   'genre': 'Fantasy',
                                        'host': 'netflix',
                                        'rating': 4.8,
                                        'title': 'The Lord of the Functions: '
                                                'The Fellowship of the '
                                                'Function'},
                                    {   'genre': 'Fantasy',
                                        'host': 'amazon',
                                        'rating': 4.0,
                                        'title': 'The Lord of the Functions: '
                                                'The Return of the Value'},
                                    {   'genre': 'Fantasy',
                                        'host': 'hulu',
                                        'rating': 4.0,
                                        'title': 'The Programmer: An '
                                                'Unexpected Stack Trace'},
                                    {   'genre': 'Horror',
                                        'host': 'netflix',
                                        'rating': 3.5,
                                        'title': 'It Came from the Stack '
                                                'Trace'}]},
                {   'watched': [   {   'genre': 'Fantasy',
                                        'host': 'netflix',
                                        'rating': 4.8,
                                        'title': 'The Lord of the Functions: '
                                                'The Fellowship of the '
                                                'Function'},
                                    {   'genre': 'Action',
                                        'host': 'amazon',
                                        'rating': 2.2,
                                        'title': 'The JavaScript and the '
                                                'React'},
                                    {   'genre': 'Intrigue',
                                        'host': 'hulu',
                                        'rating': 2.0,
                                        'title': 'Recursion'},
                                    {   'genre': 'Intrigue',
                                        'host': 'disney+',
                                        'rating': 3.0,
                                        'title': 'Zero Dark Python'}]}],
    'subscriptions': ['netflix', 'hulu'],
    'watched': [   {   'genre': 'Fantasy',
                    'host': 'netflix',
                    'rating': 4.8,
                    'title': 'The Lord of the Functions: The Fellowship of '
                                'the Function'},
                {   'genre': 'Fantasy',
                    'host': 'netflix',
                    'rating': 4.0,
                    'title': 'The Lord of the Functions: The Two '
                                'Parameters'},
                {   'genre': 'Fantasy',
                    'host': 'amazon',
                    'rating': 4.0,
                    'title': 'The Lord of the Functions: The Return of the '
                                'Value'},
                {   'genre': 'Action',
                    'host': 'amazon',
                    'rating': 2.2,
                    'title': 'The JavaScript and the React'},
                {   'genre': 'Intrigue',
                    'host': 'hulu',
                    'rating': 2.0,
                    'title': 'Recursion'},
                {   'genre': 'Intrigue',
                    'host': 'disney+',
                    'rating': 4.5,
                    'title': 'Instructor Student TA Manager'}]}

get_new_rec_by_genre(user_data)