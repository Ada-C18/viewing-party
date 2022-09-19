# ------------- WAVE 1 --------------------

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
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie (user_data, title):
    if title in user_data["watchlist"]:
        #remove from list
        user_data["watchlist"].remove(title)
        add_to_watched(user_data, title)
        return user_data
    else:
        return user_data
        

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
'''
def get_watched_avg_rating(user_data):
    if len = 0
    avr = 0.0
    else:
        sum rating / len

def get_most_watched_genre(user_data):
    count each genre sum and get max

    if "watched" is empty, return None

'''

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
'''
#user watched but friends didnt
def get_unique_watched(user_data):
    intersecter??

#friends watched but user didnt
def get_friends_unique_watched(user_data):

'''
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
'''
#friends watched but user didnt, on host
def get_available_recs(user_data):


'''
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

'''
# matching genre with the max 
def get_new_rec_by_genre(user_data):

# movie is in the user's "favorites"; 
# None of the user's friends have watched it

def get_rec_from_favorites(user_data):
'''