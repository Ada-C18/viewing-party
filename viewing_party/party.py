# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    movies_dict ={}
    if not title or not genre or not rating:
        return None
    else:
        movies_dict["title"] = title
        movies_dict["genre"] = genre
        movies_dict["rating"] = rating
        
        return movies_dict
                

def add_to_watched(user_data,movie):
    
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    

    
    for index in range(len(user_data["watchlist"])): #accessing the list inside watchlist 
        
        if title == user_data["watchlist"][index]["title"]:
            
            #adding the title already watched to watched list
            user_data["watched"].append(user_data["watchlist"][index])
            #removing the title already watched out of watchlist
            user_data["watchlist"].remove(user_data["watchlist"][index])
            print("watched ",user_data["watched"])
            print("watchlist ",user_data["watchlist"])
            return user_data
    
    return user_data 
    
    
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    rating_list =[]
    avg_rating = 0
    
    if len(user_data["watched"]) == 0:
        avg_rating == 0.0
        return avg_rating  
    
    else:
        # len(user_data["watched"])>0:
        for index in range(len(user_data["watched"])):
            rating_list.append(user_data["watched"][index]["rating"])
        print(rating_list)
        
        total_rating = (sum_rating(rating_list))
        avg_rating = total_rating / len(user_data["watched"])
        return avg_rating
    
#HELPER FUNCTION TO CALCULATE TOTAL RATING    
def sum_rating(rating_list):
    sum = 0
    for rating in rating_list:
        sum += rating
    return sum

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

