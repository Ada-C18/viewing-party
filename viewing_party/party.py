# ------------- WAVE 1 --------------------

from tkinter.tix import InputOnly


def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None
        # validate input
    new_dict = {}
    new_dict["title"] = title
    new_dict["genre"] = genre
    new_dict["rating"] = rating
    # if not new_dict["key"]
    # for key in new_dict:
    #     if not new_dict[key]:
    #         return None
    return new_dict


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            i = user_data["watchlist"].index(movie)
            user_data["watchlist"].pop(i)
    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------

def get_watched_avg_rating(user_data):
    if not user_data["watched"]:
        return 0.0

    rating_list=[]
    for movie in user_data["watched"]:
        if movie["rating"]> 0:
            rating_list.append(movie["rating"])
    
    rating_sum=sum(rating_list)
    ave_rating=rating_sum/len(rating_list)
    
    return ave_rating
    

def get_most_watched_genre(user_data):
    if not user_data["watched"]:
        return None
    frequent_genre_counter={}
    for movie in user_data["watched"]:
        genre = movie["genre"]
        if genre in frequent_genre_counter:
            frequent_genre_counter[genre]+=1
        else:
            frequent_genre_counter[genre]=1
    max_genre = max(frequent_genre_counter.values())
    for key in frequent_genre_counter:
        if frequent_genre_counter[key]== max_genre:
            return key
    

# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------

def get_unique_watched(user_data):
    # user_data= watched
    # input return user_data which is a dict
    # output return list of dictionaries, (movies we've seen only

    #=movies I saw
    
    # movies_i_saw=user_data["watched"]
    # movies_they_saw=user_data["friends"]["watched"]
    my_movies=[]
    same_movies=[]
    
    for movie in user_data["watched"]:
        for friend in user_data["friends"]:# friend is a dict with watched key referring to list of movies
            if movie in friend["watched"]:
                same_movies.append(movie)
    for movies in user_data["watched"]:
        if movies not in same_movies:
            my_movies.append(movies)
    return  my_movies

def get_friends_unique_watched(user_data):
    friend_movies=[]
    # same_movies=[]
    # for friend in user_data["friends"]:# friend is a dict with watched key referring to list of movies
    #           for movie in user_data["watched"]:
    #         if movie in friend["watched"]:
    #             same_movies.append(movie)
    #             print(f"{friend}")
    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie not in friend_movies:
                friend_movies.append(movie)
    return friend_movies


    """
    user_data= watched
    input return user_data which is a dict
    output return list of dictionaries, (movies we've seen only

    user_data["watched"]#=movies I saw
    user_data["friends"]["watched"]
    movies_i_saw=["Jaws","Titanic","Avatar"]
    movies_they_saw=["Jaws","Inception"]
    final_answer=[list of movies I've seen and friends haven't]
    delete_movies=[this is where shared movies go]
    for elem in movies_i_saw:
        if elem in movies_they_saw:
            delete_movies.append(elem)
    for movies in movies_i_saw:
        if movies not in delete_movies:
            final_answer.append(movies)
    return final_answer

    """

# -----------------------------------------
#input: dict user_data
#outpus: list of dictionaries
        
# -----------------------------------------
# ------------- WAVE 4 --------------------

def get_available_recs(user_data):
    rec_movie_list=[]
    subscriptions_list= user_data["subscriptions"]
    host_str_list= friend["watched"]["movie"]

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            if movie not in user_data["watched"] and movie in rec_movie_list and friend["watched"]["movie"]:
                rec_movie_list.append()
# -----------------------------------------

# -----------------------------------------
#input=
#output=
# ------------- WAVE 5 --------------------
# def get_new_rec_by_genre(user_data):
#     rec_movies=[]
#     #genre=
#     # get most frequent movie["genre"]

#     if movie not in user_data["watched"] and movie in rec_movies and genre the same as user frequent
#     return rec_movies

# def get_rec_from_favorites(user_data):

# -----------------------------------------
