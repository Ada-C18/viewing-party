from statistics import mode

# ------------- WAVE 1 --------------------

# 1. Create a function named `create_movie`. This function and all subsequent functions should be in `party.py`. `create_movie` should...

# - take three parameters: `title`, `genre`, `rating`
# - If those three attributes are truthy, then return a dictionary. This dictionary should...
#   - Have three key-value pairs, with specific keys
#   - The three keys should be `"title"`, `"genre"`, and `"rating"`
#   - The values of these key-value pairs should be appropriate values
# - If `title` is falsy, `genre` is falsy, or `rating` is falsy, this function should return `None`

def create_movie(title, genre, rating):
    movie_dict={}
    if not title or not genre or not rating:
        return None
    movie_dict["title"]=title
    movie_dict["genre"]=genre
    movie_dict["rating"]=rating
    return movie_dict

# 2. Create a function named `add_to_watched`. This function should...

# - take two parameters: `user_data`, `movie`
#   - the value of `user_data` will be a dictionary with a key `"watched"`, and a value which is a list of dictionaries representing the movies the user has watched
#     - An empty list represents that the user has no movies in their watched list
#   - the value of `movie` will be a dictionary in this format:
#     - ```python
#       {
#         "title": "Title A",
#         "genre": "Horror",
#         "rating": 3.5
#       }
#       ```
# - add the `movie` to the `"watched"` list inside of `user_data`
# - return the `user_data`


def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return user_data

# 3. Create a function named `add_to_watchlist`. This function should...

# - take two parameters: `user_data`, `movie`
#   - the value of `user_data` will be a dictionary with a key `"watchlist"`, and a value which is a list of dictionaries representing the movies the user wants to watch
#     - An empty list represents that the user has no movies in their watchlist
#   - the value of `movie` will be a dictionary in this format:
#     - ```python
#       {
#         "title": "Title A",
#         "genre": "Horror",
#         "rating": 3.5
#       }
#       ```
# - add the `movie` to the `"watchlist"` list inside of `user_data`
# - return the `user_data`

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

# 4. Create a function named `watch_movie`. This function should...

# - take two parameters: `user_data`, `title`
#   - the value of `user_data` will be a dictionary with a `"watchlist"` and a `"watched"`
#     - This represents that the user has a watchlist and a list of watched movies
#   - the value of `title` will be a string
#     - This represents the title of the movie the user has watched
# - If the title is in a movie in the user's watchlist:
#   - remove that movie from the watchlist
#   - add that movie to watched
#   - return the `user_data`
# - If the title is not a movie in the user's watchlist:
#   - return the `user_data`



def watch_movie(user_data,title):
    for movie in user_data["watchlist"]:
        if movie["title"]==title:
            user_data["watched"].append(movie) 
            user_data["watchlist"].remove(movie)

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

# 1. Create a function named `get_watched_avg_rating`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries
#     - This represents that the user has a list of watched movies
# - Calculate the average rating of all movies in the watched list
#   - The average rating of an empty watched list is `0.0`
# - return the average rating

def get_watched_avg_rating(user_data):
    
    count_of_ratings=0
    sum_of_ratings=0
    average=0
    
    for watched in user_data["watched"]:
        sum_of_ratings+=(watched["rating"])
        count_of_ratings+=1
    
    if count_of_ratings==0:
        return average
    
    average=sum_of_ratings/count_of_ratings
    return average

# 2. Create a function named `get_most_watched_genre`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries. Each movie dictionary has a key `"genre"`.
#     - This represents that the user has a list of watched movies. Each watched movie has a genre.
#     - The values of `"genre"` is a string.
# - Determine which genre is most frequently occurring in the watched list
# - return the genre that is the most frequently watched
# - If the value of "watched" is an empty list, `get_most_watched_genre` should return `None`.


def get_most_watched_genre(user_data):

    genre=[x["genre"] for x in user_data["watched"]]
    most_often=None

    if len(genre)==0:
        return most_often
    
    most_often=mode(genre)
    return(most_often)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

