# ------------- WAVE 1 --------------------

from genericpath import exists

def create_movie(title, genre, rating):
    if title is not None and genre is not None and rating is not None\
            and title is not False and genre is not False and rating is not False:
        return {'title': title, 'genre': genre, 'rating': rating}
    else:
        return None
    


def add_to_watched(user_data, movie):
    user_data['watched'].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data['watchlist'].append(movie)
    return user_data


def watch_movie(user_data, title):
    needed_movie = None
    for movie in user_data['watchlist']:
        if movie['title']==title:
            needed_movie=movie
            break

    if needed_movie is not None:
        user_data['watched'].append(needed_movie)
        user_data['watchlist'].remove(needed_movie)

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    sum = 0

    for movie in user_data['watched']:
        sum+=movie['rating']

    result = 0
    if len(user_data['watched'])>0:
        result=sum/len(user_data['watched'])
    return result


def get_most_watched_genre(user_data):
    genres = {}
    for movie in user_data['watched']:
        if movie['genre'] in genres:
            genres[movie['genre']]+=1
        else:
            genres[movie['genre']]=1

    result = None
    if len(genres)>0:
        result = max(genres, key=genres.get)

    return result



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    result = []
    for movie in user_data['watched']:
        watched = False 
        for friend in user_data['friends']:
            for friend_movie in friend['watched']:
                if movie['title'] == friend_movie["title"]:
                    watched = True 
                    break
            if not watched:
                result.append(movie)
    return result 

def get_friends_unique_watched(user_data):
    results = []
    exists = set()
    for friend in user_data['friends']:
        for friend_movie in friend['watched']:
            watched = False 
            for movie in user_data['watched']:
                if movie['title']== friend_movie['title']:
                    watched = True 
                    break
            if not watched and friend_movie['title'] not in exists:
                results.append(friend_movie)
                exists.add(friend_movie['title'])
    return results



        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    result = []
    exists = set ()
    for friend in user_data['friends']:
        for friend_movie in friend['watched']:
            watched = False 
            for movie in user_data['watched']:
                if movie['title']== friend_movie['title']:
                    watched = True
                    break 
            if not watched and friend_movie['title'] not in exists and friend_movie['host'] in user_data['subscriptions']:
                result.append(friend_movie)
                exists.add(friend_movie['title'])
    return result 


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    genres = {}
    result = []
    exists = set()

    for movie in user_data['watched']:
        if movie['genre'] in genres:
            genres[movie['genre']]+=1 
        else:
            genres[movie['genre']]=1

    frequent_genre = None 
    if len(genres)>0:
        frequent_genre = max(genres, key=genres.get)
    else:
        return result 

    for friend in user_data['friends']:
        for friend_movie in friend['watched']:
            watched = False 
            for movie in user_data['watched']:
                if movie['title']==friend_movie['title']:
                    watched = True 
                    break 
            if not watched and friend_movie['title'] not in exists and friend_movie['genre']== frequent_genre:
                result.append(friend_movie)
                exists.add(friend_movie['title'])
    return result 

def get_rec_from_favorites(user_data):
    result = []
    for movie in user_data['favorites']:
        watched = False 
        for friend in user_data['friends']:
            for friend_movie in friend['watched']:
                watched = True 
                break 
        if not watched:
            result.append(movie)

    return result 

    

