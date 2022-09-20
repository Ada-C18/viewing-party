# ------------- WAVE 1 --------------------
# this is my first commit 

from operator import ge


def create_movie(title, genre, rating):
    
    if title and genre and rating:
        movie = {}
        
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie

    else:
        return None

def add_to_watched(user_data, movie):
    prev = user_data["watched"] # creating a variable prev = the value of watched - we know key = watched
    curr = prev.append(movie)
    user_data["watched"] = curr # replacing the old empty value with the new value

    return user_data
    

# 
# if parameters = True return a dict with 
# {
# "title": "Interstellar"
# "genre": "Drama"
# "rating": 5}
# create empty dict

'''

Create a function named create_movie. This function and all subsequent functions should be in party.py. create_movie should...
take three parameters: title, genre, rating
If those three attributes are truthy, then return a dictionary. This dictionary should...
Have three key-value pairs, with specific keys
The three keys should be "title", "genre", and "rating"
The values of these key-value pairs should be appropriate values
If title is falsy, genre is falsy, or rating is falsy, this function should return None


'''

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
