# ------------- WAVE 1 --------------------

# def create_movie(title, genre, rating):
#     if title and genre and rating is True:
#         return {'title':title,
#         'genre': genre,
#         'rating':rating
#         }
#     else:
#         return None 
#     pass

def create_movie(title, genre, rating):
    if title is not None and genre is not None and rating is not None\
            and title is not False and genre is not False and rating is not False:
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
    needed_movie = None
    for movie in user_data['watchlist']:
        if movie['title']==title:
            needed_movie=movie
            break

    if needed_movie is not None:
        user_data['watched'].append(needed_movie)
        user_data['watchlist'].remove(needed_movie)

    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0

    for movie in user_data['watched']:
        sum+=movie['rating']

    result = 0
    if len(user_data['watched'])>0:
        result=sum/len(user_data['watched'])
    return result


def get_most_watched_genre(user_data):
    genres = {}
    for movie in user_data['watched']:
        if movie['genre'] in genres:
            genres[movie['genre']]+=1
        else:
            genres[movie['genre']]=1

    result = None
    if len(genres)>0:
        result = max(genres, key=genres.get)

    return result



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

