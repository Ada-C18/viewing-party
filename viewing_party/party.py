# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if  title and genre and rating:
        return {'title': title, 'genre': genre, 'rating': rating}
    else:
        return None

def add_to_watched(user_data, movie):
    user_data['watched'].append(movie) 
    return user_data

def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data['watchlist']:
        if movie['title'] == title:
            user_data['watched'].append(movie)
            i = user_data['watchlist'].index(movie)
            user_data['watchlist'].pop(i)
    return user_data
        
#janes_data = {
#        "watchlist": [{
#            "title": MOVIE_TITLE_1,
#            "genre": GENRE_1,
#           "rating": RATING_1},
# {
#            "title": MOVIE_TITLE_2,
#            "genre": GENRE_2,
#           "rating": RATING_2}
# ],
#       "watched": [{
#            "title": MOVIE_TITLE_4,
#            "genre": GENRE_4,
#           "rating": RATING_4
#       }]
#    }

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum_for_avg = 0
    count = len(user_data['watched'])
    if not count:
        return 0.0
    for movie in user_data['watched']:
        sum_for_avg += movie['rating']
    return sum_for_avg/count

def get_most_watched_genre(user_data):
    if not user_data['watched']:
        return None
    genre_freq ={}
    for movie in user_data['watched']:
        genre = movie['genre']
        if genre in genre_freq:
            genre_freq[genre] += 1
        else:
            genre_freq[genre] = 0
    max_genre = max(genre_freq, key=genre_freq.get)
    return max_genre



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------