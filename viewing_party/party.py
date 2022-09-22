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

    try:    
        popular_genre = max(genre_dictionary, key=genre_dictionary.get)
    except ValueError as err:
        popular_genre = None


    return(popular_genre)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    movie_titles_user_watched = set()
    movie_titles_friends_watched = set()
    list_of_movie_dictionaries_friends_have_not_watched = []

    for movie in user_data["watched"]:
        movie_titles_user_watched.add((movie['title']))
    
    for i in range(len(user_data["friends"])):
        for movie in user_data["friends"][i]["watched"]:
            title = movie.get("title")
            movie_titles_friends_watched.add(title)
        i += 1 
    
    movies_user_has_watched_but_not_friends = movie_titles_user_watched.difference(movie_titles_friends_watched)

    for movie in movies_user_has_watched_but_not_friends:
        for dictionary in user_data["watched"]:
            if movie == dictionary['title']:
                list_of_movie_dictionaries_friends_have_not_watched.append(dictionary)

    return(list_of_movie_dictionaries_friends_have_not_watched)

def get_friends_unique_watched(user_data):
    movie_titles_friends_watched = set()
    movie_titles_user_watched = set()
    list_of_movie_dictionaries_user_has_not_watched = []

    for i in range(len(user_data["friends"])):
        for movie in user_data["friends"][i]["watched"]:
            title = movie.get("title")
            movie_titles_friends_watched.add(title)
        i += 1
    
    for movie in user_data["watched"]:
        movie_titles_user_watched.add((movie["title"]))
    
    movies_friends_have_watched_but_not_user = movie_titles_friends_watched.difference(movie_titles_user_watched)

    for movie in movies_friends_have_watched_but_not_user:
        for i in range(len(user_data["friends"])):
            for dictionary in user_data["friends"][i]["watched"]:
                title = dictionary.get("title")
                if title == movie:
                    list_of_movie_dictionaries_user_has_not_watched.append(dictionary)
            i+=1
    
    remove_dupes = set()
    new_list_of_movie_dictionaries_user_has_not_watched = []
    for dictionary in list_of_movie_dictionaries_user_has_not_watched:
        tuple_me = tuple(dictionary.items())
        if tuple_me not in remove_dupes:
            remove_dupes.add(tuple_me)
            new_list_of_movie_dictionaries_user_has_not_watched.append(dictionary)

    return(new_list_of_movie_dictionaries_user_has_not_watched)
        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    movie_recs = []
    list_of_movie_dictionaries_user_has_not_watched_but_friend_has = get_friends_unique_watched(user_data)
    for subscription in user_data["subscriptions"]:
        for dictionary in list_of_movie_dictionaries_user_has_not_watched_but_friend_has:
            if subscription == dictionary["host"]:
                movie_recs.append(dictionary)
    
    return(movie_recs)

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    movie_recs_by_genre = []
    users_most_frequently_watched_genre = get_most_watched_genre(user_data)
    if users_most_frequently_watched_genre == None:
        movie_recs_by_genre = []
    else:
        list_of_movie_dictionaries_user_has_not_watched_but_friend_has = get_friends_unique_watched(user_data)
        for dictionary in list_of_movie_dictionaries_user_has_not_watched_but_friend_has:
            if users_most_frequently_watched_genre == dictionary["genre"]:
                movie_recs_by_genre.append(dictionary)
    
    return(movie_recs_by_genre)

