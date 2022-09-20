# ------------- WAVE 1 --------------------
import json

def create_movie(title, genre, rating):

   
    movie = {
        "title":title,
        "genre":genre,
        "rating":rating
    }
    #returns none if title or movie or rating is falsy
    if title == None or genre == None or rating == None:
        return None 
    #returns none if title or movie or rating is falsy
    else: 
        return movie






def add_to_watched(user_data, movie):
    #user data is dictionary w/ key "watched", value = [{}]
    
    
    user_data = {
        "watched": [movie]
    }

    ## create_movie(title, genre, rating) #call create_movie function 

#    last step to return user_data
    return user_data

def add_to_watchlist(user_data, movie):
    #user_data {"watchlist": list of dictionaries representing the movies the user wants to watch}
    #if watchlist = [] means no movies in watchlist
    user_data = {"watchlist":[movie]}

    return user_data




def watch_movie(user_data, title):
               
    
   
    for movie_title in user_data["watchlist"]:
        if title == movie_title["title"]:
            user_data["watchlist"].remove(movie_title)
            user_data["watched"].append(movie_title)
    return user_data
    


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
#   
#     #find average rating by accessing the "ratings" key from "watched" list from user_data dictionary
#user_data = {'watched': [{'genre': 'Fantasy', 'rating': 4.8, 'title': 'The Lord of the Functions: The Fellowship of the Function'}... 'rating': 2.0, 'title': 'Recursion'}, {'genre': 'Intrigue', 'rating': 4.5, 'title': 'Instructor Student TA Manager'}]}

    rating_list = [] #is this actually testing the function in pytest?
    
    if rating_list is None: #if empty list
        return 0.0
    
    for watch_list in user_data["watched"]: 
        for movie_rating in watch_list:
            # print(movie_rating)
            rating_list.append(movie_rating["rating"])
            
            
    try: #not sure if I need to add this
        average = sum(rating_list)/len(rating_list)
    except ZeroDivisionError:
        average = 0
    
    return format(average,".6f") #how do I get the format so that it is 3.58333



    





    
# def get_most_watched_genre(user_data):
#     #access the genre by user_data["watched"]
#     # to get the most frequently occuring in watched list, use a counter and for loop

#     # popular_genre = 0
    
#     genre_list = []

#     if len(user_data["watched"]) == 0:
#         return None

#     else:
#         for watch_list  in user_data["watched"]:
#             for movie_dict in watch_list:
#                 genre_list.append(movie_dict["genre"])

       
   
 

#      #not sure if we can use this but this should give the element with highest frequency , will use counter if not    
#     return max(set(genre_list), key =genre_list.count)


 




# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
# def get_unique_watched(user_data):
#     #initiated two emtpy list: user and friends
#     #loop through user_data

#     #turn user/ friends list to set and find difference result = set_a - set_b

#     user_list = []
#     friends_list = []





        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

