# ------------- WAVE 1 --------------------

import re


def create_movie(title, genre, rating):
    
    if title and genre and rating:
        return {
            "title": title,
            "genre": genre,
            "rating": rating,
        }
    else:
        return None    

def add_to_watched(user_data,movie):

    user_data['watched'].append(movie)
    return user_data


def add_to_watchlist(user_data, movie): 

    user_data["watchlist"].append(movie) 
    return user_data 

def watch_movie(user_data,title):

    for movie in user_data["watchlist"]:
        if movie['title'] == title:
            user_data["watched"].append(movie)

            user_data["watchlist"].remove(movie)    
            break
    return user_data    

           
               

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    if user_data["watched"] == []:

        return 0.0
    else:    
        sum = 0
        for movie in user_data["watched"]:
            sum += movie['rating']

        avg = sum / len(user_data["watched"]) 
        return avg 

def get_most_watched_genre(user_data):  
    

    if user_data["watched"] ==[]:
         return None

    genre_freq ={}
    for movie in user_data["watched"]:
        if movie['genre'] in genre_freq:
            genre_freq[movie["genre"]] += 1
        else:
            genre_freq[movie["genre"]] = 1
    

    for genre, value in genre_freq.items():
        if value == max(genre_freq.values()):
            return genre 


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_watched =[]

    for movie in user_data['watched']:
        add_to_unique = True
        for friend in user_data['friends']:
            if movie in friend["watched"]:
                add_to_unique = False
                break

        if add_to_unique:
            unique_watched.append(movie) 

    return unique_watched


def get_friends_unique_watched(user_data): 
    

    freinds_unique_watched = []

    for friend in user_data['friends']:
        
        for title in friend['watched']:
            # print(title)
            if title not in freinds_unique_watched and title not in user_data['watched']: 
                # print(title)
                freinds_unique_watched.append(title)
    return freinds_unique_watched          
    


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------

def get_available_recs(user_data):
    
   
    friends_unique_movies = get_friends_unique_watched(user_data)
    
    rec_movies= []
    for movie in friends_unique_movies:
        if movie["host"] in user_data['subscriptions']:
            rec_movies.append(movie)

    return rec_movies

# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    friends_unique_movies = get_friends_unique_watched(user_data)

    most_watched_genre = get_most_watched_genre(user_data)

    rec_movie_by_genre =[]

    for movie in friends_unique_movies:
        # print(movie)
        if most_watched_genre == movie['genre']:
            rec_movie_by_genre.append(movie)

    return rec_movie_by_genre 



def get_rec_from_favorites(user_data):
    unique_usr_watched = get_unique_watched(user_data)    

    rec_movies =[]

    for movie in user_data['favorites']:
        if movie in unique_usr_watched and movie not in rec_movies:
            rec_movies.append(movie)  
    return rec_movies          


