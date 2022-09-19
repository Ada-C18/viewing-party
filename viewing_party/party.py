from statistics import mode 



# ------------- WAVE 1 --------------------

from itertools import count


def create_movie(title, genre, rating):
    movie_dict={}
    if not title or not genre or not rating:
        return None
    else: 
        movie_dict["title"]=title
        movie_dict["genre"]=genre
        movie_dict["rating"]=rating
    return movie_dict


def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data



def watch_movie(user_data,title):
    for movie in user_data["watchlist"]:
        if movie["title"]==title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)


    return user_data


# Create a function named `watch_movie`. This function should...

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

watch_movie({
        "watchlist": [{'genre': 'Horror', 'rating': 3.5, 'title': 'It Came from the Stack Trace'},
{   'genre': 'Fantasy',
    'rating': 4.8,
    'title': 'The Lord of the Functions: The Fellowship of the Function'}],
    
    "watched": [{ 'genre': 'Fantasy',
    'rating': 4.0,
    'title': 'The Lord of the Functions: The Two Parameters'}]
    },'It Came from the Stack Trace')




# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    count_of_ratings=0
    sum_of_ratings=0
    for list in user_data["watched"]:
        for rate,score in list.items():
            if rate=="rating":
                count_of_ratings+=1
                sum_of_ratings+=score
    if count_of_ratings==0:
        average=0
    else:
        average=sum_of_ratings/count_of_ratings
    return average



def get_most_watched_genre(user_data):
    genre_data=[]
   
    for list in user_data.values():
        for movie in list:
            if "genre" in movie:
                genre_data.append(movie["genre"])
    if len(genre_data)==0:
        most_often=None
    else: 
        most_often=mode(genre_data)
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
    user_watched=[]
    friends_watched=[]

    for watch in user_data["watched"]:
        user_watched.append(watch)
    for friend in user_data["friends"]:
        for movie in friend.values():
            for i in movie:
                friends_watched.append(i)
    
    newlist=[]

    for u in user_watched:
        if u not in friends_watched:
            newlist.append(u)
    
    return(newlist)

                

    
get_unique_watched({"watched":[{
    "title": "The Lord of the Functions: The Fellowship of the Function",
    "genre": "Fantasy",
    "rating": 4.8
},{
    "title": "The Lord of the Functions: The Two Parameters",
    "genre": "Fantasy",
    "rating": 4.0
}, {
    "title": "The Programmer: An Unexpected Stack Trace",
    "genre": "Fantasy",
    "rating": 4.0
},{
    "title": "The JavaScript and the React",
    "genre": "Action",
    "rating": 2.2
},{
    "title": "Recursion",
    "genre": "Intrigue",
    "rating": 2.0
},{
    "title": "Instructor Student TA Manager",
    "genre": "Intrigue",
    "rating": 4.5
}], "friends":[
    {
    "watched":[
    {"title": "The Lord of the Functions: The Fellowship of the Function",
    "genre": "Fantasy",
    "rating": 4.8},
    {
    "title": "The Lord of the Functions: The Two Parameters",
    "genre": "Fantasy",
    "rating": 4.0
}]
    },
{"watched":[
     {
    "title": "The Programmer: An Unexpected Stack Trace",
    "genre": "Fantasy",
    "rating": 4.0}]
    }
]})



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

    for watch in user_data["watched"]:
        user_watched.append(watch)
    for friend in user_data["friends"]:
        for movie in friend.values():
            for i in movie:
                friends_watched.append(i)
    
    user_not_watched=[]
    final_list=[]

    for f in friends_watched:
        if f not in user_watched:
            user_not_watched.append(f)
    for item in user_not_watched:
        if item not in final_list:
            final_list.append(item)

    return(final_list)
   


get_friends_unique_watched({"watched":[{
    "title": "The Lord of the Functions: The Fellowship of the Function",
    "genre": "Fantasy",
    "rating": 4.8
},{
    "title": "The Lord of the Functions: The Two Parameters",
    "genre": "Fantasy",
    "rating": 4.0
}, {
    "title": "The Programmer: An Unexpected Stack Trace",
    "genre": "Fantasy",
    "rating": 4.0
},{
    "title": "The JavaScript and the React",
    "genre": "Action",
    "rating": 2.2
},{
    "title": "Recursion",
    "genre": "Intrigue",
    "rating": 2.0
},{
    "title": "Instructor Student TA Manager",
    "genre": "Intrigue",
    "rating": 4.5
}], "friends":[
    {
    "watched":[
    {"title": "The Lord of the Functions: The Fellowship of the Function",
    "genre": "Fantasy",
    "rating": 4.8},
    {
    "title": "Zero Dark Python",
    "genre": "Intrigue",
    "rating": 3.0
},
{
    "title": "Zero Dark Python",
    "genre": "Intrigue",
    "rating": 3.0
}, {
    "title": "JavaScript 3: VS Code Lint",
    "genre": "Action",
    "rating": 3.5
},
    {
    "title": "The Lord of the Functions: The Two Parameters",
    "genre": "Fantasy",
    "rating": 4.0
}]
    },
{"watched":[
     {
    "title": "The Programmer: An Unexpected Stack Trace",
    "genre": "Fantasy",
    "rating": 4.0}]
    }, 
]})

        
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
    user_watched=[]
    friends_watched=[]

    for watch in user_data["watched"]:
        user_watched.append(watch)
    for friend in user_data["friends"]:
        for movie in friend.values():
            for i in movie:
                friends_watched.append(i)
    
    user_not_watched=[]
    no_duplicates=[]
    final_list=[]

    for f in friends_watched:
        if f not in user_watched:
            user_not_watched.append(f)
    for item in user_not_watched:
        if item not in no_duplicates:
            no_duplicates.append(item)
    
    #compare the host with the subscriptions and only return movies that match the values in subscriptions
    for i in no_duplicates:
        for sub in user_data["subscriptions"]:
            if i["host"] ==sub:
                final_list.append(i)
                
    

    return(final_list)



# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

# 1. Create a function named  `get_new_rec_by_genre`. This function should...

# - take one parameter: `user_data`
# - Consider the user's most frequently watched genre. Then, determine a list of recommended movies. A movie should be added to this list if and only if:
#   - The user has not watched it
#   - At least one of the user's friends has watched
#   - The `"genre"` of the movie is the same as the user's most frequent genre
# - Return the list of recommended movies

def get_new_rec_by_genre(user_data):

    if len(user_data["watched"])==0:
        return []

    # step 1. find the most frequent genre of user
    genre_data=[]
    for list in user_data["watched"]:
        genre_data.append(list["genre"])

    most_often=mode(genre_data)

    
#step 2: find movies the user has not watched but a friend has 
    user_watched=[]
    friends_watched=[]
    user_not_watched=[]
    no_duplicates=[]
    final_list=[]

    for watch in user_data["watched"]:
        user_watched.append(watch)
    for friend in user_data["friends"]:
        for movie in friend.values():
            for i in movie:
                friends_watched.append(i)
   
    
    #if a movie in friends_watched is not in user_watched, add to user_not_watched list
    
    for f in friends_watched:
        if f not in user_watched:
            user_not_watched.append(f)
    
        
#  remove duplicates 
    for movie in user_not_watched:
        if movie not in no_duplicates:
            no_duplicates.append(movie)

#step 3: only have movies with the genre that the user watches most 

    for movie in no_duplicates:
        if movie["genre"]==most_often:
            final_list.append(movie)


    return(final_list)



# 2. Create a function named  `get_rec_from_favorites`. This function should...

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

    for f in favorites:
        if f not in friends_list:
            recommended.append(f)
            
    return recommended
    

    

get_rec_from_favorites({   'favorites': [   {   'genre': 'Fantasy',
                         'host': 'netflix',
                         'rating': 4.8,
                         'title': 'The Lord of the Functions: The Fellowship '
                                  'of the Function'},
                     {   'genre': 'Fantasy',
                         'host': 'netflix',
                         'rating': 4.0,
                         'title': 'The Lord of the Functions: The Two '
                                  'Parameters'},
                     {   'genre': 'Intrigue',
                         'host': 'hulu',
                         'rating': 2.0,
                         'title': 'Recursion'},
                     {   'genre': 'Intrigue',
                         'host': 'disney+',
                         'rating': 4.5,
                         'title': 'Instructor Student TA Manager'}],
    'friends': [   {   'watched': [   {   'genre': 'Fantasy',
                                          'host': 'netflix',
                                          'rating': 4.8,
                                          'title': 'The Lord of the Functions: '
                                                   'The Fellowship of the '
                                                   'Function'},
                                      {   'genre': 'Fantasy',
                                          'host': 'amazon',
                                          'rating': 4.0,
                                          'title': 'The Lord of the Functions: '
                                                   'The Return of the Value'},
                                      {   'genre': 'Fantasy',
                                          'host': 'hulu',
                                          'rating': 4.0,
                                          'title': 'The Programmer: An '
                                                   'Unexpected Stack Trace'},
                                      {   'genre': 'Horror',
                                          'host': 'netflix',
                                          'rating': 3.5,
                                          'title': 'It Came from the Stack '
                                                   'Trace'}]},
                   {   'watched': [   {   'genre': 'Fantasy',
                                          'host': 'netflix',
                                          'rating': 4.8,
                                          'title': 'The Lord of the Functions: '
                                                   'The Fellowship of the '
                                                   'Function'},
                                      {   'genre': 'Action',
                                          'host': 'amazon',
                                          'rating': 2.2,
                                          'title': 'The JavaScript and the '
                                                   'React'},
                                      {   'genre': 'Intrigue',
                                          'host': 'hulu',
                                          'rating': 2.0,
                                          'title': 'Recursion'},
                                      {   'genre': 'Intrigue',
                                          'host': 'disney+',
                                          'rating': 3.0,
                                          'title': 'Zero Dark Python'}]}],
    'subscriptions': ['netflix', 'hulu'],
    'watched': [   {   'genre': 'Fantasy',
                       'host': 'netflix',
                       'rating': 4.8,
                       'title': 'The Lord of the Functions: The Fellowship of '
                                'the Function'},
                   {   'genre': 'Fantasy',
                       'host': 'netflix',
                       'rating': 4.0,
                       'title': 'The Lord of the Functions: The Two '
                                'Parameters'},
                   {   'genre': 'Fantasy',
                       'host': 'amazon',
                       'rating': 4.0,
                       'title': 'The Lord of the Functions: The Return of the '
                                'Value'},
                   {   'genre': 'Action',
                       'host': 'amazon',
                       'rating': 2.2,
                       'title': 'The JavaScript and the React'},
                   {   'genre': 'Intrigue',
                       'host': 'hulu',
                       'rating': 2.0,
                       'title': 'Recursion'},
                   {   'genre': 'Intrigue',
                       'host': 'disney+',
                       'rating': 4.5,
                       'title': 'Instructor Student TA Manager'}]})