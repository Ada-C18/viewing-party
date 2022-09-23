# ------------- WAVE 1 --------------------



def create_movie(movie_title, genre, rating):
    if movie_title == None or genre == None or rating == None:
        return None
    else:
         movie = {}
         movie['title'] = movie_title
         movie['genre'] = genre
         movie['rating'] = rating
    return movie
          
   
def add_to_watched(user_data, movie):
    if "watched" in user_data:
        user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    if "watchlist" in user_data:
        user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for i, movie in enumerate(user_data["watchlist"]):
        if title ==movie['title']:
            user_data["watched"].append(movie)
            user_data["watchlist"].pop(i)
    return user_data
    
    

    
    



    


    
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
   if len(user_data['watched']) == 0:
        return 0
   else:
        total = sum(item['rating'] for item in user_data['watched'])
        average_rating = total/len((user_data)['watched'])
        return average_rating

    
    

def get_most_watched_genre(user_data):
    genre ={} # {'Fantasy' : 3, 'Action' : 1, "Intrigue" : 2}
    for movie in user_data["watched"]:
        current_movie_genre = movie["genre"]
        if current_movie_genre not in genre:
            genre[current_movie_genre] = 1
        else:
            genre[current_movie_genre] +=1

    if len(user_data['watched']) == 0:
        return None
    else:
        most_views = 0
        most_viewed_genre = ''
        for x in genre:
            if genre[x] > most_views:
                most_views = genre[x] # Fantasy: 3
                most_viewed_genre = x # Fantasy
        return most_viewed_genre
    
           

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
# 
def get_unique_watched(user_data):

    unique_watched = []

    for movie in user_data['watched']:
        friends_list = user_data["friends"]
        found_watched = False
        for friend in friends_list:
            watched_list = friend["watched"]
            for friends_movie in watched_list:
                if friends_movie['title']  == movie["title"]:
                    found_watched = True
        
        if found_watched == False:
            unique_watched.append(movie)
    return unique_watched
    

def get_friends_unique_watched(user_data):
    unique_watched = []

    for friend in user_data['friends']:
        watched_list = friend["watched"]
        for movie in watched_list:
            found_watched = False
            for user_movie in user_data['watched']:
                if movie['title'] == user_movie['title']:
                    found_watched = True
        
            for unique_movie in unique_watched:
                if movie['title'] == unique_movie['title']:
                    found_watched = True

            if not found_watched:
                unique_watched.append(movie)
    return unique_watched
    

    


            



   
   
    
                
        
            
            
    
    

       
        






# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
# 

def get_available_recs(user_data):
    unique_watched = get_friends_unique_watched(user_data)
    
    rec_movies = []
    
    for unique_movie in unique_watched:
        if unique_movie["host"] in user_data["subscriptions"]:
            rec_movies.append(unique_movie)
    
    return rec_movies

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
# Create a function named  `get_new_rec_by_genre`. This function should...

# - take one parameter: `user_data`
# - Consider the user's most frequently watched genre. Then, determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"genre"` of the movie is the same as the user's most frequent genre
# - Return the list of recommended movies

# 2. Create a function named  `get_rec_from_favorites`. This function should...

# - take one parameter: `user_data`
#   - `user_data` will have a field `"favorites"`. The value of `"favorites"` is a list of movie dictionaries
#     - This represents the user's favorite movies
# - Determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The movie is in the user's `"favorites"`
#   - None of the user's friends have watched it
# - Return the list of recommended movies
def get_new_rec_by_genre(user_data):
    unique_watched = get_friends_unique_watched(user_data)
    user_favorite_genre =get_most_watched_genre(user_data)
    list_of_recommended_movies =[]
    
    
    for movie in unique_watched:
        if user_favorite_genre == movie["genre"]:
            list_of_recommended_movies.append(movie)

    return list_of_recommended_movies

def get_rec_from_favorites(user_data):
    list_of_rec_favs =[]
    unique_watched = get_friends_unique_watched(user_data)
    for movie in user_data['favorites']:
        if movie not in unique_watched:
            list_of_rec_favs.append(movie)
    return list_of_rec_favs


        
           

    


    
    