# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # wave part 1
    if title is None or genre is None or rating is None:
        return None
    
    else:
        dict={}
        dict["title"]=title
        dict["genre"]=genre
        dict["rating"]=rating
        return dict

# wave 1 part 2

def add_to_watched(user_data, movie):
    list_of_dicts=[]
    user_data["watched"].append(movie)
    return user_data

#wave 1 part 3
def add_to_watchlist(user_data, movie):
    list_of_dicts=[]
    user_data["watchlist"].append(movie)
    return user_data

#wave  1 part 4

def watch_movie(user_data, title):

    #there is a dict user_data with key watchlist and watched 
    #watchlist is a key with value list of dicts
    # watched is a key with value list
    
    temp_list_of_dict=user_data["watchlist"] #[{
            #     "title": MOVIE_TITLE_1,
            #     "genre": GENRE_1,
            #     "rating": RATING_1
            # }]
    for i in range(0, len(temp_list_of_dict)):
        temp_dict=temp_list_of_dict[i] #{
            #     "title": MOVIE_TITLE_1,
            #     "genre": GENRE_1,
            #     "rating": RATING_1
            # }
        temp_string=temp_dict["title"] # MOVIE_TITLE_1
        temp_list_watched=user_data["watched"] #[]
        if temp_string is title:
            user_data["watchlist"].remove(temp_dict)
            user_data["watched"].append(temp_dict)
    return user_data

#wave 2 part 1-ran testcase 1 and 2 
def get_watched_avg_rating(user_data):
    
    total_rating = 0
    temp_list_of_dict=user_data["watched"]
    if len(temp_list_of_dict)==0:
        return 0.0
    for i in range (0, len(temp_list_of_dict)):
        total_rating+=temp_list_of_dict[i]["rating"]
    return total_rating/len(temp_list_of_dict)

#wave 2 part 2 
def get_most_watched_genre(user_data):
    #return the genre that is most frequently occuring in "watched" list
    #if "watched" list is empty, return NOne 
    dict_genre={}
    max = 0
    temp_list_of_moviedict = user_data["watched"] 
        # [FANTASY_1, 
        # FANTASY_2, 
        # FANTASY_3, 
        # ACTION_1, 
        # INTRIGUE_1, 
        # INTRIGUE_2]
         
    for i in range(0, len(temp_list_of_moviedict)):
        genre_value = temp_list_of_moviedict[i]["genre"] #fantasy
        if genre_value in dict_genre:
            val = dict_genre[genre_value] #val=
            val = val+1 #val=2
            if val> max:
                max = val
                ans = genre_value #fantasy
        else:
            dict_genre[genre_value] = 1 #fantasy-1
            if dict_genre[genre_value]> max:
                ans = genre_value #ans= 
    return ans
    
    



    
            

















    



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

