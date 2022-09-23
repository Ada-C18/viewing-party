# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):    
    if title and genre and (type(rating) == int or type(rating) == float):
        new_movie ={}  
        new_movie['title'] = title
        new_movie['genre'] = genre
        new_movie['rating'] = rating
        return new_movie
    return None

def add_to_watched(user_data, movie):
    # add movie (which is a dictionary) to the "watched" list inside "user_data"
    # "watched" is a dictionary key but it's also the index
    # of the list "user_data"
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    # "watchlist" is a dictionary key but is also an index in "user_data"
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist_list = user_data["watchlist"]
    watched_list = user_data["watched"]
    
    for movie in watchlist_list:
        if movie["title"] == title:
            watchlist_list.remove(movie)
            watched_list.append(movie)
            return user_data
    else:
        return user_data
# -----------------------------------------

# ------------- WAVE 2 --------------------
def get_watched_avg_rating(user_data):
    watched_list = user_data["watched"]   
    if watched_list == []:
        return 0.0

    sum = 0
    for movie in watched_list:
        sum += movie["rating"]
    average_movie_rating = sum / len(watched_list)
    return average_movie_rating

def get_most_watched_genre(user_data):
    watched_list = user_data["watched"]
    if watched_list == []:
        return None
    
    most_watched_genre = {}
    #access the value at key "genre"
    #count the number of times that value appears, genre_count +=?
    for movie in watched_list:
        genre = movie["genre"]
        if genre not in most_watched_genre:
            most_watched_genre[genre] = 1
        else:
            most_watched_genre[genre] += 1
    # genre with the highest count
    max_genre = max(most_watched_genre, key=most_watched_genre.get)
    return max_genre

# -----------------------------------------

# ------------- WAVE 3 --------------------
def get_unique_watched(user_data):
    user_unique_movies = []
    
    for movie in user_data["watched"]:    
        friends_list = user_data["friends"]
        found_movie = False
        for friend in friends_list:
            watched_list = friend["watched"]
            for friends_movie in watched_list:                
                if friends_movie["title"] == movie["title"]:
                    found_movie = True
        
        if found_movie == False:
            user_unique_movies.append(movie)
    return user_unique_movies
        
def get_friends_unique_watched(user_data):
    friends_movies_list = []
    user_movies_list = []
    friends_list = user_data["friends"]
    user_watched = user_data["watched"]
    
    for movie in user_watched:
        user_movies_list.append(movie["title"])
    set_user_movies = set(user_movies_list)

    
    for friend in friends_list:
        for movie in friend["watched"]:
            friends_movies_list.append(movie["title"])
    set_friends_movies = set(friends_movies_list)


    unique_friends_dict = set_friends_movies.difference(set_user_movies)

    final_list =[]
    for friend in friends_list:
        for movie in friend["watched"]:
            if movie["title"] in unique_friends_dict:
                final_list.append(movie )
    return final_list
# -----------------------------------------

# ------------- WAVE 4 --------------------


# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

