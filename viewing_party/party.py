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
    curr = prev.append(movie) # tried .append and got type error none doesn't have len # do we need to bring the index in at all?
    # user_data["watched"] = curr # replacing the old empty value with the new value # this was causing the issue - why?

    return user_data

def add_to_watchlist(user_data, movie):
    prev = user_data["watchlist"]
    curr = prev.append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            return user_data
    return user_data


        
    # need to remove key:values from watchlist{dict} and append to watched{dict}
    # need to figure out if we need to use a for loop maybe and if else statements and then how to "move" elements from one dict to another. Do we use 
    # if title in watchlist{dict} remove movie from watchlist and move to watched{dict} then return user_data - use .remove and.append
    # watchlist len will go from 1 to 0 and watched len will go from 0 to 1


# curr = prev.update({"watched":movie}) # this gives AttributeError: 'list' object has no attribute 'update' error # tried .append and got type error none doesn't have len # do we need to bring the index in at all?
''' user_data["watched"].append(movie)
    return user_data '''


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

def get_watched_avg_rating(user_data):
    sum = 0
    average = 0
    
    for i in range(len(user_data["watched"])):
        sum += user_data["watched"][i]["rating"]
        average = sum / len(user_data["watched"])
    
    return average
    
    
    # will use sum(len) to get the sum and divide it by the length for avg
    

# def get_most_watched_genre(user_data):



# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
