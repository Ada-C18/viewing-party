# ------------- WAVE 1 --------------------

from re import T


def create_movie(title, genre, rating):
    if title != None and genre != None and rating != None:
        movie = {
            'title': title,
            'genre': genre,
            'rating':rating
        }
        return  movie
    return None


def add_to_watched(user_data,movie):
    
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    
    for i in user_data["watchlist"]:
        if i["title"] == title:
            user_data["watched"].append(i)
            user_data["watchlist"].remove(i)
    return user_data    

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum1=[]
    av_rait=0
    user_data = user_data["watched"]
    for i in user_data:
       
        sum1.append(i['rating'])
        av_rait = sum(sum1)/len(sum1)

    return av_rait
        
    
def get_most_watched_genre(user_data):

    user_data = user_data['watched']
    for i in user_data:
        for b in user_data:
            if i['genre']== b['genre']:
                return i['genre']
            else:
                return None    






# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_movie=[]
    movies = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            movies.append(movie)
    for i in user_data['watched']:
        if i not in movies:
            unique_movie.append(i)
                        

    return unique_movie            

def get_friends_unique_watched(user_data):
    unique_movie=[]
    friend_unique = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie not in unique_movie:
                unique_movie.append(movie)
    for i in unique_movie:
        if i not in user_data['watched']:
            friend_unique.append(i)
    return friend_unique

                        

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    unique_movie=[]
    friend_unique = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie not in unique_movie:
                unique_movie.append(movie)
    for i in unique_movie:
        if i not in user_data['watched'] and i['host'] in user_data['subscriptions']:
            friend_unique.append(i)
    return friend_unique
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    fr_genre = []
    un_genre = str
    for genre in user_data['watched']:
        fr_genre.append(genre['genre'])
        if len(user_data['watched'])==0:
            un_genre= None
        else:    
            un_genre = max(set(fr_genre), key = fr_genre.count)    

    rec_movie=[]
    friend_movies = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie not in friend_movies:
                friend_movies.append(movie)
    for i in friend_movies:
        if i not in user_data['watched'] and i['genre'] == un_genre:
            rec_movie.append(i) 
    return rec_movie        



def get_rec_from_favorites(user_data):
    friends_movies = []
    fav_rec = []
    for friend in user_data['friends']:
        for movie in friend['watched']:
            if movie not in friends_movies:
                friends_movies.append(movie)
    for favor_movie in  user_data['favorites']:
        if favor_movie not in friends_movies:
            fav_rec.append(favor_movie)
    return fav_rec                   
