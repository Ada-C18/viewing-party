# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):
   movie ={}
   if title and genre and rating :
       movie["title"]=title
       movie["genre"]=genre
       movie["rating"]=rating
       return movie
   else:
       return None
   
def  add_to_watched(user_data , movie):
    user_data["watched"].append(movie)
    return user_data
    
        
def add_to_watchlist(user_data , movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data , title):
    for movie in user_data["watchlist"]:
        
      if movie["title"]==title:
          user_data["watchlist"].remove(movie)
          user_data["watched"].append(movie)
          return user_data
    else :
        return user_data
    
  
    
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating( user_data):
    
    while len(user_data["watched"])>0:
        sum_rating=0
        for movie in user_data["watched"]:
            sum_rating+=movie["rating"]
            
        return sum_rating/len(user_data["watched"])
    return 0.0

    
        
def get_most_watched_genre(user_data):     
    while len(user_data["watched"])>0:  
        new_list=[]
        for movie in user_data["watched"]:
            new_list.append(movie["genre"])
        return max(set(new_list), key=new_list.count)
    return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_watched=[]
    unique_watched+=user_data["watched"]
    #friends_watch+=user_data["friends"]
    for list_1 in user_data["friends"] :
        for movie in list_1["watched"]:
            if movie in unique_watched :
                unique_watched.remove(movie)
    return unique_watched



def get_friends_unique_watched(user_data):
    friends_unique=[] 
    user_watched=user_data["watched"]
    friends_watch=user_data["friends"]
    for list_1 in friends_watch :
        for movie in list_1["watched"]:
            if movie not in user_watched and movie not in friends_unique:
                friends_unique.append(movie)
    return friends_unique

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):


   recommended_movie=[]

   subs=user_data.get("subscriptions",[])
   user_watched=user_data["watched"]
   friends_watch=user_data.get("friends",[])
   
   # assign subscriptions only if the key exists
    
   for list in friends_watch:
       for movie in list["watched"]:
           if movie  not in user_watched and movie["host"] in subs:
               recommended_movie.append(movie)
   return recommended_movie




# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

    # take one parameter: user_data
def  get_new_rec_by_genre(user_data):
    recommended_movie=[]
    watched_genre = get_most_watched_genre(user_data)
    recs = get_available_recs(user_data)
    for movie in recs:
        if watched_genre == movie['genre']:
            recommended_movie.append(movie)
    return recommended_movie


def get_rec_from_favorites(user_data):
    recommended_movie=[]
    user_uniques=get_unique_watched(user_data)
    
    for movie in user_data["favorites"]:
        if movie in user_uniques and movie not in recommended_movie:
            recommended_movie.append(movie)
    return recommended_movie
                
              
        
                
    
   
            

