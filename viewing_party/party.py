# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    else:
        movie = {}
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
    return movie

def add_to_watched(data, movie):
    data["watched"].append(movie)
    return data

def add_to_watchlist(data, movie):
    data["watchlist"].append(movie)
    return data

def watch_movie(data, movie_title):
    movie = next((item for item in data["watchlist"] if item["title"] == movie_title), None)
    if movie:
        add_to_watched(data, movie)
        data["watchlist"].remove(movie)
    return data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(data):
    rating_total = 0
    number_of_ratings = len(data["watched"])
    for i in range(number_of_ratings):
        rating_total += data["watched"][i]["rating"]
    if number_of_ratings > 0:
        return rating_total / number_of_ratings
    else:
        return 0

def get_most_watched_genre(data):
    watch_frequency = {}
    most_watched_rate = 0
    watched_list = data["watched"]
    for i in range(len(watched_list)):
        genre = data["watched"][i]["genre"]
        if  genre not in watch_frequency:
            watch_frequency[genre] = 1
        else:
            watch_frequency[genre] += 1
    for value in watch_frequency.values():
        if value > most_watched_rate:
            most_watched_rate = value
    most_watched = list(watch_frequency.keys())[list(watch_frequency.values()).index(most_watched_rate)]
    return most_watched


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

