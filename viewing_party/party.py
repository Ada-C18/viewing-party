# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    info = [title, genre, rating]
    for movie_info in info:
        if movie_info == None:
            return None
        
    new_movie = {"title": title , "genre": genre , "rating": rating}
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"] = [movie]
    return user_data 

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]
    return user_data 

def watch_movie(user_data, movie):
    for movies in user_data["watchlist"]:
        for label,info in movies.items():
            if label == "title":
                if movie == info:
                    watched_movie = user_data["watchlist"].pop(user_data["watchlist"].index(movies))
                    user_data["watched"].append(watched_movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_watched):
    #putting ratings in a list
    ratings = []
    if user_watched["watched"]:
        for movies in user_watched["watched"]:
            for label,info in movies.items():
                if label == "rating":
                    ratings.append(info)
    else:
        return 0
    #calculating average rating
    total = 0
    for rating in ratings:
        total += rating
    average_rating = total / len(ratings)

    return average_rating

def get_most_watched_genre(user_watched):
    genre_popularity = {}
    if user_watched["watched"]:
        for movies in user_watched["watched"]:
                for label,info in movies.items():
                    if label == "genre":
                        if info in genre_popularity:
                            genre_popularity[info] = genre_popularity[info] + 1
                        else:
                            genre_popularity[info] = 1
        most_popular = max(genre_popularity, key=genre_popularity.get)
        return most_popular




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

