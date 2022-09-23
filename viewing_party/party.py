# ------------- WAVE 1 --------------------

#from turtle import title


from tests.test_constants import USER_DATA_5


def create_movie(title, genre, rating):
    dict_movies={"title":title,
    "genre":genre,
    "rating":rating}
    if title ==None or genre==None or rating==None:
        return None
    else:
        return dict_movies
def add_to_watched(user_data,movie):
    user_data={}
    user_data["watched"]=[movie]
    return user_data

def add_to_watchlist(user_data,movie):
    user_data={}
    user_data["watchlist"]=[movie]
    return user_data
def watch_movie(user_data,title):
    for movie in user_data["watchlist"]:
        if movie["title"]==title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

def get_watched_avg_rating(user_data):
    rating_average=[]
    sum=0.0
    if len(user_data["watched"])==0:
        return 0.0
    for rating in user_data["watched"]:
        sum+=rating["rating"]
        rating_average.append(rating["rating"])
    return sum/len(rating_average)
def get_most_watched_genre(user_data):
    genre_most=[]
    counter="0"
    for genre in user_data["watched"]:
        counter+=genre["genre"]
        genre_most.append(genre["genre"])
        return max(set(genre_most),key=genre_most.count)
    return None
def get_unique_watched(user_data):
    friends_movies=[]
    user_movies=[]
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in friends_movies:
                friends_movies.append(movie)
    for movie in user_data["watched"]:
        if movie not in friends_movies:
            user_movies.append(movie)
    return user_movies
def get_friends_unique_watched(user_data):
    friends_watch_unique=[]
    user_unique_watched=[]
    for movie in user_data["watched"]:
        if movie not in user_unique_watched:
            user_unique_watched.append(movie)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            #if movie not in friends_watch_unique or movie not in user_unique_watched:
            if movie not in user_unique_watched and movie not in friends_watch_unique:
                friends_watch_unique.append(movie)
    return friends_watch_unique
    #for movie in user_data["watched"]:
        #if movie not in friends_watch_unique:
            #friends_watch_unique.append(movie)
   #return friends_watch_unique
   #can i make this code smaller?? i think so...
   #and vs OR
    
def get_available_recs(user_data):
    friends_watched=get_friends_unique_watched(user_data)
    friends_sub=[]
    for movie in friends_watched:
        if movie["host"] in user_data.get("subscriptions"):
            friends_sub.append(movie)
    return friends_sub
        
def get_new_rec_by_genre(user_data):
    user_genre=get_most_watched_genre(user_data)
    friends_movies=get_friends_unique_watched(user_data)
    user_movie_rec=[]
    if not user_data["watched"]:
        return user_movie_rec
    for movie in friends_movies:
        if movie ["genre"]in user_genre:
            user_movie_rec.append(movie)
    return user_movie_rec
def get_rec_from_favorites(user_data):
    #kik=get_unique_watched
    user_movies=get_unique_watched(user_data)
    favorite_movie=[]
    friends_movie_list=[]
    for movie in user_data["favorites"]:
        if movie in user_data["favorites"]:
            favorite_movie.append(movie)
    for movie in user_movies:
        if movie in user_movies:
            friends_movie_list.append(movie)
    #for movie in user_data["favorites"]:
        #if movie in user_data["favorites"]:
            #favorite_movie.append(movie)
    return friends_movie_list
    


        



    




        







# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

