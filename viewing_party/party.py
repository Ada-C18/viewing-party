# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {}

    if title == None or genre == None or rating == None:
        return None

    new_movie["title"] = title
    new_movie["genre"] = genre
    new_movie["rating"] = rating

    return new_movie

def add_to_watched(user_data, movie):
    # appends "watched" list value with movie data dict   
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    # appends "watchlist" list value with movie data dict
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    # moves movie data from "watchlist" list value to "watched" dict
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    # store the list of ratings in watched and their total added together
    watched_rating_list = []
    total_rating = 0

    user_data_watched = user_data["watched"]

    if user_data_watched == []:
        return 0.0

    # appends the watched_rating_list with the rating for each movie in the watched list
    for movie in user_data_watched:
        watched_rating_list.append(movie['rating'])

    # adds the ratings together and stores them in total_rating
    for rating in watched_rating_list:
        total_rating += rating

    avg_rating = total_rating / len(watched_rating_list)

    return avg_rating

def get_most_watched_genre(user_data):
    watched_genre_count = {}
    most_watched_genre_total = 0
    most_watched_genre = ""

    user_data_watched = user_data["watched"]

    if user_data_watched == []:
        return None

    for movie in user_data_watched:
        print("debug", movie['genre'])
        if movie["genre"] in watched_genre_count:
            watched_genre_count[movie["genre"]] += 1
        else:
            watched_genre_count[movie["genre"]] = 1

    for genre in watched_genre_count:
        if watched_genre_count[genre] > most_watched_genre_total:
            most_watched_genre_total = watched_genre_count[genre]
            most_watched_genre = genre

    return most_watched_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

