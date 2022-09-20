
# -----------------------------------------
# ------------- WAVE 1 --------------------
# -----------------------------------------

def create_movie(title, genre, rating):
    #create a dictionary with the keys 'title', 'genre', 'rating', and the values the values passed in
    if title and genre and rating:
        movie_dict = {}
        movie_dict['title'] = title
        movie_dict['genre'] = genre
        movie_dict['rating'] = rating
        return movie_dict

def add_to_watched(user_data, movie):
    #user_data is a dictionary with watched as one of the keys.
    #this function adds the movie_dict (listed here as movie) into a list stored as a value connected to watched.
    user_data['watched'].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    #this function will add a movie (which is a dict, remember) into the list stored as a value to the key 'watchlist' in the user_data dict.
    #user_data is a dictionary with 'watchlist' as one of the keys.
    user_data['watchlist'].append(movie)
    return user_data

def watch_movie(user_data, movie_title):
    #This function takes in user_data (dict of watched and watched list 
    #find the movie in watchlist that has the movie_title.
    #iterate through the list, checking each dictionary. 
    
    movie_found = False

    for movie in user_data["watchlist"]:
        if movie["title"] == movie_title:
            watched_movie = movie
            movie_found = True
            break

    if movie_found == True:
        #once you find this movie, we're going to take it off of watchlist and append it to watched.
        #print(user_data['watchlist'])
        #print(watched_movie)
        user_data['watchlist'].remove(watched_movie)
        user_data['watched'].append(watched_movie)

    return user_data

"""
#This ended up not working as expected.  Keeping it here in case I want it later.
def search(a_list, movie_title):
    #this helper function helps us search through a list and return the dictionary entry for the movie with the title of movie_hour
    #for elem in a_list:
        #if elem["title"] == movie_title:
            #return elem
        #else: 
            #return None
"""


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    #this takes in the user's data (a dictionary with 2 keys: watched and watchlist)
    #it outputs the average rating of all the movies in the dictionary 'watched'
    #I would like to save these values to a user...by making a class?  We'll see. 
    ratings_lst = []
    #this gives a list of ratings
    for movie in user_data["watched"]:
        ratings_lst.append(movie["rating"])


    #adding an if to deal with if it's an empty list:
    if len(ratings_lst) > 0:
        #this calculates the average:
        avg_rating = sum(ratings_lst) / len(ratings_lst)
        return avg_rating
    else: 
        return 0


def get_most_watched_genre(user_data):
    #This will make a dictionary, and add a count of how many times each genre appears. 
    genre_count = {}
    #keys will be genres (strings)
    #values will be the number of movies in that genre.
    #adding in an if to deal with if watched is an empty list:
    if len(user_data["watched"]) > 0:
        for movie in user_data["watched"]:
            genre = movie["genre"]
            if genre not in genre_count:
                genre_count[genre] = 1
            else:
                genre_count[genre] += 1
        #now, genre_count is complete.  Let's return which key has the highest value associated with it.
        most_watched_genre = max(genre_count, key = genre_count.get)
        return most_watched_genre
    else:
        return None

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(user_data):
    #takes in user_data (a dictionary with 3 keys, watched and watchlist and friends)
    #now, user_data has a third key: "friends".
    #the value associated with this is a list of dictionaries, one dictionary per friend.
    # The dictionary for each friend has "watched", with a list of movies. (which is itself a dict, remember.) 
    #This function outputs the list of movies (dicts) in watched that are unique, and not watched by another friend.
    
    user_watched_titles = get_user_watched_titles(user_data)
    friend_watched_titles = get_friends_watched_titles(user_data)

    #set difference
    unique_watched_titles = user_watched_titles - friend_watched_titles

    #retrieve the dictionary entries from the original user_data
    unique_watched_movies = []
    for movie in user_data["watched"]:
        if movie["title"] in unique_watched_titles:
            unique_watched_movies.append(movie)
            unique_watched_titles.remove(movie["title"]) #remove it to prevent duplicates
    return unique_watched_movies

def get_user_watched_titles(user_data):
    #returns a set of titles user has watched.
    user_watched_titles = []
    for movie in user_data['watched']:
        user_watched_titles.append(movie["title"])
    return set(user_watched_titles)

def get_friends_watched_titles(user_data):
    #returns a set of titles of movies friend has watched.
    friend_watched_titles = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friend_watched_titles.append(movie["title"])
    return set(friend_watched_titles)


def get_friends_unique_watched(user_data):
    #this takes in user_data (with keys including 'watched' and 'friends')
    # it returns a list of dictionaries of all the movies a friend(s) has watched that user hasn't.  
    friend_watched_titles = get_friends_watched_titles(user_data)
    user_watched_titles = get_user_watched_titles(user_data)
    friends_unique_titles = friend_watched_titles - user_watched_titles

    #retrieve info from user_data matching the titles
    unique_watched = []
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie["title"] in friends_unique_titles and movie not in unique_watched:
                unique_watched.append(movie)
    return unique_watched

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------


def get_available_recs(user_data):
    #this will return a list of movies that:
    #the user has not watched
    #at least one of the user's friends has watched
    #is on a streaming service that the user has. 

    friends_uniqued_watched = get_friends_unique_watched(user_data)
    # here we filter for movies in the users subscription list.
    recommendations = []
    for movie in friends_uniqued_watched:
        if movie["host"] in user_data["subscriptions"]:
            recommendations.append(movie)

    return recommendations



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

