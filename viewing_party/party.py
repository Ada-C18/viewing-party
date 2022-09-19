# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    return {"title": title, "genre": genre, "rating": rating}

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            add_to_watched(user_data, movie)
            user_data["watchlist"].remove(movie)
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating_sum = 0
    counter = 0
    try:
        for movie in user_data["watched"]:
            rating_sum += movie["rating"]
            counter += 1
        return rating_sum / counter
    except ZeroDivisionError:
        return 0

#note: there's got to be a better way to do this
def get_most_watched_genre(user_data):
    # get and store list of all genre values
    genre_total_list = []
    for movie in user_data["watched"]:
        genre_total_list.append(movie["genre"])
    # create set of genres (1 instance of each)
    print(genre_total_list)
    genres = set(genre_total_list)
    print(genres)
    # create dictionary of most frequent genres
    genre_frequencies = {}
    for genre in genres:
        for item in genre_total_list:
            if genre == item:
                try:
                    genre_frequencies[genre] += 1
                except KeyError: 
                    genre_frequencies[genre] = 1
    print(genre_frequencies)
    # identify genre with highest frequency count
    most_popular_genre = None
    max_frequency = 0
    for genre, frequency in genre_frequencies.items():
        if frequency > max_frequency:
            most_popular_genre = genre
            max_frequency = frequency
    print(most_popular_genre)
    return most_popular_genre









# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

