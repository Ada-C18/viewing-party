# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie
    else:
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    i = 0
    for movie in user_data["watchlist"]:
        if title == movie["title"]:
            popped_movie = user_data["watchlist"].pop(i)
            user_data["watched"].append(popped_movie)
        i += 1
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    ratings = []
    if not user_data["watched"]:
        return 0.0

    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
    return sum(ratings) / len(user_data["watched"])

def get_most_watched_genre(user_data):
    genre_counts = {}
    if not user_data["watched"]:
        return None
    # Counts each genre using a dict (formatted as genre: count)
    for movie in user_data["watched"]:
        current_genre = movie["genre"]
        if current_genre not in genre_counts:
            genre_counts[current_genre] = 1
        else:
            genre_counts[current_genre] += 1
    # Returns key (genre) with the highest value (count)
    return max(genre_counts, key=genre_counts.get)

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_friends_watched(user_data):
    # Helper function
    # Adds all friends' watched movies to a list
    watched_list = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in watched_list:
                watched_list.append(movie)
    return watched_list


def get_unique_watched(user_data):
    unique_watched = []
    all_friends_watched = get_friends_watched(user_data)
    # Compares user's watched list to friends' watched list
    for movie in user_data["watched"]:
        if movie not in all_friends_watched:
            unique_watched.append(movie)
    
    return unique_watched

def get_friends_unique_watched(user_data):
    unique_friends_watched = []
    all_friends_watched = get_friends_watched(user_data)
    # Compares friends' watched list to user's watched list
    for movie in all_friends_watched:
        if movie not in user_data["watched"]:
            unique_friends_watched.append(movie)
    
    return unique_friends_watched

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

