import math

# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    
 # creates new movie dictionary
    new_movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

 # if no title, genre, or rating given, returns none for new movie dictionary
    if not title or not genre or not rating:
        new_movie = None

    return new_movie

def add_to_watched(user_data, movie):

 # adds watchlist movies to watched movies
    updated_user_data = user_data.copy()
    updated_user_data["watched"].append(movie)

    return updated_user_data

def add_to_watchlist(user_data, movie):

 # adds movie to users watchlist
    updated_user_data = user_data.copy()
    updated_user_data["watchlist"].append(movie)

    return updated_user_data

def watch_movie(user_data, title):
 # creates empty movie title list 
    title_list = []

 # adds movie dictionaries to movie title list if in user watchlist
    for dicts in user_data["watchlist"]:
        title_list.append(dicts["title"])

 # adds movie dictionaries to movie title list if in user watched
    for dicts in user_data["watched"]:
        title_list.append(dicts["title"])

 # updates users watched and watchlist        
    if title in title_list:
        updated_user_data = user_data.copy()
        updated_user_data["watched"].append(updated_user_data["watchlist"].copy())
        updated_user_data["watchlist"].pop()
        
        return updated_user_data
    
    else:
        return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
 # creates users watched list   
    watched_list = list(user_data.values())

 # returns users average rating  
    try:
        ratings_list = [sub['rating'] for sub in watched_list[0]]
        ratings_sum = math.fsum(ratings_list)
        avg_rating = ratings_sum/len(ratings_list)
        
        return avg_rating
  
  # if no rating returns average rating as 0  
    except ZeroDivisionError:
        avg_rating = 0
        
        return avg_rating
        
def get_most_watched_genre(user_data):
 # creates user watch list
    watched_list = list(user_data.values())
 # creates list of generes users has watched
    genre_list = [sub['genre'] for sub in watched_list[0]]

 # returns users most frequent genre watched
    if not genre_list:
        return None
    else:
        most_frequent_genre = max(set(genre_list), key = genre_list.count)
        
        return most_frequent_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    
    # gets users watched list
    user_watch_list = user_data["watched"]
    
    # gets friends list
    friends_list = user_data["friends"]
    
    # gets friends watched list
    friends_watch_list = []
    for dicts in friends_list:
        friends_watch_list.append(dicts["watched"])
        
    friends_watch_list = [val for sublist in friends_watch_list for val in sublist]

    # removes repeat movie dictionaries from friends watched list
    unique_friend_watch = list({val["title"]:val for val in friends_watch_list}.values())
    
    # removes movies that friends have watched from users watch list
    for val in unique_friend_watch:
        if val in user_watch_list:
            user_watch_list.remove(val)
            
    return user_watch_list

def get_friends_unique_watched(user_data):

# gets users watched list
    user_watch_list = user_data["watched"]
    
# gets users friends list
    friends_list = user_data["friends"]
    
# gets friends watch list
    friends_watch_list = []
    for dicts in friends_list:
        friends_watch_list.append(dicts["watched"])
        
    friends_watch_list = [val for sublist in friends_watch_list for val in sublist]
    
# removes repeat movie dictionaries from friends watched list
    unique_friend_watch = list({val["title"]: val for val in friends_watch_list}.values())
    
# removes movies from friends watched list if user has already watched
    for val in user_watch_list:
        if val in unique_friend_watch:
            unique_friend_watch.remove(val)
            
    return unique_friend_watch
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
  # variables
    user_watched_list = user_data["watched"]
    user_subs_list = user_data["subscriptions"]
    user_friends_list = user_data["friends"]

  # gets multiple friends watch lists
    friends_list = []
    for dicts in user_friends_list:
        friends_list.append(dicts["watched"])

  # compiles friends watch list into one list
    friends_rec_list = []
    for sublist in friends_list:
        for val in sublist:
            friends_rec_list.append(val)

  # removes movies that user has already watched from friends recommendations list
    for dicts in user_watched_list:
        if dicts in friends_rec_list:
            friends_rec_list.remove(dicts)

  # retrieves recommendations if user has subscription to site
    recommendations = []
    for subs in user_subs_list:
        for dicts in friends_rec_list:
            if dicts['host'] == subs:
                recommendations.append(dicts)
                break

    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

  #user data
    user_watched_list = user_data['watched']

    if not user_watched_list:
        genre_list = []
        most_watched_genre = None
    else:
        genre_list = [d['genre'] for d in user_watched_list]
        most_watched_genre = max(set(genre_list), key=genre_list.count)
 
  #friend data

    user_friends_list = user_data["friends"]
    friends_list = []
    for dicts in user_friends_list:
        friends_list.append(dicts["watched"])

    friends_list = []
    for dicts in user_friends_list:
        friends_list.append(dicts["watched"])

  # compiles friends watch list into one list
    friends_rec_list = []
    for sublist in friends_list:
        for val in sublist:
            friends_rec_list.append(val)

  # creates recommendation list by most watched genre
    rec_by_genre = []
    for dict in friends_rec_list:
        if dict['genre'] == most_watched_genre:
            rec_by_genre.append(dict)

  # removes repeated recommendations
    recommendations = []
    for dicts in rec_by_genre:
        if dicts not in recommendations:
            recommendations.append(dicts)
   
  # removes recommendations if user has already watched movie
    for dicts in user_watched_list:
        if dicts in recommendations:
            recommendations.remove(dicts)
        
    return recommendations

def get_rec_from_favorites(user_data):
    
    # user favorites list
    user_favorites = user_data['favorites']

    # user friends list
    user_friends_list = user_data['friends']

    # friends watchlist
    friends_list = []
    for dicts in user_friends_list:
        friends_list.append(dicts['watched'])

    friends_watch_list = []
    for sublist in friends_list:
        for val in sublist:
            friends_watch_list.append(val)

    # creates user recommendations for friends if friend has not seen movie
    user_recommendations = []
    for dicts in user_favorites:
        if dicts not in friends_watch_list:
            user_recommendations.append(dicts)
            
    return user_recommendations