# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    # check to see if parameters are true
    # conditional for each paramter 
    # add parameters to a dictionary if true
    # create a dictionary
    # append to dictionary if true, NONE if false
    # return dictionary

    movie = {}
    if title == None or genre == None or rating == None:
        return None
    else:
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie

def add_to_watched(user_data, movie):
    watched_list =[]
    watched_list.append(movie)
    user_data["watched"] = watched_list

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

