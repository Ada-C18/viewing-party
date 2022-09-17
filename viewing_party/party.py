# ------------- WAVE 1 --------------------

from sys import breakpointhook


def create_movie(title, genre, rating):
    
    movie = {}
    
    if not title or not genre or not rating:
        return None
    else:    
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
    
    return movie

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist = user_data['watchlist']
    watched = user_data['watched']
    i = 0

    for movie in watchlist:        
        if watchlist[i]['title'] == title:
            watchlist.remove(movie)
            watched.append(movie)
            
            user_data['watchlist'] = watchlist
            user_data['watched'] = watched
            return user_data
        else:
            i += 1
    else:
        return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    total_rating = 0.0
    avg_rating = 0.0
    watched = user_data['watched']

    if len(watched):
        for movie in watched:
            total_rating += movie['rating']
        
        avg_rating = total_rating / len(watched)
    
    return avg_rating

def get_most_watched_genre(user_data):
    watched = user_data['watched']
    genre_names = set()
    genre_dict = {}

    # because we don't know the genres that the user has watched, \
    # we have to determine what these are and initialize the dictionary \
    # before we can increment the genres.

    if len(watched):
        for movie in watched:
            genre_names.add(movie['genre'])
        
        for genre in genre_names:
            genre_dict[genre] = 0
        
        for movie in watched:
                for genre in genre_names:
                    if movie['genre'] == genre:
                        genre_dict[genre] += 1
        return max(genre_dict, key = genre_dict.get)

    else:
        return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

