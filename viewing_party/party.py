# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # wave part 1
    if title is None or genre is None or rating is None:
        return None
    
    else:
        dict = {}
        dict["title"] = title
        dict["genre"] = genre
        dict["rating"] = rating
        return dict

# wave 1 part 2

def add_to_watched(user_data, movie):
    list_of_dicts = []
    user_data["watched"].append(movie)
    return user_data

#wave 1 part 3
def add_to_watchlist(user_data, movie):
    list_of_dicts = []
    user_data["watchlist"].append(movie)
    return user_data

#wave  1 part 4

def watch_movie(user_data, title):

    #there is a dict user_data with key watchlist and watched 
    #watchlist is a key with value list of dicts
    # watched is a key with value list
    
    temp_list_of_dict = user_data["watchlist"] 
    for i in range(0, len(temp_list_of_dict)):
        temp_dict = temp_list_of_dict[i] 
        temp_string = temp_dict["title"] 
        temp_list_watched=user_data["watched"] 
        if temp_string is title:
            user_data["watchlist"].remove(temp_dict)
            user_data["watched"].append(temp_dict)
    return user_data



# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
#wave 2 part 1-ran testcase 1 and 2 
def get_watched_avg_rating(user_data):
    
    total_rating = 0
    temp_list_of_dict = user_data["watched"]
    if len(temp_list_of_dict) == 0:
        return 0.0
    for i in range (0, len(temp_list_of_dict)):
        total_rating+=temp_list_of_dict[i]["rating"]
    return total_rating/len(temp_list_of_dict)

    #wave 2 part 2 
def get_most_watched_genre(user_data):
    #return the genre that is most frequently occuring in "watched" list
    #if "watched" list is empty, return NOne 
    dict_genre = {}
    max = 0
    temp_list_of_moviedict = user_data["watched"] 
        

    if len(temp_list_of_moviedict) == 0:
        return None

         
    for i in range(0, len(temp_list_of_moviedict)):
        genre_value = temp_list_of_moviedict[i]["genre"] 
        if genre_value in dict_genre:
            val = dict_genre[genre_value] 
            val = val+1 
            if val > max:
                max = val
                ans = genre_value 
        else:
            dict_genre[genre_value] = 1 
            if dict_genre[genre_value] > max:
                ans = genre_value 
    return ans
    


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
# wave 3 func 1-ran tests 1 and 2 in wave 3
# make a function to compare if ele in list A is in list B


def get_unique_watched(user_data):
    #return a list of dicts representing movies user has watched, but none of their friends have watched
    result = [] 
    
    temp_list_of_moviedict_user = user_data["watched"] 

    temp_list_of_friends = user_data["friends"] 
    set_of_movies_friend = set()
    for i in range(0, len(temp_list_of_friends)):
        temp_list_friends = temp_list_of_friends[i]["watched"] 
        for i in range(0, len(temp_list_friends)):
            temp_dict_friend = temp_list_friends[i]
            if "title" in temp_dict_friend:
                temp_movie_friend = temp_dict_friend["title"]
                if temp_movie_friend not in set_of_movies_friend:
                    set_of_movies_friend.add(temp_movie_friend)

    for i in range(0, len(temp_list_of_moviedict_user)):
        movie_dict = temp_list_of_moviedict_user[i]
        if 'title' in movie_dict:
            movie_title = movie_dict['title']
            if movie_title not in set_of_movies_friend:
                result.append(temp_list_of_moviedict_user[i])
    
    return result

#friends have watched but user hasnt watched 
#wave 3 part 2
def get_friends_unique_watched(user_data):
    result = [] 
    set_not_watched = set()
    temp_list_of_moviedict_user = user_data["watched"] 

    temp_list_of_friends = user_data["friends"] 
    set_of_movies_user = set()
    for i in range(0, len(temp_list_of_moviedict_user)):
        temp_dict_user = temp_list_of_moviedict_user[i]
        if "title" in temp_dict_user:
            temp_movie_user = temp_dict_user["title"]
            if temp_movie_user not in set_of_movies_user:
                set_of_movies_user.add(temp_movie_user)


    for i in range(0, len(temp_list_of_friends)):
        movie_list_friend = temp_list_of_friends[i]["watched"] 
        for j in range(0, len(movie_list_friend)):
            if "title" in movie_list_friend[j]:
                movie_title = movie_list_friend[j]["title"]
                if movie_title not in set_of_movies_user and movie_title not in set_not_watched:
                    result.append(movie_list_friend[j])
                    set_not_watched.add(movie_title)
       
    
    return result

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

#wave 4 function 1


def get_available_recs(user_data):
    result = []
    user_dict = []
    friends_dict = []
    for movie in user_data["watched"]:
        user_dict.append(movie)
    for movie in user_data["friends"]:
        for item in movie["watched"]:
            friends_dict.append(item)

    for item in friends_dict:
        if item not in user_dict:
            if item["host"] in user_data["subscriptions"]:
                result.append(item)
    return result

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
# wave 5 part 1


def get_new_rec_by_genre(user_data):
    # find user's most frequently watched genre
    most_watched_genre = get_most_watched_genre(user_data) 
    result = []
    user_dict = []
    friends_dict = []
    for movie in user_data["watched"]:
        user_dict.append(movie)
    for movie in user_data["friends"]:
        for item in movie["watched"]:
            friends_dict.append(item)

    for item in friends_dict:
        if item not in user_dict:
            if item["genre"] is most_watched_genre:
                result.append(item)
    return result



#wave 5 part 2


def get_rec_from_favorites(user_data):
    result = []
    user_dict = []
    friends_dict = []
    for movie in user_data["watched"]:
        user_dict.append(movie)
    for movie in user_data["friends"]:
        for item in movie["watched"]:
            friends_dict.append(item)
    for item in user_data["favorites"]:
        if item not in friends_dict:
            result.append(item)
    return result

    
    


