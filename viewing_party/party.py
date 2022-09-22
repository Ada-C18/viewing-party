# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {}

    if title and genre and rating:
        movie_dict['title'] = title
        movie_dict['genre'] = genre
        movie_dict['rating'] = rating

        return movie_dict
    
    return None
def add_to_watched(user_data, movie):

    user_data['watched'].append(movie)
    return user_data
def add_to_watchlist(user_data, movie):

    user_data['watchlist'].append(movie)
    return user_data
def watch_movie(user_data, title):

    for movie_dict in user_data['watchlist']:
        if title == movie_dict['title']:
            user_data['watched'].append(movie_dict)
            user_data['watchlist'].remove(movie_dict)

    return user_data


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
    for genre, frequency in genre_counter.items():
        if frequency == sorted_genre_count[-1]:
            return genre
    return None
        
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):

    unique_movies = []
    friends_movies = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            friends_movies.append(movie)

    for movie_dict in user_data['watched']:
        if movie_dict not in friends_movies:
            unique_movies.append(movie_dict)
    return unique_movies
def get_friends_unique_watched(user_data):
    friends_unique_movies = []
    
    users_movies = []
    for movie_dict in user_data['watched']:
        users_movies.append(movie_dict)
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie not in users_movies:
                if movie not in friends_unique_movies:
                    friends_unique_movies.append(movie)
    return friends_unique_movies
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friends_unique_movies = get_friends_unique_watched(user_data)
    recommended_movies = []
    for movie in friends_unique_movies:
        if movie["host"] in user_data['subscriptions']:
            recommended_movies.append(movie)
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    recommended_movies = []
    friends_unique_movies = get_friends_unique_watched(user_data)
    for movie in friends_unique_movies:
        if movie['genre'] == most_watched_genre:
            recommended_movies.append(movie)
    return recommended_movies
def get_rec_from_favorites(user_data):
    users_unique_movies = get_unique_watched(user_data)
    recommended_movies = []
    for movie in users_unique_movies:
        if movie in user_data['favorites']:
            recommended_movies.append(movie)
    return recommended_movies
