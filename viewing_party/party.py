# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    #create dictionary to pair "title", "genre", and "rating" to inputted values
    #if any input element is None, return None
    
    new_movie = {}
    
    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
        return new_movie
    
    return None 

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    
    return user_data

def watch_movie(user_data, movie_to_watch):
    updated_watchlist = user_data["watchlist"]
    updated_watched = user_data["watched"]
    updated_data = {
        "watchlist": list(user_data["watchlist"]),
        "watched": list(user_data["watched"])
    }
    
    #Finds movie_to_watch in user_data's watchlist
    #Removes it and adds it to user_data's watched
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_to_watch:
            updated_data["watched"].append(movie)
            updated_data["watchlist"].remove(movie)
    
    return updated_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    #Extract ratings from all the listed movies
    #Get average by summing up and dividing by #
    ratings = []
    
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
    
    avg_rating = sum(ratings) / len(ratings)
    return avg_rating

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

