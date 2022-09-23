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

    if is_user == True:
        user_set.difference_update(friend_set)
        return user_set
    elif is_user == False:
        friend_set.difference_update(user_set)
        return friend_set



def get_unique_watched(user_data):
    user_set = create_film_diff_sets(user_data, True)
    unique_films = []

    for title in user_set:
        for film in user_data[ "watched"]:
            if title == film["title"]:
                unique_films.append(film)
    return unique_films


def get_friends_unique_watched(user_data):
    friend_set = create_film_diff_sets(user_data, False)
    unique_films = []
    duplicate = False

    for title in friend_set:
        for friend in user_data["friends"]:
            for film in friend[ "watched"]:
                 
                 if title == film["title"]:
                    unique_films.append(film)
                    duplicate = True 
                    break
            
            if duplicate == True:
                duplicate = False
                break        
                    
                
            
    return unique_films
   

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    avialable_recs = []
    friends_unique_watched = get_friends_unique_watched(user_data)
    
    for film in friends_unique_watched:
        if film["host"] in user_data["subscriptions"]:
            avialable_recs.append(film)

    return avialable_recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    most_watched_genre = get_most_watched_genre(user_data)
    unwatched = get_friends_unique_watched(user_data)
    recomendations = []

    for films in unwatched:
        if films["genre"] == most_watched_genre:
            recomendations.append(films)
    return recomendations
def get_rec_from_favorites(user_data):
    unique_watched = get_unique_watched(user_data)
    recomendations = []

    for film in unique_watched:
        for movie in user_data["favorites"]:
            if movie["title"] == film["title"]:
                recomendations.append(movie)

    return recomendations
        