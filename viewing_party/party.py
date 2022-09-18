# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------
TITLE_KEY = "title"
GENRE_KEY = "genre"
RATING_KEY = "rating"


def create_movie(title, genre, rating):

    new_movie = {
        TITLE_KEY: title,
        GENRE_KEY: genre,
        RATING_KEY: rating}

    if not new_movie[TITLE_KEY]:
        return None
    if not new_movie[GENRE_KEY]:
        return None
    if not new_movie[RATING_KEY]:
        return None

    return new_movie


def add_to_watched(user_data, movie):
    user_data = {"watched": [movie]}
    return user_data


def add_to_watchlist(user_data, movie):
    user_data = {"watchlist": [movie]}
    return user_data


def watch_movie(user_data, title):
    if user_data["watchlist"]:
        for i in user_data['watchlist']:
            if i['title'] == title:
                user_data["watched"].append(i)
                user_data['watchlist'].remove(i)

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):
    sum = 0
    ratings_list = []
    if user_data['watched']:
        for i in user_data["watched"]:
            ratings_list.append(i['rating'])
        list_len = len(ratings_list)
        for i in ratings_list:
            sum += i
        average = sum/list_len
        return average
    return 0.0


def get_most_watched_genre(user_data):
    genre_list = []
    genre_tally_dict = {}
    most_watched_str = None
    most_watched_int = 0
    if user_data:
        for i in user_data["watched"]:
            genre_list.append(i['genre'])
        for i in genre_list:
            if i not in genre_tally_dict:
                genre_tally_dict[i] = 1
                most_watched_int = 1
            else:
                genre_tally_dict[i] += 1
                most_watched_int += 1
            for i in genre_tally_dict:
                if genre_tally_dict[i] > most_watched_int:
                    most_watched_str = i
        return most_watched_str
        # use genre keys in each movie to find which is most watched.
    return None
    # -----------------------------------------
    # ------------- WAVE 3 --------------------
    # -----------------------------------------

    # Function compares user watched list with friends watched, Returns UNIQUE list ONLY USER watched.


def get_unique_watched(user_data):
    user_watched_list = user_data['watched']
    complete_list_of_friends = user_data['friends']
    user_unique_movie_list = []
    friends_title_list = []
    for friend in complete_list_of_friends:
        for friend_dict in friend['watched']:
            friends_title_list.append(friend_dict['title'])
    for user_dict in user_watched_list:
        if user_dict['title'] not in friends_title_list:
            user_unique_movie_list.append(user_dict)
    return user_unique_movie_list

 # user_title_list.append(user_dict['title'])
# friends_title_list.append(friend_dict['title'])
 # for user_dict in user_watched_list:
    # if friend_dict in user_watched_list or friend_dict['title'] == user_dict['title']:
    #     continue
    # if user_dict not in user_unique_movie_list:
    # unified_friends_set = friend_1_watched | friend_2_watched
    # users_unique_movies = user_watched_list | unified_friends_set
    # turn into dictionary user_unique_movies
    # return users_unique_movies


# -----------------------------------------------
    # Function that compares user list with friends, returns UNIQUE list ONLY FRIENDS watched
# def get_friends_unique_watched(user_data):
#     user_watched_set = user_data['watched']
#     friend_1_watched = user_data['friends']
#     friend_2_watched = user_data['friends'][1]
#     # return friends_unique_movies
#     pass

    # -----------------------------------------
    # ------------- WAVE 4 --------------------
    # -----------------------------------------

    # def get_available_recs(user_data):

    # -----------------------------------------
    # ------------- WAVE 5 --------------------
    # -----------------------------------------

    # def get_new_rec_by_genre(user_data):
