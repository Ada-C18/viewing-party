# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):

   
    movie = {
        "title":title,
        "genre":genre,
        "rating":rating
    }
    #returns none if title or movie or rating is falsy
    if title == None or genre == None or rating == None:
        return None 
    
    else: 
        return movie






def add_to_watched(user_data, movie):
    #user data is dictionary w/ key "watched"
    
    user_data = {
        "watched": [movie]
    }

    
    return user_data

def add_to_watchlist(user_data, movie):
    #user_data {"watchlist": list of dictionaries representing the movies the user wants to watch}
 
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

    rating_list = []
   

    for movie in user_data["watched"]:
    
        rating_list.append(movie["rating"])
    if len(user_data["watched"]) == 0:
        return 0.0
        
    else:
        return sum(rating_list)/len(rating_list)
    
   

    
def get_most_watched_genre(user_data):
    #access the genre by user_data["watched"]
   

    genre_list = []

    if len(user_data["watched"]) == 0:
        return None

    else:
        for watch_list  in user_data["watched"]:
            genre_list.append(watch_list["genre"])

    return max(set(genre_list), key =genre_list.count)



# # -----------------------------------------
# # ------------- WAVE 3 --------------------
# # -----------------------------------------
def get_unique_watched(user_data):
    
# initiated two emtpy list: user and friends
#we have an outer dictionary, one with "watched" key and one with "friends " key
# {'watched': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}, {'title': 'The Lord of the Functions: The Two Parameters', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'The Lord of the Functions: The Return of the Value', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'The JavaScript and the React', 'genre': 'Action', 'rating': 2.2}, {'title': 'Recursion', 'genre': 'Intrigue', 'rating': 2.0}, {'title': 'Instructor Student TA Manager', 'genre': 'Intrigue', 'rating': 4.5}],
# 'friends': [{'watched': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}, {'title': 'The Lord of the Functions: The Return of the Value', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'The Programmer: An Unexpected Stack Trace', 'genre': 'Fantasy', 'rating': 4.0}, {'title': 'It Came from the Stack Trace', 'genre': 'Horror', 'rating': 3.5}]}, {'watched': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8}, {'title': 'The JavaScript and the React', 'genre': 'Action', 'rating': 2.2}, {'title': 'Recursion', 'genre': 'Intrigue', 'rating': 2.0}, {'title': 'Zero Dark Python', 'genre': 'Intrigue', 'rating': 3.0}]}]
#They want to see the what the user saw that none of their friends saw, and return list of movies [{title:,genre:},]
# loop through user_data and use if statement to see if user_data["watched"] is in user_data["friends"] 

#The Lord of the Functions: The Fellowship of the Function'The Lord of the Functions: The Two Parameters',The Lord of the Functions: The Return of the Value,'The JavaScript and the React''Recursion'Instructor Student TA Manager'
# 'The Lord of the Functions: The Fellowship of the Function''The Lord of the Functions: The Return of the Value''The Programmer: An Unexpected Stack Trace','It Came from the Stack Trace', 'The Lord of the Functions: The Fellowship of the Function',The JavaScript and the React','Recursion','Zero Dark Python'
   
    
    friends_watched_titles = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] not in friends_watched_titles:
                friends_watched_titles.append(movie["title"])
                
    
        
    unique_movies = []
    for user_watched_movie in user_data["watched"]:
        if user_watched_movie["title"] not in friends_watched_titles:
            unique_movies.append(user_watched_movie)
    return unique_movies
    
    
def get_friends_unique_watched(user_data):
#get only one of the friend's movie watched list, compare it to the users to see what the friend has saw the user hasn't


    user_list =[]
    friend_unique_movies = []
    friend_unique_no_duplicate = []

    for i in user_data["watched"]:
        user_list.append(i)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_list:
                friend_unique_movies.append(movie)
    #removing duplicates
    friend_unique_no_duplicate = [i for n, i in enumerate(friend_unique_movies)
            if i not in friend_unique_movies[n + 1:]]
    return friend_unique_no_duplicate

    


        
# # -----------------------------------------
# # ------------- WAVE 4 --------------------
# # -----------------------------------------
def get_available_recs(user_data):
# # # {'watched': [{'title': 'The Lord of the Functions: The Fellowship of the Function', 'genre': 'Fantasy', 'rating': 4.8, 'host': 'netflix'}
# # # 'subscriptions': ['netflix', 'hulu']}
# # #return a list with what the user has not wached that would be in the friends list, that the user has a subscription for


    recommended_movies = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["host"] in user_data["subscriptions"]:
                if movie not in user_data["watched"]:
                    recommended_movies.append(movie)
    return recommended_movies


   





# # # -----------------------------------------
# # # ------------- WAVE 5 --------------------
# # # -----------------------------------------
def get_new_rec_by_genre(user_data):
# we have to make a list of recommended movies from the friend's unique watched list IF it is in the most frequently watched genre

    recommended_movies = []
    most_watched_genre = get_most_watched_genre(user_data)
    
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["genre"] == most_watched_genre:
                if movie not in user_data["watched"]:
                    recommended_movies.append(movie)
    return recommended_movies


               



def get_rec_from_favorites(user_data):
# make a list of recommendations from user's favorite 

    recommendations =[]
    user_watched_movies = get_unique_watched(user_data)
    for movie in user_data["favorites"]:
        if movie in user_watched_movies:
            recommendations.append(movie)
    return recommendations
    






    
