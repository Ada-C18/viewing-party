# ------------- WAVE 1 --------------------

## WAVE 1.01: validating input

def valid_title(title):
    if isinstance(title, str) and len(title) > 0:
        return True
    else:
        return False 

def valid_genre(genre):
    if isinstance(genre, str) and len(genre) > 0:
        return True
    else:
        return False 

def valid_rating(rating):
    # since I'm calculating the average later, also check to make sure that 
    # 0 <= rating <= 5 (assumed)
    # for example, if someone enters a tomatometer rating (1-100), return 
    # None 
    if not isinstance(rating, float):
        return False
    elif rating < 0.0 or rating > 5.0:
        return False 
    else:
        return True



def create_movie(title, genre, rating):
    """create_movie(title, genre, rating) returns a a dict when given:
    title: string, not empty
    genre: string, not empty
    rating: float?"""

    # validate input
    if valid_title(title) and valid_genre(genre) and valid_rating(rating):

        # model our movies as dictionary objects with title, genre, 
        # and rating fields 
        new_movie = {'title': title, 'genre': genre, 'rating': rating}
        return new_movie 

    else:
        return None 

def add_to_watchlist(user_data, movie):
    # append `movie` to the `user_data['watchlist']` field

    # get a reference to watchlist safely 
    watchlist = user_data.get('watchlist', [])
    watchlist.append(movie)
    return user_data # includes updates to watchlist

def add_to_watched(user_data, movie):
    # append `movie` to the `user_data['watched']` field

    # get a reference to watched safely 
    watched = user_data.get('watched', [])
    watched.append(movie)
    return user_data # includes updates to watchlist

def watch_movie(user_data, movie_title):
    # move a movie from watchlist to watched

    # all of this is happening in-place and 
    # might be safer done functionally

    watchlist = user_data.get('watchlist', [])
    watched = user_data.get('watched', [])

    for movie in watchlist:
        if movie_title == movie['title']:
            watched.append(movie)
            watchlist.remove(movie)
            break 
    
    # return updated user_data  
    user_data["watchlist"] = watchlist
    user_data["watched"] = watched
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


def get_watched_avg_rating(user_data):
    # calculate the average rating from user_data['watched']
    watched = user_data.get('watched', [])
    if not watched:
        return 0.0
    
    # assume average means mean 
    sum_rating = 0.0
    count_rating = len(watched)
    for movie in watched:
        sum_rating += movie['rating']

    
    # pass back the average 
    return sum_rating/count_rating 

# design questions
# handling ties? 
# Star Wars: science fiction, fantasy, or science fantasy? 

def get_most_watched_genre(user_data):

    # chedk for empty watch list
    watched = user_data.get('watched', [])
    if not watched:
        return None 

    # keys ~ str, vals ~ int
    genre_freq_table = {}
    for movie in watched:
        # ignore movies where the genre isn't set
        genre = movie.get('genre', None)
        # safely get the old freq with a default value
        # of 0 if we've not seen this genre
        if genre:
            old_freq = genre_freq_table.get(genre, 0)
            genre_freq_table[genre] = old_freq + 1

    # loop over genre_freq_table 
    # and collect the key with the highest value
    top_genre = None
    top_freq = 0
    for genre, freq in genre_freq_table.items():
        if freq > top_freq:
            # make sure to update both top_freq and 
            # top_genre 
            top_freq = freq 
            top_genre = genre
    
    return top_genre 




    









# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

