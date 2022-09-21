# ------------- WAVE 1 --------------------
from lib2to3.pytree import generate_matches
# from turtle import title

def create_movie(title, genre, rating):
    new_movie = { }
    
    if title == None or genre == None or rating == None:
        return None

    else:
        new_movie['title'] = title
        new_movie['genre'] = genre
        new_movie['rating'] = rating
    
        return new_movie
    

def add_to_watched(user_data,movie):
    
    user_data['watched'].append(movie)
    
    return user_data
    
def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    
    return user_data

def watch_movie(user_data, title):

    """
    title = 'string'
    input : user_data = dictionary
            2 keys, 'watchlist', 'watched'
            values = [ list ]
    """
    
    for count in range(len(user_data['watchlist'])):
        if user_data["watchlist"][count]['title'] == title:
            
            user_data['watched'].append(user_data["watchlist"][count])
            
            del user_data['watchlist'][count]
        
    return user_data         


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum = 0
    count = 0
    for count in range(len(user_data['watched'])):
        if (user_data["watched"][count]['rating']) != 0:
            sum += (user_data["watched"][count]['rating'])
        
        else:
            user_data["watched"][count]['rating'] = 0.0
            sum += (user_data["watched"][count]['rating'])

    average = sum / (count+1)
    return average

def get_most_watched_genre(user_data):
    total_genre = {}

    if user_data["watched"] == []:
        max_genre = None
    else:
        for count in range(len(user_data['watched'])):
            if user_data["watched"][count]['genre'] not in total_genre:
                total_genre[user_data["watched"][count]['genre']] = 1
            else:
                total_genre[user_data["watched"][count]['genre']] +=1
        max_genre = max(total_genre, key=total_genre.get)
    return max_genre

#***************************************************************************************************
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    movies_user = []
    friends_user = []

    for count in range(len(user_data['watched'])):
        movies_user.append(user_data['watched'][count]['title'])

    for friend in user_data['friends']:
        for movie in friend['watched']:
            for title,value in movie.items():
                if title == 'title':
                    friends_user.append(value)
    
    #transforme the list of movies from user and friends to set, para avoid duplicate titles
    movies_user_set = set(movies_user)
    friends_user_set = set(friends_user)
    
    # obtain the difference of movies_user minus friends_movies
    movies_only_user = movies_user_set - friends_user_set
    
    #convert the list -> from set to list.
    movies_only_final_list = list(movies_only_user)
    
    movies_only_final_list_dict = []
    
    for title in movies_only_final_list:
        for count in range(len(user_data['watched'])):
            if user_data['watched'][count]['title'] == title:
                movies_only_final_list_dict.append(user_data['watched'][count])
    
    return movies_only_final_list_dict

#***************************************************************************************************
def get_friends_unique_watched(user_data):
    
    movie_user = []
    friends_users = []
    
    for count in range(len(user_data['watched'])):
        movie_user.append(user_data['watched'][count]['title'])
        
    for friend in user_data['friends']:
        for movie in friend['watched']:
            for title,value in movie.items():
                if title == 'title':
                    friends_users.append(value)
    
    #transforme the list of movies from user and friends to set, para avoid duplicate titles
    movies_user_set = set(movie_user)
    friends_user_set = set(friends_users)
    
    # obtain the difference of friends_movies minus movies_user
    movies_only_friends = friends_user_set - movies_user_set
    
    #convert the list -> from set to list.
    movies_only_final_list = list(movies_only_friends)
    print('list>', movies_only_final_list)
    movies_friends_final_list_dict = []
    
    for title in movies_only_final_list:
        for friend in user_data['friends']:
            for movie in friend['watched']:
                if (movie['title']) == title:
                    if movie not in movies_friends_final_list_dict:
                        movies_friends_final_list_dict.append(movie)
    
    return movies_friends_final_list_dict
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------