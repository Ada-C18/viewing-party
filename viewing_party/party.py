# ------------- WAVE 1 --------------------

from symbol import single_input


def create_movie(title, genre, rating): #Wave 1, step 1 done
    movie_dict={}
    if title is None or genre is None or rating is None:
        return None

    movie_dict["title"]=title
    movie_dict["genre"]=genre
    movie_dict["rating"]=rating
    return movie_dict

def add_to_watched(user_watched_dict,movie_info):
    user_watched_dict["watched"] = [movie_info]
    return user_watched_dict

def add_to_watchlist(user_watchlist_dict, movie_info):
    user_watchlist_dict["watchlist"] = [movie_info]
    return user_watchlist_dict

def watch_movie(single_user_data,movie_title):    
    list_of_watchlist_movie_info=single_user_data["watchlist"]
    list_of_watched_movie_info=single_user_data["watched"]

    #Adds movie info to list of watched movies if it is in the watchlist and then removes the movie info from the watchlist
    for index,movie_info in enumerate(list_of_watchlist_movie_info):
        if movie_title == movie_info["title"]:
            list_of_watched_movie_info.append(movie_info)
            list_of_watchlist_movie_info.pop(index)
    return single_user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(single_user_data):
    list_of_watched_movie_info=single_user_data["watched"]
    
    #Calculates the number of watched movies
    number_of_watched_movies=len(list_of_watched_movie_info)

    list_of_movie_ratings=[]
    sum_of_all_ratings=0

    if len(list_of_watched_movie_info) == 0:
        return 0.0

    #Adds rating of each watched movie to a list
    for movie_info in list_of_watched_movie_info:
        list_of_movie_ratings.append(movie_info["rating"])

    #Determines the sum of all ratings
    for rating in list_of_movie_ratings:
        sum_of_all_ratings+=rating

    #Calculates the average rating using the sum of all ratings and the number of movies
    average_rating=sum_of_all_ratings/number_of_watched_movies
    return average_rating

def get_most_watched_genre(single_user_data):
    list_of_watched_movie_info=single_user_data["watched"]
    list_of_genres=[]
    genre_counter_dict={}
    list_of_watched_genre_counts=[]

    if len(list_of_watched_movie_info) == 0:
        return None

    #Adds genre of each watched movie to a list
    for movie_info in list_of_watched_movie_info:
        list_of_genres.append(movie_info['genre'])

    #Adds genre as the key to a dictionary with a value that counts the number of times it is in the genre list
    for genre in list_of_genres:
        if not genre in genre_counter_dict:
            genre_counter_dict[genre] = 1
        else:
            genre_counter_dict[genre] += 1

    #Adds genre count values to a list
    for genre_count_value in genre_counter_dict.values():
        list_of_watched_genre_counts.append(genre_count_value)

    #Determines the highest genre count value
    max_watched_genre_count=max(list_of_watched_genre_counts)

    #Returns a genre from the genre:counter dictionary with a counter value that is the same as the highest genre count value
    for genre,genre_count_value in genre_counter_dict.items():
        if genre_count_value == max_watched_genre_count:
            return genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_unique_watched(single_user_data):
    list_of_user_movie_info=single_user_data["watched"]
    list_of_frnds_watched_dicts=single_user_data["friends"]
    list_of_user_movie_titles=[]
    list_of_friends_movie_titles=[]
    list_of_unique_user_movie_info=[]
    
    #Adds user's watched movie titles to a list
    for user_movie_info in list_of_user_movie_info:
        list_of_user_movie_titles.append(user_movie_info["title"])
 
    #Adds friends' watched movie titles to a list
    for frnds_watched_movie_info in list_of_frnds_watched_dicts:
        for frnds_watched_movie_titles in frnds_watched_movie_info["watched"]:
            list_of_friends_movie_titles.append(frnds_watched_movie_titles["title"])

    #Uses sets data structure and difference method to add user's unique move titles that only the user has seen to a list
    list_of_unique_user_movie_titles=set(list_of_user_movie_titles).difference(set(list_of_friends_movie_titles))
    
    #Adds movie info from a list of the user's watched movie info to a new list if the movie title is in the list of the user's unique movie titles
    for user_movie_info in list_of_user_movie_info:
        if user_movie_info["title"] in list_of_unique_user_movie_titles:
            list_of_unique_user_movie_info.append(user_movie_info)
    return list_of_unique_user_movie_info

