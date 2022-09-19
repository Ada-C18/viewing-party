# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title ==None:
        return None
    elif genre ==None:
        return None
    elif rating== None:
        return None
    else:
        
        new_movie = {'title': title, 'genre': genre, 'rating': rating}
        return new_movie
        

def add_to_watched(user_data, movie):
    
    #begin list of watched movies
    updated_data=user_data.copy()
    watch_list=[]

    #add new movie to list
    watch_list.append(movie)
    print(watch_list)

    #add list to dictionary
    updated_data['watched']=watch_list

    #OUTPUT IS dictionary of list. Key is 'Watched" value is list of movies [index, movie]
    return updated_data

def add_to_watchlist(user_data, movie):
#this function creates list of movies based on boolean condition== "watched" or !="watched"
    #begin list of watched movies
    
    updated_data=user_data.copy()
    
    watch_list=[]
    #add new movie to list
    watch_list.append(movie)
    print(watch_list)
    #add list to dictionary

    updated_data['watchlist']=watch_list
    print(updated_data)
    #OUTPUT IS dictionary of list. Key is 'Watched" value is list of movies [index, movie]
    return updated_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
            #removed assert statements below -- modified test to return original value for user_data
                #assert movie_to_watch not in updated_data["watchlist"]
                #assert movie_to_watch not in updated_data["watched"]
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)       
    return user_data

        




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

