# ------------- WAVE 1 --------------------

from operator import length_hint


def create_movie(title, genre, rating):
    movie = {}
    # check if the parameters are truthy
    if title and genre and rating :
        movie["title"] = title
        movie["genre"] = genre
        movie["rating"] = rating
        return movie
    else :
        return None


def add_to_watched(user_data, movie):

    user_data["watched"].append(movie)
    return user_data  


def add_to_watchlist(user_data, movie) :
    user_data["watchlist"].append(movie)     
    return user_data


def watch_movie(user_data, title):

    for movie in user_data["watchlist"]:
        if movie["title"] == title :
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
            
    return user_data
        






# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    sum = 0
    average = 0
    length = len(user_data["watched"])
    for i in range(length):
        sum += user_data["watched"][i]["rating"]
        average = sum / length

    return average   


def get_most_watched_genre(user_data):
    genre_dict = {}
    length = len(user_data["watched"])
    if length > 0 :
        for i in range(length):
            genre = user_data["watched"][i]["genre"]
            if genre in genre_dict.keys():
                genre_dict[genre] +=1
            else :
                genre_dict[genre] = 1

        # now that I have my genre_dict I can sort
        #  the list of values and get the last number as the most occoring      
        # genre_dict_values = genre_dict.values()
        # genre_dict_keys = genre_dict.keys()
        genre_list = []
        for k, v in genre_dict.items():
            genre_list.append((v, k))
        genre_list.sort(reverse = True)
        return genre_list[0][1]
    else :
        return None

            

        # sorted_genre_dict_values = list(genre_dict_values).sort(reverse = True)
        # most_occurring = sorted_genre_dict_values[0]

        # for i in range(len(genre_dict)):
        """
            if genre_dict[genre_dict_keys[i]]== most_occurring :
                return genre_dict_keys[i]
            else :
                return None

    else :
        return None 
        """             



    

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------


