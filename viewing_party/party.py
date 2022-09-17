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

def get_most_watched_genre(user_data):
    genre_list = []
    counter = 0
    popular_genre = None
    if len(user_data["watched"]) == 0:
        # print("None")
        return None
    else:
        for index in range(len(user_data["watched"])):
            genre_list.append(user_data["watched"][index]["genre"])
        # print(genre_list)
        
        for item in genre_list:
            frequency = genre_list.count(item)
            # print(freq_genre)
            if frequency > counter :
                counter = frequency
                popular_genre = item
        # print(popular_genre)
        return popular_genre
    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

#  user_data ={ "watched":[{movie_dict1},{movie_dict2}],
#             "friends":["watched":[{movie1},{movie2}]],
#             }

def get_unique_watched(user_data):
    friends_watched_list = get_friends_watched_list(user_data)
    user_watched_list = get_user_watched_list(user_data)
    user_unique_list =[]

    for movie_dict in range(len(user_watched_list)):
        if user_watched_list[movie_dict] not in friends_watched_list:
            user_unique_list.append(user_watched_list[movie_dict])
    return user_unique_list


def get_friends_unique_watched(user_data):
    friends_watched_list = get_friends_watched_list(user_data)
    user_watched_list = get_user_watched_list(user_data)
    friends_unique_list = []
    
    for friends_dict in range(len(friends_watched_list)):
        if friends_watched_list[friends_dict] not in user_watched_list:
            friends_unique_list.append(friends_watched_list[friends_dict])
    return friends_unique_list

#HELPER FUNCTION TO CREATE FRIENDS' WATCHED LIST
def get_friends_watched_list(user_data):
    friends_watched_list = []

    if len(user_data["friends"]) == 0:
        friends_watched_list = []
    
    else:
        for index1 in range(len(user_data["friends"])): #first loop to give us the movie list (of dictionaries) of "friends"
            for index2 in range(len(user_data["friends"][index1]["watched"])): #second loop give us each element (list of dictionaries of "friends' watched list")
                for index3 in range(len(user_data["friends"][index1]["watched"][index2])): #third loop give us access to each element within the list of friends watched list to compare title
                    if user_data["friends"][index1]["watched"][index2] not in friends_watched_list:
                        friends_watched_list.append(user_data["friends"][index1]["watched"][index2])

        return friends_watched_list

#HELPER FUNCTION TO CREATE USER'S WATCH LIST
def get_user_watched_list(user_data):
    user_watched_list = []

    if len(user_data["friends"]) ==0:
        user_watched_list = []
    else:
        for movie in range(len(user_data["watched"])):
            user_watched_list.append(user_data["watched"][movie])
    
    return user_watched_list
        


        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

