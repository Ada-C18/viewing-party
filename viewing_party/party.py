# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    '''
    create_movie(title, genre, rating):
    
    takes three parameters: `title`, `genre`, `rating`
    If those three attributes are truthy, then return a dictionary. This dictionary should...
    Have three key-value pairs, with specific keys
    The three keys should be `"title"`, `"genre"`, and `"rating"`
    The values of these key-value pairs should be appropriate values
    If `title` is falsy, `genre` is falsy, or `rating` is falsy, this function should return `None`

    returns movie_dictionary
    '''
    if (not title) or (not genre) or (not rating):
        # here we check if we have any of the attributes are falsy, we return None 
        return None

    movie_dictionary = {} #create empty dictionary

    movie_dictionary["title"] = title #add key "title" with corresponding value
    movie_dictionary["genre"] = genre #add key "genre" with corresponding value
    movie_dictionary["rating"] = rating #add key "rating" with corresponding value
   
    return movie_dictionary

def add_to_watched(user_data, movie):
    '''
    - take two parameters: `user_data`, `movie`        
    - add the `movie` to the `"watched"` list inside of `user_data`
    - return the `user_data`    
    '''

    #appending the dictionary "movie" to the list user_data["watched"]
    user_data["watched"].append(movie) 
    return user_data
    
def add_to_watchlist(user_data, movie):       
    '''
    - take two parameters: `user_data`, `movie`        
    - add the `movie` to the `"watchlist"` list inside of `user_data`
    - return the `user_data`    
    '''    

    #appending the dictionary "movie" to the list user_data["watchlist"]
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    '''
    - take two parameters: `user_data`, `title`
    - If the title is in a movie in the user's watchlist:
        - remove that movie from the watchlist
        - add that movie to watched
        - return the `user_data`
    - If the title is not a movie in the user's watchlist:
        - return the `user_data`
    '''
    # using the for loop to iterate through the list user_data["watchlist"]
    for movie in user_data["watchlist"]:
        # and check if the movie's title is what we're looking for,    
        if movie["title"] == title:
            # then we add it to the "watched"            
            user_data["watched"].append(movie)
            # and remove it from the "watchlist"           
            user_data["watchlist"].remove(movie)           

    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    '''
    - take one parameter: `user_data`
    - Calculate the average rating of all movies in the watched list
    - The average rating of an empty watched list is `0.0`
    - return the average rating
    '''
    #creating basic variables that we'll need
    average_rating = 0.0
    total = 0.0

    #if the "watched is empty, we return 0.0"
    if len(user_data["watched"]) == 0:
        return 0.0
    else:
        #using the for loop to iterate through every movie in "watched"
        for movie in user_data["watched"]:
            #and calculate total sum of movie ratings
            total += movie["rating"]
        #number of movies equals the length of "watched"    
        movie_count = len(user_data["watched"])
        average_rating = total/movie_count
        return average_rating    

def get_most_watched_genre(user_data):
    '''
    - take one parameter: `user_data`
    - Determine which genre is most frequently occurring in the watched list
    - return the genre that is the most frequently watched
    - If the value of "watched" is an empty list, `get_most_watched_genre` should return `None`.
    
    '''

    # creating an empty dictionary fo genres to calculate frequency
    # genre will be a key and frequency a value
    genres = {} 
    if len(user_data["watched"]) == 0: #if "watched" is empty, we return None
        return None
    else:
        #using a for loop to iterate through "watched"
        for movie in user_data["watched"]:
            #if it's a first time we encounter this genre we create key/value pair with value "1"
            if movie["genre"] not in genres:
                genres[movie["genre"]] = 1
            #if we already have this key, we add 1 to the value
            else:
                genres[movie["genre"]] += 1
        
        #Here I wanted to use max function and found a method to get the specific key corresponding to this max value.
        #I'm not checking an edge case where there's two exact same frequencies with maximum value
        most_watched_genre = max(genres, key=genres.get)

        #we can also do something like this:
        # frequency_list = genres.values()
        # max_value = max(frequency_list)
        # for genre in genres:
        #     if genres[genre] == max_value:
        #         most_watched_genre = genre
                #and this loop might be updated to catch several genres with the same frequency

        return most_watched_genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_user_movies_list(user_data, category):
    '''
    helper function get_user_movies_list
    - creates a list of titles of a requiered category ("watched", "watchlist" or "favorites")
    - returns list of titles
    '''
    #creating empty list
    movies_list = []
    #using for loop to iterate through this entire category and add all the titles to the list
    for movie in user_data[category]:
        movies_list.append(movie["title"])

    return movies_list

def get_friends_watched_movies_list(user_data):
    '''
    helper function get_friends_watched_movies_list
    - creates a list of titles of a "watched" category
    - returns list of titles
    '''
    #creating an empty list
    movies_list = []
    #using for loop to iterate by each friend
    for friend in user_data["friends"]:
        #using for loop to iterate by each movie in friend's watched list
        for movie in friend["watched"]:
            #append all the titles to the list
            movies_list.append(movie["title"])
    return movies_list

def use_set_to_compare_lists_return_list(main_list, list_to_compare):
    '''
    helper function use_set_to_compare_lists_return_list
    - takes to lists (list 1, list 2)
    - returns the difference between list 1 and list 2, 
    - unique values of a list 1, that are not found in the list 2
    '''
    #convirting lists we received in the function call to sets
    main_set = set(main_list)
    set_to_compare = set(list_to_compare)

    #calculating set difference
    difference_set = main_set - set_to_compare
    #re-convirting this difference set to list
    difference_list = list(difference_set)

    return difference_list

def convert_titles_into_list_of_movies_dict(user_data, list_of_titles, user, category):
    '''
    helpers function convert_titles_into_list_of_movies_dict
    - takes user_data, list_of_titles, user and category
    - user will be True for user and False for friends
    - category might be "watched", "watchlist" or "favorites"
    - uses user_data and list_of_titles to create a movie dictionary with all the movie info inside
    - returns the list "result" with movie dictionaries
    '''

    #empty result list
    result = []
    #using for loop to iterate through our titles in list_of_titles
    for title in list_of_titles:
        # if user is True, which means that we are working with user info
        if user:
            #using for loop to iterate through each movie in a category
            for movie in user_data[category]:
                # and if we find our title,
                if title == movie["title"]:
                    # we add the whole movie to our result list
                    result.append(movie)
        else: #if user is false, we're working with friends info
            #for each friend in the list
            for friend in user_data["friends"]:
                #for each movie in "watched"
                for movie in friend["watched"]:
                    # and if we find our title and movie is not yet there from another friend,
                    if title == movie["title"] and movie not in result:
                        # we add the whole movie to our result list
                        result.append(movie)

    return result

def get_unique_watched(user_data):
    '''
    - take one parameter: `user_data` 
    - Determine which movies the user has watched, but none of their friends have watched.
    - Return a list of dictionaries, that represents a list of movies
    '''

    # using helper function to create a list of titles of movies that user has watched
    user_watched_list = get_user_movies_list(user_data, "watched")

    # using helper function to create a list of titles of movies that friends have watched
    all_friends_movies_list = get_friends_watched_movies_list(user_data)

    #creating a list of unique titles of movies that user has watched
    user_unique_movies_list = use_set_to_compare_lists_return_list(user_watched_list, all_friends_movies_list)

    #we need this user parameter for the helper function convert_titles_into_list_of_movies_dict
    # to tell it whether we access user data of friends data
    user = True

    final_result = convert_titles_into_list_of_movies_dict(user_data, user_unique_movies_list, user, "watched")

    return final_result

def get_friends_unique_watched(user_data):
    '''
    - take one parameter: `user_data` 
    - Determine which movies from the friends list the user hasn't watched
    - Return a list of dictionaries, that represents a list of movies
    '''
    # using helper function to create a list of titles of movies that user has watched
    user_watched_list = get_user_movies_list(user_data, "watched")

    # using helper function to create a list of titles of movies that friends have watched
    all_friends_movies_list = get_friends_watched_movies_list(user_data)

    #creating a list of unique titles of friends movies that user hasn't watched
    friends_unique_movies_list = use_set_to_compare_lists_return_list(all_friends_movies_list, user_watched_list)

    #we need this user parameter for the helper function convert_titles_into_list_of_movies_dict
    # to tell it that we want to access friends data
    user = False

    final_result = convert_titles_into_list_of_movies_dict(user_data, friends_unique_movies_list, user, "")

    return final_result

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    '''
    - take one parameter: `user_data`
    - Determine a list of recommended movies. A movie should be added to this list if and only if:
        - The user has not watched it
        - At least one of the user's friends has watched
        - The `"host"` of the movie is a service that is in the user's `"subscriptions"`
    - Return the list of recommended movies
    '''
    # we're extracting available hosts from user_data["subscriptions"]
    # and store them in the list
    available_hosts = user_data["subscriptions"]

    # we're using the function get_friends_unique_watched
    # to get all the unique movies the user hasn't watched
    unique_movies_from_friends = get_friends_unique_watched(user_data)

    # creating an empty list to store result
    result = []


    # using for loop to iterate through unique movies user hasn't watched
    for movie in unique_movies_from_friends:
        #checking if the "host" for that movie is available for the user
        if movie["host"] in available_hosts:
            # if yes, we append the movie to the result
            result.append(movie)

    return result

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    '''
    - take one parameter: `user_data`
    - Consider the user's most frequently watched genre. 
    - Then, determine a list of recommended movies. A movie should be added to this list if and only if:
        - The user has not watched it
        - At least one of the user's friends has watched
        - The `"genre"` of the movie is the same as the user's most frequent genre
    '''

    # so we use our get_friends_unique_watched function to get all the movies user didn't watch
    friends_recommendations = get_friends_unique_watched(user_data)

    # and we use get_most_watched_genre to get user's favorite genre
    users_favorite_genre = get_most_watched_genre(user_data)

    #empty list fo the result
    result = []

    # using for loop to go through each movie in friends recommendations
    for movie in friends_recommendations:
        #if movie's genre is the users favorite genre
        if movie["genre"] == users_favorite_genre:
            #we add it to the result
            result.append(movie)
    
    return result


def get_rec_from_favorites(user_data):
    '''
    - take one parameter: `user_data`
    - Determine a list of recommended movies. 
    - A movie should be added to this list if and only if:
        - The movie is in the user's `"favorites"`
        - None of the user's friends have watched it
        - Return the list of recommended movies
    '''

    # using helper function to create a list of titles of movies that user has watched
    user_watched_list = get_user_movies_list(user_data, "favorites")

    # using helper function to create a list of titles of movies that friends have watched
    all_friends_movies_list = get_friends_watched_movies_list(user_data)

    #creating a list of unique titles of movies that user has watched and his friends didn't
    recomendation_titles_list = use_set_to_compare_lists_return_list(user_watched_list, all_friends_movies_list)

    #we need this user parameter for the helper function convert_titles_into_list_of_movies_dict
    # to tell it whether we access user data of friends data
    user = True
    final_result = convert_titles_into_list_of_movies_dict(user_data, recomendation_titles_list, user, "favorites")

    return final_result

