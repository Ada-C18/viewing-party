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

def get_unique_watched(single_user_data):
    list_of_user_movie_info=single_user_data["watched"]
    # print(list_of_user_movie_info)
    list_of_frnds_watched_dicts=single_user_data["friends"]
    # print(list_of_frnds_watched_dicts)
    list_of_user_movie_titles=[]
    list_of_friends_movie_titles=[]
    list_of_unique_user_movie_info=[]

    for user_movie_info in list_of_user_movie_info:
        list_of_user_movie_titles.append(user_movie_info["title"])
    # print(list_of_user_movie_titles)

    for frnds_watched_movie_info in list_of_frnds_watched_dicts:
        for frnds_watched_movie_titles in frnds_watched_movie_info["watched"]:
            list_of_friends_movie_titles.append(frnds_watched_movie_titles["title"])
    # print(list_of_friends_movie_titles)

    list_of_unique_user_movie_titles=set(list_of_user_movie_titles).difference(set(list_of_friends_movie_titles))
    # print(list_of_unique_user_movies)
    
    for user_movie_info in list_of_user_movie_info:
        if user_movie_info["title"] in list_of_unique_user_movie_titles:
            list_of_unique_user_movie_info.append(user_movie_info)
    # print(list_of_unique_user_movie_info)
    return list_of_unique_user_movie_info

def get_friends_unique_watched(single_user_data):
    list_of_user_movie_info=single_user_data["watched"]
    # print(list_of_user_movie_info)
    list_of_frnds_watched_dicts=single_user_data["friends"]
    # print(list_of_frnds_watched_dicts)
    list_of_user_movie_titles=[]
    list_of_friends_movie_titles=[]
    list_of_unique_frnds_movie_info=[]

    for user_movie_info in list_of_user_movie_info:
        list_of_user_movie_titles.append(user_movie_info["title"])
    # print(list_of_user_movie_titles)

    for frnds_watched_movie_info in list_of_frnds_watched_dicts:
        for frnds_watched_movie_titles in frnds_watched_movie_info["watched"]:
            list_of_friends_movie_titles.append(frnds_watched_movie_titles["title"])
    # print(list_of_friends_movie_titles)

    list_of_unique_frnds_movie_titles=set(list_of_friends_movie_titles).difference(set(list_of_user_movie_titles))
    print(list_of_unique_frnds_movie_titles, '/n')
    
    for frnds_watched_movie_info in list_of_frnds_watched_dicts:
        for frnds_movie_info in frnds_watched_movie_info["watched"]:
            if frnds_movie_info["title"] in list_of_unique_frnds_movie_titles and frnds_movie_info not in list_of_unique_frnds_movie_info:
                list_of_unique_frnds_movie_info.append(frnds_movie_info)
    print(list_of_unique_frnds_movie_info)
    return list_of_unique_frnds_movie_info


test_user_data={   'friends': [   {   'watched': [   {   'genre': 'Fantasy',
                                          'rating': 4.8,
                                          'title': 'The Lord of the Functions: '
                                                   'The Fellowship of the '
                                                   'Function'},
                                      {   'genre': 'Fantasy',
                                          'rating': 4.0,
                                          'title': 'The Lord of the Functions: '
                                                   'The Return of the Value'},
                                      {   'genre': 'Fantasy',
                                          'rating': 4.0,
                                          'title': 'The Programmer: An '
                                                   'Unexpected Stack Trace'},
                                      {   'genre': 'Intrigue',
                                          'rating': 3.0,
                                          'title': 'Zero Dark Python'},        
                                      {   'genre': 'Horror',
                                          'rating': 3.5,
                                          'title': 'It Came from the Stack '
                                                   'Trace'}]},
                   {   'watched': [   {   'genre': 'Fantasy',
                                          'rating': 4.8,
                                          'title': 'The Lord of the Functions: '
                                                   'The Fellowship of the '
                                                   'Function'},
                                      {   'genre': 'Action',
                                          'rating': 2.2,
                                          'title': 'The JavaScript and the '
                                                   'React'},
                                      {   'genre': 'Intrigue',
                                          'rating': 2.0,
                                          'title': 'Recursion'},
                                    #   {   'genre': 'Intrigue',
                                    #       'rating': 3.0,
                                    #       'title': 'Zero Dark Python'},             
                                      {   'genre': 'Intrigue',
                                          'rating': 3.0,
                                          'title': 'Zero Dark Python'}]}],
    'watched': [   {   'genre': 'Fantasy',
                       'rating': 4.8,
                       'title': 'The Lord of the Functions: The Fellowship of '
                                'the Function'},
                   {   'genre': 'Fantasy',
                       'rating': 4.0,
                       'title': 'The Lord of the Functions: The Two '
                                'Parameters'},
                   {   'genre': 'Fantasy',
                       'rating': 4.0,
                       'title': 'The Lord of the Functions: The Return of the '
                                'Value'},
                   {   'genre': 'Action',
                       'rating': 2.2,
                       'title': 'The JavaScript and the React'},
                   {'genre': 'Intrigue', 'rating': 2.0, 'title': 'Recursion'},
                   {   'genre': 'Intrigue',
                       'rating': 4.5,
                       'title': 'Instructor Student TA Manager'}]}

get_friends_unique_watched(test_user_data) 

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

