from statistics import mode 



# ------------- WAVE 1 --------------------

from itertools import count


def create_movie(title, genre, rating):
    movie_dict={}
    if not title or not genre or not rating:
        return None
    else: 
        movie_dict["title"]=title
        movie_dict["genre"]=genre
        movie_dict["rating"]=rating
    return movie_dict


def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data



def watch_movie(user_data,title):
    for movie in user_data["watchlist"]:
        if movie["title"]==title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)


    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    count_of_ratings=0
    sum_of_ratings=0
    for list in user_data["watched"]:
        for rate,score in list.items():
            if rate=="rating":
                count_of_ratings+=1
                sum_of_ratings+=score
    if count_of_ratings==0:
        average=0
    else:
        average=sum_of_ratings/count_of_ratings
    return average



def get_most_watched_genre(user_data):
    genre_data=[]
   
    for list in user_data.values():
        for movie in list:
            if "genre" in movie:
                genre_data.append(movie["genre"])
    if len(genre_data)==0:
        most_often=None
    else: 
        most_often=mode(genre_data)
    return(most_often)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------


def get_unique_watched(user_data):
    user_watched=[]
    friends_watched=[]

    for watch in user_data["watched"]:
        user_watched.append(watch)
    for friend in user_data["friends"]:
        for movie in friend.values():
            for i in movie:
                friends_watched.append(i)
    
    newlist=[]

    for u in user_watched:
        if u not in friends_watched:
            newlist.append(u)
    
    return(newlist)


def get_friends_unique_watched(user_data):
    user_watched=[]
    friends_watched=[]

    for watch in user_data["watched"]:
        user_watched.append(watch)
    for friend in user_data["friends"]:
        for movie in friend.values():
            for i in movie:
                friends_watched.append(i)
    
    user_not_watched=[]
    final_list=[]

    for f in friends_watched:
        if f not in user_watched:
            user_not_watched.append(f)
    for item in user_not_watched:
        if item not in final_list:
            final_list.append(item)

    return(final_list)
   
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    user_watched=[]
    friends_watched=[]

    for watch in user_data["watched"]:
        user_watched.append(watch)
    for friend in user_data["friends"]:
        for movie in friend.values():
            for i in movie:
                friends_watched.append(i)
    
    user_not_watched=[]
    no_duplicates=[]
    final_list=[]

    for f in friends_watched:
        if f not in user_watched:
            user_not_watched.append(f)
    for item in user_not_watched:
        if item not in no_duplicates:
            no_duplicates.append(item)
    
    #compare the host with the subscriptions and only return movies that match the values in subscriptions

    for i in no_duplicates:
        for sub in user_data["subscriptions"]:
            if i["host"] ==sub:
                final_list.append(i)

    return(final_list)



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):

    if len(user_data["watched"])==0:
        return []

    # step 1. find the most frequent genre of user
    genre_data=[]
    for list in user_data["watched"]:
        genre_data.append(list["genre"])

    most_often=mode(genre_data)

    
#step 2: find movies the user has not watched but a friend has 
    user_watched=[]
    friends_watched=[]
    user_not_watched=[]
    no_duplicates=[]
    final_list=[]

    for watch in user_data["watched"]:
        user_watched.append(watch)
    for friend in user_data["friends"]:
        for movie in friend.values():
            for i in movie:
                friends_watched.append(i)
   
    
    #if a movie in friends_watched is not in user_watched, add to user_not_watched list
    
    for f in friends_watched:
        if f not in user_watched:
            user_not_watched.append(f)
    
        
#  remove duplicates 
    for movie in user_not_watched:
        if movie not in no_duplicates:
            no_duplicates.append(movie)

#step 3: only have movies with the genre that the user watches most 

    for movie in no_duplicates:
        if movie["genre"]==most_often:
            final_list.append(movie)


    return(final_list)


def get_rec_from_favorites(user_data):
    favorites=[]
    recommended=[]
    friends_list=[]

    for fave in user_data["favorites"]:
        favorites.append(fave)
    for watch in user_data["friends"]:
        for movie in watch["watched"]:
            friends_list.append(movie)

    for f in favorites:
        if f not in friends_list:
            recommended.append(f)
            
    return recommended
    

    

