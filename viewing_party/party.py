# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # make a dictionary with these keys: "title":title, "genre": genre, "rating": rating
    movie_dict = {}

    if title and genre and rating:
        movie_dict['title'] = title
        movie_dict['genre'] = genre
        movie_dict['rating'] = rating

        return movie_dict
    
    return None
def add_to_watched(user_data, movie):
    # user data is a dictionary with a key watched that has the value of an empty list which will be later a list of dictionaries with the movies the user has watched
    # the value of movie is a dictionary like the one from the first function
    # add the value of movie to the list in watched
    # return user_data
    user_data['watched'].append(movie)
    return user_data
def add_to_watchlist(user_data, movie):
    # add movie to list in 'watchlist' key in user_data dictionary
    user_data['watchlist'].append(movie)
    return user_data
def watch_movie(user_data, title):

    for movie_dict in user_data['watchlist']:
        if title == movie_dict['title']:
            user_data['watched'].append(movie_dict)
            user_data['watchlist'].remove(movie_dict)

    return user_data


    # for movie in user_data.values():
    #     if title in user_data['watchlist']:
    #         user_data['watchlist'].remove(movie)
    #         user_data['watched'].append(movie)
    #         return user_data
    #     return user_data


    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    total_rating = 0.0
    avg_rating = 0.0
    for movie_dict in user_data['watched']:
        total_rating += movie_dict['rating']
        if len(user_data['watched']) == 0:
            avg_rating = 0.0
        else:
            avg_rating = total_rating/ len(user_data['watched'])
    return avg_rating
def get_most_watched_genre(user_data):
    genres = []
    genre_counter = {}
    for movie_dict in user_data['watched']:
        genres.append(movie_dict['genre'])
    for genre in genres:
        if genre not in genre_counter.keys():
            genre_counter[genre] = 1
        else:
            genre_counter[genre] += 1
    sorted_genre_count = sorted(genre_counter.values())
    for key, value in genre_counter.items():
        if value == sorted_genre_count[-1]:
            return key
    return None
        
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    # i need to compare my watched to a combined list of my friends watched movies
    unique_movies = []
    friends_movies = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            friends_movies.append(movie)
        # print(friends_movies)

    for movie_dict in user_data['watched']:
        if movie_dict not in friends_movies:
            unique_movies.append(movie_dict)
    return unique_movies
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

