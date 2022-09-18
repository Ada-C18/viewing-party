# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title is None or genre is None or rating is None:
        return None
    else:
        movie_dict = {'genre': genre, 'rating': rating, 'title': title}
        return movie_dict

def add_to_watched(user_data, movie):
    updated_data = user_data.copy()
    updated_data["watched"] += [movie]
    return updated_data

def add_to_watchlist(user_data, movie):
    updated_data = user_data.copy()
    updated_data["watchlist"] += [movie]
    return updated_data

def watch_movie(user_data, movie_title):
    updated_data = user_data.copy()
    movie_index = 0

    for movie in updated_data["watchlist"]:
        if movie["title"] == movie_title:
            updated_data = add_to_watched(updated_data, movie)
            updated_data["watchlist"].pop(movie_index)
        
        movie_index += 1
    return updated_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) == 0:
        return 0
    else:
        ratings_total = 0
        ratings_count = 0
        for movie in user_data["watched"]:
            ratings_total += movie["rating"]
            ratings_count +=1

        return ratings_total / ratings_count

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) == 0:
        return None
    else:
        genre_count = {}
        for movie in user_data["watched"]:
            if movie["genre"] in genre_count:
                genre_count[movie["genre"]] += 1
            else:
                genre_count[movie["genre"]] = 1
                
        return max(genre_count, key=genre_count.get)




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

