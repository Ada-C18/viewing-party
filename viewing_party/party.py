def create_movie(title, genre, rating):
    if not title or genre or rating:
        print("Missing title, genre or rating")
        return None
    movie_dict={
        "title":title,
        "genre":genre,
        "rating":rating
    }
    return movie_dict
def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    if title not in user_data["watchlist"].values():
        return user_data
    else:
        user_data["watched"] = user_data["watchlist"].pop(title)

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watchedavg_rating(user_data):
    if not user_data["watched"]["rating"]:
        return 0.0
    else:
        return sum(user_data["watched"]["rating"])/len(user_data["watched"]["rating"])

def get_most_watched_genre(user_data):
    pass


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

