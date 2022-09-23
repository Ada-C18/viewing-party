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
    if not user_data['watched']:
        return 0.0
    for movie in user_data['watched']:
        rating +=movie['rating']

    average_rating = rating/len(user_data['watched'])
    return average_rating

def get_most_watched_genre(user_data):
    counter =0 
    genre_list = []
    genre_dict = {}
    if not user_data['watched']:
        return None
    for movie in user_data['watched']:
        genre_list.append(movie.get('genre'))
    i = 0
    genre_loc = 0
    for genre in genre_list:
        genre_count = genre_list.count(genre)
        if genre_count > counter:
            counter = genre_count 
            max_genre = genre

            
        
    return max_genre
    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data, movie):
    pass

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
