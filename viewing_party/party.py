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
    to_watch_list = []
    to_watch_list.append(movie)
    user_data["watchlist"] = to_watch_list
    return user_data

def watch_movie(user_data, title):
    index = 0
    for i in user_data["watchlist"]:
        if title == i["title"]:
            movie = i
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
        else:
            index += 1
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total = 0.0
    movies = 0
    index = 0
    for i in user_data["watched"]:
        total += i["rating"]
        movies += 1
        index += 1
    if movies == 0:
        avg = 0.0
    else:
        avg = total / movies
    return avg

def get_most_watched_genre(user_data):
    count = 0
    max_count = 0
    max_genre = ""
    for i in user_data["watched"]:
        genre = i["genre"]
        for i in user_data["watched"]:
            if genre in i["genre"]:
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
    for i in user_data["watched"]:
        movie = i
        for j in user_data["friends"]:
            if i in j["watched"]:
                shared = True
        if not shared:
            unique.append(movie)
        shared = False
    return unique

def get_friends_unique_watched(user_data):
    unique = []
    for i in user_data["friends"]:
        for j in i["watched"]:
            movie = j
            if movie not in user_data["watched"] and movie not in unique:
                unique.append(movie)
    return unique



# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recs = []
    unique = []
    service = ""
    for i in user_data["friends"]:
        for j in i["watched"]:
            movie = j
            if movie not in user_data["watched"] and movie not in unique:
                unique.append(movie)
                service = movie["host"]
                if service in user_data["subscriptions"]:
                    recs.append(movie)
    return recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

