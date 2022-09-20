# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    pass
    #make a dictionary with these keys: "title","genre","rating"
    movie_dict = {}
    movie_dict["title"]= title
    movie_dict["genre"] = genre
    movie_dict["rating"] = rating
    
    information = [title,genre,rating]
    if None in information:
        return None
    else:
        return movie_dict

def add_to_watched(user_data, movie):
    user_data["watched"] = [movie]
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"] = [movie]
    return user_data 

def watch_movie(user_data,title):
    watched_movie = title
    for movie in user_data["watchlist"]:
        for value in movie.values():
            if value == watched_movie:
                user_data["watchlist"].remove(movie)
                user_data["watched"].append(movie)

    return(user_data)

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    ratings = []
    ratings_sum = 0

    if(len(user_data["watched"])) is 0:
        ratings_average = 0.0
    else:
        for i in range(len(user_data["watched"])):
            ratings.append((user_data["watched"][i]["rating"]))
            i+=1
    
        for rating in ratings:
            ratings_sum += rating
        
        ratings_average = ratings_sum / len(ratings)

    return ratings_average  

def get_most_watched_genre(user_data):
    genre_list = []
    genre_dictionary = {}

    if (len(user_data["watched"])) is 0:
        popular_genre = None
    else:
        for i in range(len(user_data["watched"])):
            genre_list.append((user_data["watched"][i]["genre"]))
            i += 1
    
    for genre in genre_list:
        count = genre_list.count(genre)
        genre_dictionary[genre] = count
        
    popular_genre = max(genre_dictionary, key=genre_dictionary.get)
    return(popular_genre)






# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

