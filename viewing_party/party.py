# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating): #Wave 1, step 1 done
    movie_dict={}
    if title is None or genre is None or rating is None:
        return None

    movie_dict["title"]=title
    movie_dict["genre"]=genre
    movie_dict["rating"]=rating
    # print(movie_dict["title"])
    return movie_dict
# create_movie('tit','gen',5)

def add_to_watched(user_watched_dict,movie_info):
    user_watched_dict["watched"] = [movie_info]
    return user_watched_dict

def add_to_watchlist(user_watchlist_dict, movie_info):
    user_watchlist_dict["watchlist"] = [movie_info]
    return user_watchlist_dict

def watch_movie(single_user_data,movie_title):    
    list_of_watchlist_movie_info=single_user_data["watchlist"]
    list_of_watched_movie_info=single_user_data["watched"]

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
    number_of_watched_movies=len(list_of_watched_movie_info)
    list_of_movie_ratings=[]
    sum_of_all_ratings=0

    if len(list_of_watched_movie_info) == 0:
        return 0.0

    for movie_info in list_of_watched_movie_info:
        list_of_movie_ratings.append(movie_info["rating"])

    for rating in list_of_movie_ratings:
        sum_of_all_ratings+=rating

    average_rating=sum_of_all_ratings/number_of_watched_movies
    return average_rating

def get_most_watched_genre(single_user_data):
    list_of_watched_movie_info=single_user_data["watched"]
    list_of_genres=[]
    genre_counter_dict={}
    list_of_watched_genre_counts=[]

    if len(list_of_watched_movie_info) == 0:
        return None

    for movie_info in list_of_watched_movie_info:
        list_of_genres.append(movie_info['genre'])

    for genre in list_of_genres:
        if not genre in genre_counter_dict:
            genre_counter_dict[genre] = 1
        else:
            genre_counter_dict[genre] += 1
    
    for genre_count_value in genre_counter_dict.values():
        list_of_watched_genre_counts.append(genre_count_value)

    max_watched_genre_count=max(list_of_watched_genre_counts)

    for genre,genre_count_value in genre_counter_dict.items():
        if genre_count_value == max_watched_genre_count:
            return genre

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

