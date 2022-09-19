# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title and genre and rating:
        movie_dict = {"title": title, "genre": genre, "rating": rating}
        return movie_dict
    else:
        return None

def add_to_watched(user_data, movie):
    '''
    Takes two arguments, user_data and movie, where user_data 
    is a dictionary that stores all of the movies the user has watched 
    and movie is a dictionary which contains the information for a movie
    
    Adds the value of movie to the "watched" list inside of user_data

    Returns user_data
    '''
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    adds movie to the watchlist list inside of user_data,
    where movie is a dictionary and user_data is a dictionary with a list of dictionaries 
    '''
    user_data["watchlist"].append(movie)
    print(user_data)
    return user_data

def watch_movie(user_data, title):
    '''
    moves title from a user's watchlist to their watched list
    '''
    # watchlist_list = user_data["watchlist"]
    # print(watchlist_list)
    for index in range(len(user_data["watchlist"])):
        if user_data["watchlist"][index]["title"] == title:
            user_data["watched"].append(user_data["watchlist"].pop(index))
            
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    '''
    calculates the average rating of the movies in the user's watched list
    '''
    avg_rating = 0.0
    rating_sum = 0.0
    if len(user_data["watched"]) == 0:
        return avg_rating
    else:
        for movie in user_data["watched"]:
            rating_sum += movie["rating"]
    avg_rating = rating_sum / len(user_data["watched"])
    return avg_rating

def get_most_watched_genre(user_data):
    genre_dict = {}
    for movie in user_data["watched"]:
        current_genre = movie["genre"]
        if current_genre in genre_dict.keys():
            genre_dict[current_genre] += 1
        else:
            genre_dict[current_genre] = 1
    current_highest_genre = None
    current_highest_genre_score = 0
    for genre, frequency in genre_dict.items():
        if frequency > current_highest_genre_score:
            current_highest_genre_score = frequency
            current_highest_genre = genre 
    return current_highest_genre



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

