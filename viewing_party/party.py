# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    dict_movie={
        "title": title,
        "genre": genre,
        "rating": rating
    }
    for key in dict_movie:
        if not dict_movie[key]:
            return None
    return dict_movie
def add_to_watched(the_user_data, movie_watched):
    the_user_data["watched"].append(movie_watched)
    return the_user_data

def add_to_watchlist(the_user_d, movie_to_watch):
    the_user_d["watchlist"].append(movie_to_watch)
    return the_user_d
def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
            if movie["title"] == title:
                user_data["watched"].append(movie)
                i  = user_data["watchlist"].index(movie)
                user_data["watchlist"].pop(i)
                return user_data
    else:
        return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user):

    sum_rating = 0.0
    if not user["watched"]:
            return sum_rating
    for movie in user["watched"]:
        sum_rating += movie["rating"]
        
    return sum_rating / len(user["watched"])
            
def get_most_watched_genre(user):
    dict_most_genre = {}
    most_genre_val = 0

    most_genre = []
    if not user["watched"]:
        return None
    for movie in user["watched"]:
        
        if movie["genre"] not in dict_most_genre:
            dict_most_genre[movie["genre"]] = 1
        else:
            dict_most_genre[movie["genre"]] +=1
    for genre, val in dict_most_genre.items():
        if val > most_genre_val:
            most_genre_val = val
    for genre in dict_most_genre:
        if dict_most_genre[genre] == most_genre_val:
            most_genre.append(genre)
    return ''.join(most_genre)


    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

