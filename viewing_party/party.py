# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    '''
    Create a dict containing info about one movie, with "title", "genre", and "rating", as keys, mapped to values passed in as arguments.
    '''
    if not title or not genre or not rating:
        return None

    movie = {}
    movie["title"] = title
    movie["genre"] = genre
    movie["rating"] = rating

    return movie

def add_to_watched(user_data, movie):
    '''
    Add a movie to a user's list of watched movies
    '''
    # user_data = {"watched" : []}
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    '''
    Add a movie to a user's watchlist
    '''
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    '''
    Move a movie from watchlist to watched
    '''
    
    #I want to find the correct dict entry in watchlist given the value of "title", how do I do that?
    #Iterate over watchlist until watchlist["title"] == movie_title
    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            watched_movie = movie
            user_data["watched"].append(watched_movie)
            user_data["watchlist"].remove(watched_movie)
    
    return user_data
    
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    ratings = []
    for movie in user_data["watched"]:
        ratings.append(movie["rating"])
    if not ratings:
        return 0
    
    return sum(ratings)/len(ratings)

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    genres = {}
    for movie in user_data["watched"]:
        if movie["genre"] not in genres:
            genres[movie["genre"]] = 1
        else:
            genres[movie["genre"]] += 1
    
    return max(genres, key = genres.get)
         
        
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

test_data = {"watchlist": [{"title": 1,
                            "genre": "scifi",
                            "rating": 3}],
             "watched": [{"title": 4,
                          "genre": "fantasy",
                          "rating": 6}]
    }

watch_movie(test_data, 1)
get_watched_avg_rating(test_data)
get_most_watched_genre(test_data)
