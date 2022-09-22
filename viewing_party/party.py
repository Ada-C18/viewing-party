# ------------- WAVE 1 --------------------

from re import U
from venv import create


def create_movie(title, genre, rating):
    movie = {
        "title" : title,
        "genre" : genre,
        "rating" : rating,
    }
    if all(movie.values()) == False:
        return None
    else:
        return movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie):
    for movie_dict in user_data["watchlist"]:
        if movie_dict["title"] == movie:
            user_data["watched"].append(user_data["watchlist"].pop())
    return user_data

      
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    x = 0.0
    
    if len(user_data["watched"]) == 0:
        return x
    
    for film in user_data["watched"]:
        x += film["rating"]
    return x / len(user_data["watched"]) 

def get_most_watched_genre(user_data):
    genre_count = {}
    x = -1 
    best_genre = "" 
    
    if len(user_data["watched"]) == 0:
        return None
    
    for film in user_data["watched"]: 
        current_genre = film["genre"]   
        if current_genre not in genre_count.keys():
            genre_count.update({current_genre : 1})
        else:
            genre_count[current_genre] += 1 
    for genre, count in genre_count.items(): 
        if count > x:
            x = count
            best_genre = genre
    return best_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def create_film_diff_sets(user_data, is_user):
    user_set = set()
    friend_set = set()

    for film in user_data["watched"]:
        user_set.add(film["title"])
    for friend in user_data["friends"]:
        for film in friend["watched"]:
            friend_set.add(film["title"])

    if is_user:
        user_set.difference_update(friend_set)
        return user_set
    else:
        friend_set.difference_update(user_set)
        return friend_set
    



def get_unique_watched(user_data):
    user_set = create_film_diff_sets(user_data, True)
    user_unique_films = []
   
    for title in user_set:
        for film in user_data[ "watched"]:
            if title == film["title"]:
                user_unique_films.append(film)
    return user_unique_films


def get_friends_unique_watched(user_data):
    create_film_diff_sets(user_data, False)
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
