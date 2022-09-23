# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    #make a dictionary with these keys:
    movie_dict = {}
    movie_dict["title"]= title # appropriate values
    movie_dict["genre"]= genre  # appropriate values
    movie_dict["rating"]= rating # appropriate values
    information = [title, genre, rating]
        
    if None in information: # if title, genre, rating is falsy return None
        return None
    else:
            return movie_dict

def add_to_watched(user_data, movie):
    # Add a movie to a watched list in user data and return user data
    user_data["watched"].append(movie) # add movie to the "watched" list inside user_data
    return user_data
    
def add_to_watchlist(user_data, movie):
    #movies the user wants to watch
    user_data["watchlist"].append(movie) # add the movie to the "watchlist" list inside user_data
    return user_data

def watch_movie (user_data, title):
    
    for movie in user_data["watchlist"]: 
        if title == movie["title"]: #if the title is in a movie in the use's watchlist
            user_data["watchlist"].remove(movie) # remove that movie from watchlist
            add_to_watched(user_data, movie) # add that movie to watched
    return user_data
        # else:
        #     return user_data
    
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    #take dict of "watched" values are a list of movies return a list of the average rating of movies if list is empty return 0.0
    total_rating = 0.0
    average_rating = 0.0
    
    if user_data["watched"]:
        for movie in range(len(user_data["watched"])):
            total_rating += user_data["watched"][movie]["rating"]
        average_rating = total_rating / len(user_data["watched"])
    return average_rating

def get_most_watched_genre(user_data):
    # find the most popular movie genre
    genre_list = []
    
    for i in user_data: # looping the dictionary
        if i == "watched": # looking for "watched" list
            if not user_data[i]: #return most_popular_genre as None if "watched" list is empty
                most_popular_genre = None
                return most_popular_genre
            else:
                for item in user_data[i]: #if "watched" list not empty 
                    for movie_items in item:
                        if movie_items == "genre": #append "genre" to empty genre_list
                            genre_list.append(item[movie_items])
                most_popular_genre = max(set(genre_list), key = genre_list.count) #looking for most popular genre in the list
    return most_popular_genre
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    #unique movies only by user and return list
    watched_by_user = user_data['watched']
    watched_by_friends = get_movies_watched_by_friends(user_data)
    user_unique_movies = []
    for user_movie in watched_by_user:
        if user_movie not in watched_by_friends and user_movie not in user_unique_movies:
                user_unique_movies.append(user_movie)
    return user_unique_movies

def get_movies_watched_by_friends(user_data):
    #all friends whatched movies togheter and return a list
    watched_by_friends = []

    for friends in user_data['friends']:
        for movies in friends.values():
            for movie in movies:
                watched_by_friends.append(movie)
    return watched_by_friends

def get_friends_unique_watched(user_data):
    #look for unique movies watched only by friends and return list
    watched_by_user = user_data['watched'] 
    watched_by_friends = get_movies_watched_by_friends(user_data) 
    friends_movies_unique = []

    for movie in watched_by_friends:
        if movie not in watched_by_user and movie not in friends_movies_unique:
            friends_movies_unique.append(movie)
    
    return friends_movies_unique

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    movie_friends_watched_list = get_friends_unique_watched(user_data) # from wave 3
    final_list = list()

    for movie in movie_friends_watched_list:
        if movie["host"] in user_data["subscriptions"]:
            final_list.append(movie)
    return final_list

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    
    recommended_movies = []
    friends_watched = get_friends_unique_watched(user_data) # from wave 3
    most_watched_genre = get_most_watched_genre(user_data) # from wave 2

    for movie in friends_watched:
        if movie["genre"] == most_watched_genre:
            recommended_movies.append(movie)
    return recommended_movies

def get_rec_from_favorites(user_data):
    recommended_movies = []
    friends_titles_watched = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_titles_watched.append(movie["title"])
    
    for movie in user_data["favorites"]:
        if movie["title"] not in friends_titles_watched:
            recommended_movies.append(movie)

    return recommended_movies
