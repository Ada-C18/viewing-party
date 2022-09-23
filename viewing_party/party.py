# ------------- WAVE 1 --------------------
from statistics import mean, mode

def create_movie(title, genre, rating):

    if title and genre and rating:
    
        movie = {"title": title,
    "genre": genre,
    "rating": rating,
    }

        return movie
 
def add_to_watched(user_data, movie):

    movies_watched = movie
    user_data["watched"].append(movies_watched)

    return user_data

def add_to_watchlist(user_data, movie):

    movie_watchlist = movie
    user_data["watchlist"].append(movie_watchlist)

    return user_data


def watch_movie(user_data, title):
    watchlist = user_data["watchlist"]
    
    
    for watch in range(len(watchlist)):
        if watchlist[watch]["title"] == title: 
            user_data["watched"].append(watchlist[watch])
            del watchlist[watch]
    return user_data



#wave 2

def get_watched_avg_rating(user_data):
#use loop to iterate through rating data and add them together / divide to find average
    
    watch_list = user_data["watched"]
    sum = 0
  
    if len(watch_list) == 0: 
        return 0
        #movie["rating"] == 0

    for movie in watch_list:
        sum += movie["rating"]
    
    average_rating = sum/len(watch_list) 

    return average_rating


#wave three

def get_most_watched_genre(user_data):

    watched_genre = user_data["watched"]
    genre_list = []


    if len(watched_genre) == 0: 
        return None
    for movies in range(len(watched_genre)):
        genre_list.append(watched_genre[movies]["genre"])
    return mode(genre_list)

    
def get_friends_movies(user_data):
    
    friends_list = []
    friends_watched_list_of_dicts = user_data["friends"]

    for friends in range(len(friends_watched_list_of_dicts)):
        for friends_two in range(len(friends_watched_list_of_dicts[friends]["watched"])):
            friends_list.append(friends_watched_list_of_dicts[friends]["watched"][friends_two])

    return friends_list


def get_unique_watched(user_data):
    
    unique_movies = []
    user_watched_list = user_data["watched"]
    friends_watched_list = get_friends_movies(user_data)

    for index in range(len(user_watched_list)):
        if not user_watched_list[index] in friends_watched_list:
            unique_movies.append(user_watched_list[index])
    
    return unique_movies

    
def get_friends_unique_watched(user_data):
    user_not_watched = []

    friends_watched_list = get_friends_movies(user_data)
    user_watched = user_data["watched"]
    # new_list = [item for item in friends_watched_list if item not in user_watched]
    # return new_list
    for movie in friends_watched_list:
         if movie not in user_watched:
           user_not_watched.append(movie)
     
    remove_duplicates = []

    for x in user_not_watched:
        if x not in remove_duplicates:
            remove_duplicates.append(x)

    return remove_duplicates  

#wave 4 tests 

def get_available_recs(user_data):

    rec_list = []
    user_subscriptions = user_data["subscriptions"]
    friends_watched_list = get_friends_movies(user_data)
    movies_user_has_not_seen = get_friends_unique_watched(user_data)

    for movie in movies_user_has_not_seen:
        if movie["host"] in user_subscriptions:
            rec_list.append(movie)
    return rec_list
     

#wave 5 
def get_new_rec_by_genre(user_data):
    user_unseen_movies = get_friends_unique_watched(user_data) #friend has seen but user has not
    fav_genre = get_most_watched_genre(user_data) #variable to get favorite genre
    rec_by_genre = []

    for movies in user_unseen_movies:
        if movies["genre"] == fav_genre:
            rec_by_genre.append(movies)
    
    return rec_by_genre

def get_rec_from_favorites(user_data):
    favorite_movies_rec_list = []
    unseen_movies_friends = get_unique_watched(user_data)
    favorite_movies = user_data["favorites"]

    for movie in unseen_movies_friends:
        if movie in favorite_movies:
            favorite_movies_rec_list.append(movie)
    return favorite_movies_rec_list







