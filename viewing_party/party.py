# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):

    if title == None or genre == None or rating == None:
        return None

    movie_dict = {
        "title": title,
        "genre": genre,
        "rating": rating
    }
    
    return movie_dict


def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):

    user_data["watchlist"].append(movie)

    return user_data

def watch_movie(user_data, title):

    watchlist = user_data["watchlist"]
    for i in range(len(watchlist)):
        if watchlist[i]["title"] == title:
            user_data["watched"].append(watchlist[i])
            del watchlist[i]
    
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):

    if len(user_data["watched"]) == 0:
        return 0

    rating_sum = 0
    #pull the ratings from the watched dict
    # append those ratings to the rating sum list
    watched = user_data["watched"]
    for movie in watched:
        rating = movie["rating"]
        rating_sum += rating
    
    return rating_sum / len(user_data["watched"])

def get_most_watched_genre(user_data):
    # go through the watched list of dict and find the genre
    # find the most frequent genre
    # genre is a str
    if len(user_data["watched"]) == 0:
        return None

    genre_dict = {}
    watched = user_data["watched"]
    max = 0
    for movie in watched:
        genre = movie['genre']
        if genre not in genre_dict:
            genre_dict[genre] = 1
        else:
            current_count = genre_dict.get(genre)
            genre_dict[genre] = current_count + 1

        if genre_dict.get(genre) > max:
            max = genre_dict.get(genre)

    for genre in genre_dict:
        if genre_dict.get(genre) == max:
            return genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    watched = user_data.get("watched")
    watched_movie_titles = set()
    friends_movie_titles = set()
    friends = user_data.get("friends")
    result = []

    for movie in watched:
        watched_movie_titles.add(movie["title"])

    for friend in friends:
        current_friend = friend.get("watched")
        for movie in current_friend:
            friends_movie_titles.add(movie["title"])


    for title in watched_movie_titles:
        if title not in friends_movie_titles:
            for movie in watched:
                if title == movie["title"]:
                    result.append(movie)

    return result

def get_friends_unique_watched(user_data):
    friends = user_data.get("friends")
    watched = user_data.get("watched")
    friends_title_set = set()
    watched_title_set = set()
    unique_title_set = set()
    result = []
    # this gathers all movie titles found in 
    # each friends watched movie list
    for friend in friends:
        watched_array = friend.get("watched")
        for movie in watched_array:
            title = movie.get("title")
            friends_title_set.add(title)
    # gathers all movie titles watched by user
    for movie in watched:
        title = movie.get("title")
        watched_title_set.add(title) 

    title_difference = friends_title_set - watched_title_set
    
    for friend in friends:
        watched_array = friend.get("watched")
        for movie in watched_array:
            title = movie.get("title")
            if title in title_difference and title not in unique_title_set:
                result.append(movie)
                unique_title_set.add(title)

    return result

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    
    recommended_movies = []
    friends_unique_watched = get_friends_unique_watched(user_data)
    subscriptions = set(user_data.get('subscriptions'))

    for movie in friends_unique_watched:
        if movie.get('host') in subscriptions:
            recommended_movies.append(movie)
    
    return recommended_movies
    
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):

    favorite_genre = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)
    recommended_movies = []

    for movie in friends_unique_watched:
        if movie.get("genre") == favorite_genre:
            recommended_movies.append(movie)

    return recommended_movies

def get_rec_from_favorites(user_data):

    unique_movies = get_unique_watched(user_data)
    favorites = user_data.get("favorites")
    recommended_movies= []
    favorite_title_set = set()

    for movie in favorites:
        title = movie.get('title')
        favorite_title_set.add(title)
    
    for movie in unique_movies:
        title = movie.get('title')
        if title in favorite_title_set:
            recommended_movies.append(movie)

    return recommended_movies