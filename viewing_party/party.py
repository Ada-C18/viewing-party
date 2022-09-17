# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    '''Add new movie if title, genre and rating are truthy'''
    new_movie = {}

    if title and genre and rating:
        new_movie["title"] = title
        new_movie["genre"] = genre
        new_movie["rating"] = rating
    else:
        return None

    return new_movie


def add_to_watched(user_data, movie):
    '''Add movie to watched movies list in user data dict'''
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    '''Add movies to watchlist in user data dict'''
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    '''Move watched movies from watchlist to watched in user_data'''
    for i in range(len(user_data["watchlist"])):
        if user_data["watchlist"][i]['title'] == title:
            user_data['watched'].append(user_data['watchlist'][i])
            user_data["watchlist"].remove(user_data["watchlist"][i])

    return user_data

# Note: For Waves 2, 3, 4, and 5, your implementation of each of the functions should not modify `user_data`.

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    '''Calculate avg rating of watched movies in user data'''
    print(user_data)
    average = 0.0
    rating_total = 0.0
    for i in range(len(user_data["watched"])):
        print(user_data["watched"][i]["rating"])
        rating_total += user_data["watched"][i]["rating"]
    
    if len(user_data['watched']) == 0:
        average == 0.0
    else:
        average = rating_total / len(user_data["watched"])
    
    return average


def get_most_watched_genre(user_data):
    '''Returning the genre watched the most times'''
    genres = []
    genre_count = {}
    for i in range(len(user_data["watched"])):
        genres.append(user_data['watched'][i]['genre'])
        genres.sort()
    print(f"genres: {genres}")

    for item in genres:
        if item not in genre_count:
            genre_count[item] = 0
        genre_count[item] += 1

    if len(genre_count) > 0:
        max_genre = max(genre_count, key=genre_count.get)       
        return max_genre
    else:
        return None

# max(stats, key=stats.get)
        

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------



        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

