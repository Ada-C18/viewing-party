# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating,
        }
    else:
        return None    

def add_to_watched(user_data,movie):

    user_data['watched'].append(movie)
    return user_data


def add_to_watchlist(user_data, movie): 

    user_data["watchlist"].append(movie) 
    return user_data 

def watch_movie(user_data,title):

    for movie in user_data["watchlist"]:
        if movie['title'] == title:
            user_data["watched"].append(movie)

            user_data["watchlist"].remove(movie)    
            break
    return user_data    

           
               

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if user_data["watched"] == []:

        return 0.0
    else:    
        sum = 0
        for movie in user_data["watched"]:
            sum += movie['rating']

        avg = sum / len(user_data["watched"]) 
        return avg 

def get_most_watched_genre(user_data):  
    

    if user_data["watched"] ==[]:
         return None

    genre_freq ={}
    for movie in user_data["watched"]:
        if movie['genre'] in genre_freq:
            genre_freq[movie["genre"]] += 1
        else:
            genre_freq[movie["genre"]] = 1
    return max(genre_freq, key = lambda genre : genre_freq[genre])





# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_watched =[]

    for movie in user_data['watched']:
        add_to_unique = True
        for friend in user_data['friends']:
            if movie in friend["watched"]:
                add_to_unique = False
                break

        if add_to_unique:
            unique_watched.append(movie) 

    return unique_watched


def get_friends_unique_watched(user_data): 
    # user_unique_watched = set(get_unique_watched(user_data))
    freiend_movies_watched = set()
    for friend in user_data['friends']:
        freiend_movies_watched.update(friend["watched"])

    return list(freiend_movies_watched - set(user_data['watched']))




        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

