# ------------- WAVE 1 --------------------

# create movie as dictionary with title, genre, rating as key
def create_movie(title, genre, rating):   
    movie = {}
    if not title or not genre or not rating:
        return None
    else:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie

# add movie to watched
def add_to_watched(user_data, movie):  
    user_data["watched"].append(movie)
    return user_data

# add movie to watchlist
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

# if title matches element in watchlist, remove movie from watchlist and add to watched; otherwise return user_data
def watch_movie (user_data, title):    
    for movie in user_data["watchlist"]:
        if title in movie["title"]:
        #remove from list, can also use list.pop(list.index(movie))
            user_data["watchlist"].remove(movie)                
        #add_to_watched(user_data, title)
            user_data["watched"].append(movie)
            return user_data
    else:
        return user_data   


# ------------- WAVE 2 --------------------

# calculate avg. rating of all movie in wached list
def get_watched_avg_rating(user_data):
    
    sum_rating = 0.0
    watched_length = len(user_data["watched"])
    # access movie rating - user_data["watchlist"][0]["rating"] 
    if watched_length > 0:
        for movie in user_data["watched"]:
            sum_rating += movie["rating"]
        return sum_rating / watched_length
    else:
        return 0.0

#def get_most_watched_genre(user_data):
    #count each genre sum and get max

    #if "watched" is empty, return None



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