# ------------- WAVE 1 --------------------

def create_movie(title: str, genre: str, rating: float) -> dict: 
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating,
    }
    
    if title == None or genre == None or rating == None:
        return None
        
    return movie


def add_to_watched(user_data: dict, movie: dict) -> dict:    
    user_data["watched"].append(movie)

    return user_data 


def add_to_watchlist(user_data: dict, movie: dict) -> dict:  
    user_data["watchlist"].append(movie)

    return user_data


def watch_movie(user_data: dict, title: str) -> dict:
    user_watchlist = user_data["watchlist"]
    
    for movie in range(len(user_watchlist)):
        if user_watchlist[movie]["title"] == title:
            user_data["watched"].append(user_watchlist[movie])
            del user_watchlist[movie]

    return user_data 

   
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data: dict) -> float:
    user_ratings_list = []
    
    for movie in user_data["watched"]:
        user_ratings_list.append(movie["rating"])

    try:
        average_rating = sum(user_ratings_list) / len(user_data["watched"])
        return average_rating
    except(ZeroDivisionError):
        return 0.0


def get_most_watched_genre(user_data: dict) -> str:
    if len(user_data["watched"]) == 0:
        return None
    
    user_genres_list = []
    for movie in user_data["watched"]:
        user_genres_list.append(movie["genre"])

    user_most_watch_genre = max(set(user_genres_list), key=user_genres_list.count)    

    return user_most_watch_genre


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def user_wateched_movies(user_data: dict) -> set:
    set_user_watched_movies = set()
    for movie in user_data["watched"]: 
        set_user_watched_movies.add(movie["title"])
    
    return set_user_watched_movies


def friends_wateched_movies(user_data: dict) -> set:
    set_friends_watched_movies = set()
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            set_friends_watched_movies.add(movie["title"])
    
    return set_friends_watched_movies


def remove_duplicate_values(list_of_values: list) -> list:
    seen = set()
    unique_values = []
    for item in list_of_values:
        t = tuple(item.items())
        if t not in seen:
            seen.add(t)
            unique_values.append(item)
            
    return unique_values


def get_unique_watched(user_data: dict) -> int:
    user_watched_movies = user_wateched_movies(user_data)
    friends_watched_movies = friends_wateched_movies(user_data)
    user_unique_watched_movies = []
    
    set_user_unique_titles = user_watched_movies.difference(friends_watched_movies) # Set of movies(titles) only watched by user

    for movie in user_data["watched"]:
        if movie["title"] in set_user_unique_titles:
            user_unique_watched_movies.append(movie)
            
    return user_unique_watched_movies


def get_friends_unique_watched(user_data: dict) -> list: 
    user_watched_movies = user_wateched_movies(user_data)
    friends_watched_movies = friends_wateched_movies(user_data)
    unique_recomended_movies = []
     
    set_friends_unique_movie_titles = friends_watched_movies.difference(user_watched_movies) #  Set of movies only watched by friends but not user

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in set_friends_unique_movie_titles:
                if movie["title"] not in unique_recomended_movies:
                    unique_recomended_movies.append(movie)
    
    unique_recomended_movies = remove_duplicate_values(unique_recomended_movies)

    return unique_recomended_movies
          
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data: dict) -> dict:
    user_movies_not_watched = get_friends_unique_watched(user_data) 
    user_subscriptions = user_data["subscriptions"]
    recommended_movies = []

    for movie in user_movies_not_watched:
        if movie["host"] in user_subscriptions:
            recommended_movies.append(movie)
            
    return recommended_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def is_empy(user_data: dict) -> list:
    is_empty = list()  

    for friend in user_data["friends"]:
        if friend["watched"]:
            is_empty.append(False)
        is_empty.append(True)
    
    return is_empty


def user_most_frequent_watched_genre(user_data: dict) -> str:
    list_user_most_watched_genres = list()

    if len(user_data["watched"]) == 0:
        return list_user_most_watched_genres

    for movie in user_data["watched"]:
        list_user_most_watched_genres.append(movie["genre"])
    
    most_watched_genre = max(set(list_user_most_watched_genres), key=list_user_most_watched_genres.count)
    
    return most_watched_genre


def get_new_rec_by_genre(user_data: dict) -> list:
    friends = user_data["friends"] 
    user_most_watched_genre = user_most_frequent_watched_genre(user_data)
    recomended_movies = list()
    is_empty = is_empy(user_data)   

    if len(user_data["watched"]) == 0:
        return recomended_movies
        
    if all(is_empty):
        return recomended_movies

    friends_movie_watched = get_friends_unique_watched(user_data)
    for movie in friends_movie_watched:
        if movie["genre"] == user_most_watched_genre:
            recomended_movies.append(movie)

    return recomended_movies
    

def get_rec_from_favorites(user_data: dict) -> list:
    favorite_user_movies = user_data["favorites"] # A list of dictionaries of user fav movies
    friends_watched_movies = friends_wateched_movies(user_data)
    recomended_movies = []

    if len(favorite_user_movies) < 1:
        return recomended_movies

    for movie in favorite_user_movies:
        if movie["title"] not in friends_watched_movies:
            recomended_movies.append(movie)

    return recomended_movies
   
                 

