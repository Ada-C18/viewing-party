# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movie_dict = {'title': title, 'genre' : genre, 'rating': rating}
    if title and genre and rating:
        return movie_dict
    else:
        return None
    
def add_to_watched(user_data,movie):
    user_data['watched'].append(movie)
    return user_data


def add_to_watchlist(user_data,movie):
    user_data['watchlist'].append(movie)
    return user_data


def watch_movie(user_data,title): 
    i = 0

    for movie in user_data['watchlist']:
        
        if movie['title']==title:
            
            user_data['watched'].append(user_data['watchlist'].pop(i))
            return user_data
        i+=1  
           
            
    
  
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    rating = 0.0
    if not user_data['watched']:
        return 0.0
    for movie in user_data['watched']:
        rating +=movie['rating']

    average_rating = rating/len(user_data['watched'])
    return average_rating

def get_most_watched_genre(user_data):
    counter =0 
    genre_list = []
    genre_dict = {}
    if not user_data['watched']:
        return None
    for movie in user_data['watched']:
        genre_list.append(movie.get('genre'))
    i = 0
    genre_loc = 0
    for genre in genre_list:
        genre_count = genre_list.count(genre)
        if genre_count > counter:
            counter = genre_count 
            max_genre = genre

            
        
    return max_genre
    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
#
def get_unique_watched(user_data):
    # unique_list =[]
    # for movie in user_data["watched"]:
    #     if movie not in user_data["friends"]["watched"]:
    #         unique_list.append(movie)
    # return unique_list
    all_friends_movies = []
    i = 0
    for friend in user_data["friends"]:
        for friend_movie in user_data["friends"][i]["watched"]:
            all_friends_movies.append(friend_movie)
        i += 1

    friend_titles = []
    for friend_movie in all_friends_movies:
        friend_titles.append(friend_movie["title"])

    friends_not_watched = []
    for user_movie in user_data["watched"]:
        if user_movie["title"] not in friend_titles:
            friends_not_watched.append(user_movie)
    return friends_not_watched

def get_friends_unique_watched(user_data):
    unwatched_list = []
    counter = 0
    for movie in user_data ["friends"]: 
        for friend_movie in user_data["friends"][counter]["watched"]:
            unwatched_list.append(friend_movie)
        counter +=1

    seen_movies = set()
    clean_list = []
    for friends_movie in unwatched_list:
        t = tuple(friends_movie.items())
        if t not in seen_movies:
            seen_movies.add(t)
            clean_list(friends_movie)
    
    user_not_watched = []
    for friends_movies in clean_list:
        if friends_movies not in user_data["watched"]:
            user_not_watched.append(friends_movies)
    return user_not_watched


# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):

    all_friends_movies = []
    i = 0
    for friend in user_data["friends"]:
        for friends_movie in user_data["friends"][i]["watched"]:
            all_friends_movies.append(friends_movie)
        i += 1

    friends_and_user = []
    for friend_movies in all_friends_movies:
        if friend_movies not in user_data["watched"]:
            friends_and_user.append(friend_movies)

    recomended_movies = []
    j = 0
    for movie in friends_and_user:
        for subscription in user_data["subscriptions"]:
            if subscription in friends_and_user[j]["host"]:
                recomended_movies.append(movie)
        j += 1

    return recomended_movies


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

rec_genre_list =[]
    
def user_genre(user_data):
    return max(set(user_data["watched"]), key = user_data["watched"].count)

def get_new_rec_by_genre(user_data):
    for movie in (user_data):
        if movie in user_data["friends"]["watched"] and movie not in user_data['watched']:
            rec_genre_list.append(movie)
    return rec_genre_list

