# ------------- WAVE 1 --------------------

from shutil import move


def create_movie(title, genre, rating):
    if title == None or genre == None or rating == None:
        return None
    else:
        movie_dict= {}
        movie_dict["title"] = title
        movie_dict["genre"] = genre
        movie_dict["rating"] = rating
        return movie_dict


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"]== title:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
        
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    average_rating = 0
    sum = 0
    lenght = len(user_data["watched"])
    for i in range(lenght):
        sum += user_data["watched"][i]["rating"]
        average_rating = sum/lenght 
    return average_rating

def get_most_watched_genre(user_data):
    genre_movie ={}
    lenght = len(user_data["watched"])
    if lenght == 0:
        return None
    else:  
        for i in range(lenght):
            genre = user_data["watched"][i]["genre"]
            if genre in genre_movie:
                genre_movie[genre] +=1
            else:
                genre_movie[genre]=1

        genre_movie_list =[]
        for k, v in genre_movie.items():
            genre_movie_list.append((v,k))
        genre_movie_list.sort()
        return genre_movie_list[-1][1]





      


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

