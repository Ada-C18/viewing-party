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
# - take two parameters: `user_data`, `movie`
#   - the value of `user_data` will be a dictionary with a key `"watched"`, and a value which is a list of dictionaries representing the movies the user has watched
#     - An empty list represents that the user has no movies in their watched list
#   - the value of `movie` will be a dictionary in this format:
#     - ```python
#       {
#         "title": "Title A",
#         "genre": "Horror",
#         "rating": 3.5
#       }
#       ```
# - add the `movie` to the `"watched"` list inside of `user_data`
# - return the `user_data`
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
# Create a function named watch_movie. This function should...
# take two parameters: user_data, title
# the value of user_data will be a dictionary with a "watchlist" and a "watched"
# This represents that the user has a watchlist and a list of watched movies
# the value of title will be a string
# This represents the title of the movie the user has watched
# If the title is in a movie in the user's watchlist:
# remove that movie from the watchlist
# add that movie to watched
# return the user_data
# If the title is not a movie in the user's watchlist:
# return the user_data

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
            user_data["watchlist"].clear()
            user_data["watched"].append(title)
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

