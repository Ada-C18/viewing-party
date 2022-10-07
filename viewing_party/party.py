# ------------- WAVE 1 --------------------

# I feel like there's a better way to test if title, genre, & rating are truthy 
# but not sure how

def create_movie(title, genre, rating):
    # Original:

    # new_movie = {"title": title, "genre": genre, "rating": rating}
    # if title and genre and rating:
    #     return new_movie
    # else:
    #     return None

    # Refactored
    if not title or not genre or not rating:
        return None
    else:
        return  {"title": title, "genre": genre, "rating": rating}

def add_to_watched(user_data, movie):
    # Original:

    # has_watched = [movie] 
    # user_data = {"watched" : has_watched }
    # return user_data

    # Refactored:
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    # Original:

    # wants_to_watch = [] 
    # user_data = {"watchlist" : wants_to_watch }
    # wants_to_watch.append(movie)

    # Refactored

    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movies in user_data["watchlist"]:
        if movies["title"] == title:
            user_data["watchlist"].remove(movies)
            user_data["watched"].append(movies)
    return user_data
        
        
# -----------------------------------------
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------        

def get_watched_avg_rating(user_data):
    # Original:

    # count = 0
    # movie_rating = 0.0
    # if len(user_data["watched"]) == 0:
    #     return 0.0
    # else:
    #     for movies in user_data["watched"]:
    #         movie_rating += movies["rating"]
    #         count += 1  
    #     return movie_rating/count
  



# Refactored:
    if not user_data["watched"]:
        return 0.0
    count = 0
    movie_rating = 0.0
    for movies in user_data["watched"]:
        movie_rating += movies["rating"]
        count += 1  
    return movie_rating/count


def get_most_watched_genre(user_data):
    # Original: 

    # genre_list = []
    # if len(user_data["watched"]) == 0:
    #     return None
    # else:
    #     for movie in user_data["watched"]:
    #         genre_list.append(movie["genre"])
    #     return max(set(genre_list), key = genre_list.count)
    
    # Refactored:

    if not user_data["watched"]:
        return None
    genre_list = []
    for movie in user_data["watched"]:
        genre_list.append(movie["genre"])
        return max(set(genre_list), key = genre_list.count)

        



# -----------------------------------------
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    movies_list = [movies for movies in user_data["watched"]]
    # for movie in user_data["friends"]:
    #     for title in movie["watched"]:
    #         if title in movies_list:
    #             movies_list.remove(title)
    # return movies_list
    unique_movies_list = []
    for movie in movies_list:
        if movie not in user_data["friends"]:
            unique_movies_list.append(movie)
    return unique_movies_list
    # go deeper
    
def get_friends_unique_watched(user_data):
    # movies_list = [movies for movies in user_data["watched"]]
    friends_list = []
    for movie in user_data["friends"]:
        for title in movie["watched"]:
            if title not in user_data["watched"]:
                if title not in friends_list:
                    friends_list.append(title)
    
    return friends_list

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    friends_recs = []
    compatible = [] 
    # movies_list = [movies for movies in user_data["watched"]]
    for movie in user_data["friends"]:
        for title in movie["watched"]:
            if title not in user_data["watched"] and title not in friends_recs:
                friends_recs.append(title)

    for movie in friends_recs:
        if movie["host"] in user_data["subscriptions"]:
            compatible.append(movie)
    return compatible
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    genre_recs = []
    genre_list = []
    fave_genre = []
   
    if not user_data["watched"]:
        return None
    genre_list.append(movie["genre"])
    fave_genre.append(max(set(genre_list), key = genre_list.count))

    friends_recs = []
    movies_list = [movies for movies in user_data["watched"]]
    for movie in user_data["friends"]:
        for title in movie["watched"]:
            if title not in movies_list:
                if title not in friends_recs:
                    friends_recs.append(title)
    for movie in friends_recs:
        if movie["genre"] in fave_genre:
            genre_recs.append(movie)

    return genre_recs

def get_rec_from_favorites(user_data):
    movie_recs = []

    movies_list = [movies for movies in user_data["favorites"]]
    friends_list = []
    for movie in user_data["friends"]:
        for title in movie["watched"]:
            if title not in friends_list:
                friends_list.append(title)
    for movie in movies_list:
        if movie not in friends_list:
            # if movie not in movie_recs:
            movie_recs.append(movie)
    return movie_recs