def get_friends_unique_watched(single_user_data):
    list_of_user_movie_info=single_user_data["watched"]
    list_of_frnds_watched_dicts=single_user_data["friends"]
    list_of_user_movie_titles=[]
    list_of_friends_movie_titles=[]
    list_of_unique_frnds_movie_info=[]

    #Adds user's watched movie titles to a list
    for user_movie_info in list_of_user_movie_info:
        list_of_user_movie_titles.append(user_movie_info["title"])

    #Adds friends' watched movie titles to a list
    for frnds_watched_movie_info in list_of_frnds_watched_dicts:
        for frnds_watched_movie_titles in frnds_watched_movie_info["watched"]:
            list_of_friends_movie_titles.append(frnds_watched_movie_titles["title"])
    
    #Uses sets data structure and difference method to add friends' unique move titles that at least one friend has seen to a list
    list_of_unique_frnds_movie_titles=set(list_of_friends_movie_titles).difference(set(list_of_user_movie_titles))
    
    #Adds movie info from a list of friends' watched movie info to a new list if the movie title is in the list of friends' unique movie titles (and isn't already in the new list)
    for frnds_watched_movie_info in list_of_frnds_watched_dicts:
        for frnds_movie_info in frnds_watched_movie_info["watched"]:
            if frnds_movie_info["title"] in list_of_unique_frnds_movie_titles and frnds_movie_info not in list_of_unique_frnds_movie_info:
                list_of_unique_frnds_movie_info.append(frnds_movie_info)
    return list_of_unique_frnds_movie_info

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(single_user_data):
    list_of_user_movie_info=single_user_data["watched"]
    list_of_user_movie_hosts=single_user_data["subscriptions"]
    list_of_users_unwatched_movie_info=[]
    list_of_recommended_movie_info=[]

    #Uses wave_03 function to add user's friends' unique watched movie info to a list
    list_of_unique_frnds_movie_info=get_friends_unique_watched(single_user_data)

    #Adds friends' movie info to user's unwatched list if it has not already been watched
    for movie_info in list_of_unique_frnds_movie_info:
        if movie_info not in list_of_user_movie_info:
            list_of_users_unwatched_movie_info.append(movie_info)

    #Adds user's unwatched movie into to user's recommended list if they are subscribed to the movie's host
    for movie_info in list_of_users_unwatched_movie_info:
        if movie_info["host"] in list_of_user_movie_hosts:
            list_of_recommended_movie_info.append(movie_info)
    return list_of_recommended_movie_info

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(single_user_data):
    #Returns an empty list if the user does not have a most frequent genre
    if len(single_user_data["watched"]) == 0:
        return []
    
    #Returns an empty list if the user's friends do not have watchlists with movie info that can be used to get available movie recommendations
    if len(get_friends_unique_watched(single_user_data)) == 0 :
        return []

    users_most_frequent_genre=get_most_watched_genre(single_user_data)
    list_of_users_recco_movie_info=get_available_recs(single_user_data)
    print(list_of_users_recco_movie_info)
    list_of_users_recco_movie_info_by_genre=[]

    #Adds recommended movie info to new list if the movie's genre is the most watched genre
    for movie_info in list_of_users_recco_movie_info:
        if movie_info["genre"] == users_most_frequent_genre:
            list_of_users_recco_movie_info_by_genre.append(movie_info)
    return list_of_users_recco_movie_info_by_genre

def get_rec_from_favorites(single_user_data):
    #Returns an empty list if the user does not have a favorites list
    if len(single_user_data["favorites"]) == 0:
        return []

    list_of_users_recco_movies_by_favorites=[]
    list_of_user_favorties_movie_info=single_user_data["favorites"]
    #Uses wave_03 function to add user's unique watched (friends have not watched) movie info to a list
    list_of_unique_user_movie_info=get_unique_watched(single_user_data)

    #Adds movie info to a new list if only the user has watched it and it is in the user's favorites list
    for movie_info in list_of_user_favorties_movie_info:
        if movie_info in list_of_unique_user_movie_info:
            list_of_users_recco_movies_by_favorites.append(movie_info)
    return list_of_users_recco_movies_by_favorites
