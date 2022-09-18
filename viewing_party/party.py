# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {"title": title, "genre": genre, "rating": rating}
    if title is None or genre is None or rating is None:
        new_movie = None
    return new_movie

def add_to_watched(user_data, movie):
    updated_data = user_data
    updated_data["watched"].append(movie)
    return updated_data 

def add_to_watchlist(user_data, movie):
    updated_data = user_data
    updated_data["watchlist"].append(movie)
    return updated_data 

def watch_movie(user_data, movie):
    for item in user_data["watchlist"]:
        if item["title"] == movie:
            watched_movie = item
            user_data["watched"].append(watched_movie)
            user_data["watchlist"].remove(watched_movie)
    updated_data = user_data
    return updated_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# works when I change to float, ask instructor why
def get_watched_avg_rating(user_data):
    number_of_movies = 0
    average_ratings = 0.0
    if len(user_data["watched"]) == 0:
        average_ratings = 0.0
        return average_ratings
    for movie in user_data["watched"]:
        number_of_movies += 1
        average_ratings += float(movie["rating"])
    average_ratings = average_ratings/number_of_movies
    return average_ratings
        
def get_most_watched_genre(user_data):
    # loop through the user_data["watched"]
    # for every genre add to a new dictionary as a key
    # if key already exists, increase value by 1
    # if key doesn't already exist add to dictionary
    # go through this new dictionary, and find highest value and return that genre
    genre_dict = {}
    highest_count = 0
    most_frequent_genre = ""
    if len(user_data["watched"]) == 0:
        return None
    for movie in user_data["watched"]:
        if movie["genre"] not in genre_dict:
            genre_dict[movie["genre"]] = 0
        elif movie["genre"] in genre_dict:
            genre_dict[movie["genre"]] += 1
    for genre, count in genre_dict.items():
        if count > highest_count:
            most_frequent_genre = genre
            highest_count = count
    return most_frequent_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

