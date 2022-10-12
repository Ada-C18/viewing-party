# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------
TITLE_KEY = "title"
GENRE_KEY = "genre"
RATING_KEY = "rating"


def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None

    new_movie = {
        TITLE_KEY: title,
        GENRE_KEY: genre,
        RATING_KEY: rating}
    return new_movie


def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data


def watch_movie(user_data, title):
    if user_data["watchlist"]:
        for movie in user_data['watchlist']:
            if movie['title'] == title:
                user_data["watched"].append(movie)
                user_data['watchlist'].remove(movie)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):
    sum = 0
    ratings_list = []
    if user_data['watched']:
        for movie in user_data["watched"]:
            ratings_list.append(movie['rating'])
        for movie in ratings_list:
            sum += movie
        average = sum/len(ratings_list)
        return average
    return 0.0


def get_most_watched_genre(user_data):
    genre_list = []
    genre_tally_dict = {}
    most_watched_str = None
    most_watched_int = 0
    if user_data:
        for movie in user_data["watched"]:
            genre_list.append(movie['genre'])
        for genre in genre_list:
            if genre not in genre_tally_dict:
                genre_tally_dict[genre] = 1
            else:
                genre_tally_dict[genre] += 1
            for genre in genre_tally_dict:
                if genre_tally_dict[genre] > most_watched_int:
                    most_watched_int = genre_tally_dict[genre]
                    most_watched_str = genre
        return most_watched_str
    return None

    # -----------------------------------------
    # ------------- WAVE 3 --------------------
    # -----------------------------------------


def get_unique_watched(user_data):
    user_watched_list = user_data['watched']
    friends = user_data['friends']
    user_unique_watched_list = []
    friends_title_list = []
    for friend in friends:
        for movie in friend['watched']:
            friends_title_list.append(movie['title'])
    for movie in user_watched_list:
        if movie['title'] not in friends_title_list:
            user_unique_watched_list.append(movie)
    return user_unique_watched_list


def get_friends_unique_watched(user_data):

    user_watched_list = user_data['watched']
    friends = user_data['friends']
    friends_unique_movie_list = []
    user_title_list = []
    for movie in user_watched_list:
        user_title_list.append(movie['title'])
    for friend in friends:
        for movie in friend['watched']:
            if movie['title'] not in user_title_list and movie not in friends_unique_movie_list:
                friends_unique_movie_list.append(movie)
    return friends_unique_movie_list

    # -----------------------------------------
    # ------------- WAVE 4 --------------------
    # -----------------------------------------


def get_available_recs(user_data):

    subscriptions_list = user_data['subscriptions']
    friends_unique_movie_list = get_friends_unique_watched(user_data)
    list_of_recommended_movies = []

    for movie in friends_unique_movie_list:
        if movie['host'] in subscriptions_list:
            list_of_recommended_movies.append(movie)

    return list_of_recommended_movies

    # -----------------------------------------
    # ------------- WAVE 5 --------------------
    # -----------------------------------------


def get_new_rec_by_genre(user_data):

    friends_unique_watched_list = get_friends_unique_watched(user_data)
    users_favorite_genres = get_most_watched_genre(user_data)
    list_of_recommended_genre_movies = []

    if users_favorite_genres and friends_unique_watched_list:
        for movie in friends_unique_watched_list:
            if movie['genre'] in users_favorite_genres and movie in friends_unique_watched_list:
                list_of_recommended_genre_movies.append(movie)
            return list_of_recommended_genre_movies

    return list_of_recommended_genre_movies


def get_rec_from_favorites(user_data):

    list_of_recommended_movies = []
    unique_users_movie_list = get_unique_watched(user_data)
    user_watched_list = user_data['watched']
    users_favorites = user_data['favorites']

    if user_watched_list and users_favorites:
        for movie in unique_users_movie_list:
            if movie in users_favorites:
                list_of_recommended_movies.append(movie)
        return list_of_recommended_movies
    return list_of_recommended_movies
