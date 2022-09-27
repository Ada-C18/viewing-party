# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    new_movie = {}
    if title != None:
        new_movie["title"] = title
        if genre != None:
            new_movie["genre"] = genre
            if rating != None:
                new_movie["rating"] = rating
                return new_movie
            else:
                return None
        else:
            return None
    else:
        return None
            

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i in range(len(user_data["watchlist"])):
        if title == user_data["watchlist"][i]["title"]: 
            user_data["watched"].append(user_data["watchlist"][i])
            user_data["watchlist"].pop(i)
            
            return user_data
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if len(user_data["watched"]) >= 1:
        sum = 0
        for i in range(len(user_data["watched"])):
            sum += user_data["watched"][i]["rating"]
        return sum / len(user_data["watched"])   
    else:
        return 0.0

def get_most_watched_genre(user_data):
    if len(user_data["watched"]) >= 1:
        genre_list = []
        for i in range(len(user_data["watched"])):
            genre_list.append(user_data["watched"][i]["genre"])
        
        counter = 0
        most_frequent_genre = genre_list[0]
        for i in genre_list:
            curr_frequency = genre_list.count(i)
            if(curr_frequency> counter):
                counter = curr_frequency
                most_frequent_genre = i
 
        return most_frequent_genre
    else:
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