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

def add_to_watchlist(user_data, movie):
    list_of_dicts=[]
    user_data["watchlist"].append(movie)
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

