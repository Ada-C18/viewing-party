# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    dict = {}
    if title and genre and rating:
        dict['title'] = title
        dict['genre'] = genre
        dict['rating'] = rating
        return dict
    else:
        return None

def add_to_watched(user_data, movie):
    #user_data = {'watched': []}
    #movie = {'title': "Title A", "genre": "Horror", "rating": 3.5}
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    #user_data = {'watchlist': []}
    #movie = {"title": "Title A", "genre": "Horror", "rating": 3.5}
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, title):
    #user_data = {"watchlist": [], "watched": []}
    #title = ""
    watchlist = user_data['watchlist']
    for watchlist_movie in watchlist:
        if title == watchlist_movie['title']:
            movie = watchlist_movie
            result = add_to_watched(user_data, movie)
            print('Result:', result)
            user_data['watchlist'].remove(watchlist_movie)
            
            return result
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    avg_rating = 0.0
    rating_sum = 0.0
    watched = user_data['watched']
    if len(watched) != 0:
        for movie in watched:
            rating_sum += movie['rating']
        avg_rating = rating_sum/len(watched)
    return avg_rating

def get_most_watched_genre(user_data):
    genre_counter = {}
    watched = user_data['watched']
    most = ''
    if len(watched) != 0:
        for movie in watched:
            if movie['genre'] in genre_counter.keys():
                genre_counter[movie['genre']] += 1
            else:
                genre_counter[movie['genre']] = 0
        most = max(genre_counter, key = genre_counter.get)
        return most

    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

