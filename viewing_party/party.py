# ------------- WAVE 1 --------------------

def create_movie(movie_title, genre, rating):
    my_movie = {
        "title" : movie_title,
        "genre" : genre,
        "rating" : rating,
    }

    return my_movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)

    return user_data    

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, movie):
    user_data["watched"].append(movie)
    user_data["watchlist"] = []

    return user_data

def watched_movie(user_data, movie_to_watch):

    if movie_to_watch in user_data["watchlist"]:
        user_data["watched"].append(movie_to_watch)
        user_data["watchlist"].remove(movie_to_watch)   

    return user_data


        


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]
    all_ratings = []
    for watch in watched_list:
        all_ratings.append(watch["rating"])
    rating_sum = sum(all_ratings)
    if len(user_data["watched"]) == 0:
        avg_rating = 0
    else:
        avg_rating = rating_sum/len(user_data["watched"])

    return avg_rating


def get_most_watched_genre(user_data):
    genre_list = user_data["watched"]
    all_genres = []
    for genres in genre_list:
        all_genres.append(genres["genre"])
    
    if len(all_genres) == 0:
        return None
    else:
        counter = 0
        num = all_genres[0]
        
        for i in all_genres:
            frequency = all_genres.count(i)
            if frequency > counter:
                counter = frequency
                num = i
        return num
    



# def get_unique_watched(amandas_data):


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

