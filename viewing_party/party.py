# ------------- WAVE 1 --------------------

# from imp import new_module
# from turtle import title
# from os import remove

def create_movie(title, genre, rating):
    new_movie = {"title": title,
            "genre": genre,
            "rating": rating}
    
    if new_movie["genre"] == None:
        return None
    if new_movie["rating"] == None:
        return None
    if new_movie["title"] == None:
        return None
    return new_movie

def add_to_watched(user_data, movie):
    user_data = {}
    user_data["watched"] = [movie]
    return user_data

def add_to_watchlist(user_data, movie):
    user_data = {}
    user_data["watchlist"] = [movie]
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            i = user_data["watchlist"].index(movie)
            user_data["watchlist"].pop(i)
            return user_data
    else:
        return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    rating = []
    sum = 0.0

    for i in user_data["watched"]: #4.0, 4.8
        if i["rating"] == None: # i = 4.8
            return sum
        elif i["rating"] != None: 
            sum += i["rating"] #4.0 + 4.8 = 8.8 
            rating.append(i["rating"]) #[4.0, 4.8] 
            
    return sum/len(rating) 


def get_most_watched_genre(user_data): 
    fav_genre = []
    counter = 0
    top_genre = fav_genre

    for i in user_data["watched"]:
        fav_genre.append(i["genre"])
    
    for genre in fav_genre:
        curr_freq = fav_genre.count(genre)
        if(curr_freq > counter):
            counter = curr_freq
            top_genre = genre
            return top_genre
        elif fav_genre == []:
            return None






# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------