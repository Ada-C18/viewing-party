from collections import Counter

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    return {
        "title": title,
        "genre": genre,
        "rating": rating,
    }

def add_to_watched(user_data, movie):
    updated_data = user_data.copy()
    updated_data["watched"].append(movie)
    return updated_data

def add_to_watchlist(user_data, movie):
    updated_data = user_data.copy()
    updated_data["watchlist"].append(movie)
    return updated_data

def watch_movie(user_data, movie):
    updated_data = user_data.copy()
    watchlist = updated_data["watchlist"]
    watched = updated_data["watched"]
    watchlist_titles = {
        watch_item["title"]: watch_item 
        for watch_item in watchlist
    }
    if movie in watchlist_titles:
        movie_details = watchlist_titles[movie]
        watchlist.remove(movie_details)
        watched.append(movie_details)
    return updated_data
        

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    watched = user_data["watched"]
    total = 0
    for movie in watched:
        total += movie["rating"]
    return (total / len(watched)) if len(watched) else 0

def get_most_watched_genre(user_data):
    genres = Counter([movie["genre"] for movie in user_data["watched"]])
    return genres.most_common(1)[0][0] if genres else None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

