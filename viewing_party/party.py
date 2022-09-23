# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {'title': title, 'genre' : genre, 'rating': rating}
    if title and genre and rating:
        return movie_dict
    else:
        return None
    
def add_to_watched(user_data,movie):
    user_data['watched'].append(movie)
    return user_data


def add_to_watchlist(user_data,movie):
    user_data['watchlist'].append(movie)
    return user_data


def watch_movie(user_data,title): 
    movie_exist = False
    i = 0

    for movie in user_data['watchlist']:
        if movie['title']==title:
            
            user_data['watched'].append(user_data['watchlist'].pop(i))
            return user_data
            movie_exist = True
    i+=1
           
            
    
  
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    rating = 0.0
    for movie in user_data['watched']:
        rating +=movie['rating']

    average_rating = rating/len(user_data['watched'])
    return average_rating

def get_most_watched_genre(user_data):
    counter = 0
    genre_list = []
    genre_dict = {}
    for movie in user_data['watched']:
        genre_list.append(movie.get('genre'))
    i = 0
    genre_loc = 0
    for genre in genre_list:
        genre_count = genre_list.count(genre)
        if genre_count > counter:
            counter = genre_count 
            genre_loc = i
        genre_dict.update({'genre': genre_count })
    a = sorted(genre_dict.items(), key=lambda x: x[1])
    for genre in a:
        genre_frequent =genre

    return a[-1][0]
    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
