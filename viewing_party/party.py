# ------------- WAVE 1 --------------------

from shutil import move
from tests.test_constants import FANTASY_1, FANTASY_2, GENRE_1, HORROR_1, RATING_1


def create_movie(title, genre, rating):
    new_movie = {"title": title, "genre": genre, "rating": rating}
    if title and genre and rating:
        return new_movie
    else:
        print(f'{new_movie} is None')

# test 5


def add_to_watched(user_data, movie):
    user_data = {"watched": []}
    user_data['watched'] = [movie]
    return user_data
# test 6


def add_to_watchlist(user_data, movie):
    user_data = {"watchlist": []}
    user_data['watchlist'] = [movie]
    return user_data

# test 7&8


def watch_movie(user_data, title):
    for i in range(len(user_data['watchlist'])):
        if user_data['watchlist'][i]['title'] == title:
            user_data['watched'].append(user_data['watchlist'][i])
            # user_data['watched'].remove(user_data['watchlist'][i])
            del (user_data['watchlist'][i])
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# test 1 & 2
def get_watched_avg_rating(user_data):
    score = 0
    num = len(user_data['watched'])
    if num == 0:
        return 0
    else:
        for i in range(num):
            score += user_data['watched'][i]['rating']
        return score/num

# test 3&4


def get_most_watched_genre(user_data):
    num = len(user_data['watched'])
    genre_dict = {}
    if num == 0:
        return None
    else:
        for i in range(num):
            if user_data['watched'][i]['genre'] not in genre_dict:
                genre_dict[user_data['watched'][i]['genre']] = 0
            elif user_data['watched'][i]['genre'] in genre_dict:
                genre_dict[user_data['watched'][i]['genre']] += 1
        max_value = max(genre_dict, key=genre_dict.get)
    return max_value

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    unique_list = []
    movie_list = []
    num = len(user_data['friends'])
    for i in range(num):
        movie_list += user_data['friends'][i]['watched']
    for movie_dict in user_data['watched']:
        if movie_dict not in movie_list:
            unique_list.append(movie_dict)  # append dict, not +=
    return unique_list


def get_friends_unique_watched(user_data):
    unique_list = []
    movie_list = []
    num = len(user_data['friends'])
    for i in range(num):
        movie_list += user_data['friends'][i]['watched']
    for movie_dict in movie_list:
        if movie_dict not in unique_list:
            if movie_dict not in user_data['watched']:
                unique_list.append(movie_dict)  # append dict, not +=
    return unique_list
# question about assertion in test wave 03

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):
    movie_recs = []
    fr_unique_list = get_friends_unique_watched(user_data)
    for movie_dict in fr_unique_list:
        if movie_dict['host'] in user_data['subscriptions']:
            movie_recs.append(movie_dict)
    return movie_recs
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


def get_new_rec_by_genre(user_data):
    movie_recs = []
    fr_unique_list = get_friends_unique_watched(user_data)
    max_genre = get_most_watched_genre(user_data)
    for movie_dict in fr_unique_list:
        if movie_dict['genre'] == max_genre:
            movie_recs.append(movie_dict)
    return movie_recs


def get_rec_from_favorites(user_data):
    fav_list = []
    movie_list = []
    num = len(user_data['friends'])
    for i in range(num):
        movie_list += user_data['friends'][i]['watched']
    for movie_dict in user_data['favorites']:
        if movie_dict not in movie_list:
            fav_list.append(movie_dict)  # append dict, not +=
    return fav_list
