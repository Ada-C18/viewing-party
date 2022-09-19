# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating,
    }
    return movie
def add_to_watched(user_data, movie):
    updated_data = user_data.copy()
    updated_data["watched"].append(movie)
    return updated_data
def add_to_watchlist(user_data, movie):
    updated_data = user_data.copy()
    updated_data["watchlist"].append(movie)
    return updated_data
def watch_movie(user_data, title):
    # want this function to iterate through the watched list
    #remove watchlist index from wachlist

    watchlist = user_data["watchlist"] 
    watched =user_data["watched"]
    # Value of title will be a string 
    # for i in range(len(watchlist)):

    for movie in watchlist:
        if movie["title"] == title:
            watched.append(movie)
            watchlist.remove(movie)
            # return user_data#
        #   add to watched and remove from watchlist
    # else:   
    
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    # represents that the user has a list of watched movies 
    rating_list = []
    for movie in user_data["watched"]:
        if movie["rating"]>0:
            rating_list.append(movie["rating"])
    rating_sum = sum(rating_list)
    avg_rating = rating_sum/len(rating_list)
    
    
    return avg_rating
   
   
    # watched = user_data["watched"]
    # avg_rating = ""
    # for i in range(len(watched)):
        # if watched[i]
    # return avg_rating 
    
    #  avr_

# calculate the average rating of all movies in the watched list
####### Divide the sum() by the len() of a list of numbers###  
# return the average rating
# Movie is a dictionary but it is a list
# Movie rating is a key
# We want the value to get the rating
# If 

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

