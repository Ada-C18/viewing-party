# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {"title": title,
        "genre": genre,
        "rating": rating
        }
        return movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    watched_list = []
    watched_list.append(movie)
    user_data["watched"] = watched_list
    return user_data

def add_to_watchlist(user_data, movie):
    watchlist = []
    watchlist.append(movie)
    user_data["watchlist"] = watchlist
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total = 0.0
    movies = 0
    for movie in user_data["watched"]:
        total += movie["rating"]
        movies += 1
    if movies == 0:
        avg = 0.0
    else:
        avg = total / movies
    return avg

def get_most_watched_genre(user_data):
    count = 0
    max_count = 0
    max_genre = ""
    for movie in user_data["watched"]:
        genre = movie["genre"]
        for movie in user_data["watched"]:
            if genre in movie["genre"]:
                count += 1
        if count > max_count:
            max_genre = genre
            max_count = count
        count = 0
    if max_count == 0:
        return None
    else:
        return max_genre    


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    unique = []
    shared = False
    for watched in user_data["watched"]:
        for friend in user_data["friends"]:
            if watched in friend["watched"]:
                shared = True
        if not shared:
            unique.append(watched)
        shared = False
    return unique

def get_friends_unique_watched(user_data):
    unique = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in unique:
                unique.append(movie)
    return unique


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recs = []
    unique = get_friends_unique_watched(user_data)
    service = ""
    for movie in unique:
        service = movie["host"] 
        if service in user_data["subscriptions"]:
            recs.append(movie)
    return recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recs = get_friends_unique_watched(user_data)
    genre_recs = []
    genre = get_most_watched_genre(user_data)
    for movie in recs:
        if movie["genre"] == genre:
            genre_recs.append(movie)
    return genre_recs

def get_rec_from_favorites(user_data):
    user_recs = get_unique_watched(user_data)
    faves = []
    for movie in user_data["favorites"]:
        if movie in user_recs:
            faves.append(movie)
    return faves
