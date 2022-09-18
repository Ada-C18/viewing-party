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

# pop watchlist in list-dict-List title
# store in variable ,append to watched list


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

# {'watched': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}, {'title': 'The Lord of the Functions: The Two Parameters', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'The Lord of the Functions: The Return of the Value', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'The JavaScript and the React', 'genre': 'Action', 'rating': 2.2}, {'title': 'Recursion', 'genre': 'Intrigue', 'rating': 2.0}, {'title': 'Instructor Student TA Manager', 'genre': 'Intrigue', 'rating': 4.5}]}


def get_watched_avg_rating(user_data):
    sum = 0
    ratings_list = []
    if user_data:
        for i in user_data["watched"]:
            ratings_list.append(i['rating'])
        list_len = len(ratings_list)
        for i in ratings_list:
            sum += i
        average = sum/list_len
        return average
# empty watched list has 0.0 average rating

    return 0.0


# def get_most_watched_genre(user_data): #param same as above
    # use genre keys in each movie to find which is most watched.
    # if value of user_data is empty, return None


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# Function compares user watched list with friends watched, Returns UNIQUE list ONLY USER watched.

# def get_unique_watched(user_data):

# Function that compares user list with friends, returns UNIQUE list ONLY FRIENDS watched

# def get_friends_unique_watched(user_data):


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# def get_available_recs(user_data):


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# def get_new_rec_by_genre(user_data):