# 1. Create a function named `get_unique_watched`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
#     - This represents that the user has a list of watched movies and a list of friends
#     - The value of `"friends"` is a list
#     - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
#     - Each movie dictionary has a `"title"`.
# - Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies the user has watched, but none of their friends have watched.
# - Return a list of dictionaries, that represents a list of movies


def get_unique_watched(user_data):

    user_unique_movie=[]
    friends_watched=[]
    
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)
    
    for watch in user_data["watched"]:
         if watch not in friends_watched:
             user_unique_movie.append(watch)
    
    return(user_unique_movie)

# 2. Create a function named `get_friends_unique_watched`. This function should...

# - take one parameter: `user_data`
#   - the value of `user_data` will be a dictionary with a `"watched"` list of movie dictionaries, and a `"friends"`
#     - This represents that the user has a list of watched movies and a list of friends
#     - The value of `"friends"` is a list
#     - Each item in `"friends"` is a dictionary. This dictionary has a key `"watched"`, which has a list of movie dictionaries.
#     - Each movie dictionary has a `"title"`.
# - Consider the movies that the user has watched, and consider the movies that their friends have watched. Determine which movies at least one of the user's friends have watched, but the user has not watched.
# - Return a list of dictionaries, that represents a list of movies
  


def get_friends_unique_watched(user_data):
    
    user_watched=[]
    friends_watched=[]  
    user_not_watched=[]
    friends_unique_movies=[]

    for watch in user_data["watched"]:
        user_watched.append(watch)
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            friends_watched.append(movie)
   
    for film in friends_watched:
        if film not in user_watched:
            user_not_watched.append(film)
    for film in user_not_watched:
        if film not in friends_unique_movies:
            friends_unique_movies.append(film)

    return(friends_unique_movies)



        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# 1. Create a function named `get_available_recs`. This function should...

# - take one parameter: `user_data`
#   - `user_data` will have a field `"subscriptions"`. The value of `"subscriptions"` is a list of strings
#     - This represents the names of streaming services that the user has access to
#     - Each friend in `"friends"` has a watched list. Each movie in the watched list has a `"host"`, which is a string that says what streaming service it's hosted on
# - Determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"host"` of the movie is a service that is in the user's `"subscriptions"`
# - Return the list of recommended movies


def get_available_recs(user_data):
    
    final_list=[]

    friends_unique_movie=get_friends_unique_watched(user_data)

    # compare the host with the subscriptions and only return movies that match the values in subscriptions

    for movie in friends_unique_movie: 
        for subscription in user_data["subscriptions"]:
            if movie["host"] ==subscription:
                final_list.append(movie)
                

    return(final_list)



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# 1. Create a function named `get_new_rec_by_genre`. This function should...

# - take one parameter: `user_data`
# - Consider the user's most frequently watched genre. Then, determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"genre"` of the movie is the same as the user's most frequent genre
# - Return the list of recommended movies

def get_new_rec_by_genre(user_data):

    genre_data=[]
    final_list=[]
    
    if len(user_data["watched"])==0:
        return []

# find the most frequent genre of user
    
    for list in user_data["watched"]:
        genre_data.append(list["genre"])

    most_often=mode(genre_data)
    
# find movies the user has not watched but a friend has 
    
    friends_unique=get_friends_unique_watched(user_data)

# only have movies with the genre that the user watches most 
   
    for movie in friends_unique:
        if movie["genre"]==most_often:
            final_list.append(movie)
  
    return(final_list)



# 2. Create a function named `get_rec_from_favorites`. This function should...

# - take one parameter: `user_data`
#   - `user_data` will have a field `"favorites"`. The value of `"favorites"` is a list of movie dictionaries
#     - This represents the user's favorite movies
# - Determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The movie is in the user's `"favorites"`
#   - None of the user's friends have watched it
# - Return the list of recommended movies


def get_rec_from_favorites(user_data):
    favorites=[]
    recommended=[]
    friends_list=[]

    for fave in user_data["favorites"]:
        favorites.append(fave)
    for watch in user_data["friends"]:
        for movie in watch["watched"]:
            friends_list.append(movie)

    for movie in favorites:
        if movie not in friends_list:
            recommended.append(movie)
            
    return recommended
    

    

